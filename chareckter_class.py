class Character():
    """It's a Character class."""

    MAX_SPEED = 100  #this is a constant value
    dead_health = 0
    _diplomacy = 6/10

    def __init__(self, race, damage=5, armor=3):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100
        self._current_speed = 5

    def get_damage(self, damage):
        self.health = self.health - (damage-self.armor if (damage >= self.armor) else None)
        return self.health

    def is_dead(self):
        return self.health == Character.dead_health

    @property #разрешает читать зищищенный атрибут
    def diplomacy(self):
        return self._diplomacy

    @property
    def current_speed(self):
        return self.current_speed

    @current_speed.setter #позволяет читать свойство атрибута и также записывать по заданной логике
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 10:
            self._current_speed = 10
        else:
            self._current_speed = current_speed


drengin = Character(race='Drengin Empire', damage=7)
print(drengin.race, drengin.get_damage(10))

alliance = Character(race='Terran Alliance', armor=5)
print(alliance.race, alliance.get_damage(10))
print(drengin.is_dead())
print(drengin.diplomacy)

alliance.current_speed = 6
print(alliance._current_speed)