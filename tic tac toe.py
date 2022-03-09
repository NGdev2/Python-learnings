field = ["|", "1", "2", "3", "|",
         "|", "4", "5", "6", "|",
         "|", "7", "8", "9", "|"]

player = 1
end = False
name1 =  str(input(f"\nEnter your name, Player 1! "))
name2 =  str(input(f"\nEnter your name, Player 1! "))

def turn(player):
    change = False
    if player == 1:
        mark = "X"
    else:
        mark = "0"

    
    while change == False:
        for i in range(15):
            print(field[i], end=" ")
            if (i == 4 or i == 9):
                print(end="\n")
        enter = int(input(f"\nХод игрока {name1 if (player == 1) else name2 }:"))
        if (enter > 0 and enter < 4):
            if field[enter] == str(enter):
                field[enter] = mark
            else:
                continue
        elif (enter < 7):
            if field[enter + 2] == str(enter):
                field[enter + 2] = mark
            else:
                continue
        elif (enter < 10):
            if field[enter + 4] == str(enter):
                field[enter + 4] = mark
            else:
                continue
        else:
            continue

        change = True
    if player == 1:
        return 2
    else:
        return 1


while end == False:
    player = turn(player)
    if (field[1] == field[6] == field[11] or field[2] == field[7] == field[12] or field[3] == field[8] == field[13] or
            field[1] == field[7] == field[13] or field[3] == field[7] == field[11] or field[1] == field[2] == field[
                3] or
            field[6] == field[7] == field[8] or field[11] == field[12] == field[13]):
        end = True
       

        print(f"player {name1 if player == 2 else name2} wins:")
        for i in range(15):
            print(field[i], end=" ")
            if (i == 4 or i == 9):
                print(end="\n")

    elif (field[1] != "1" and field[6] != "4" and field[11] != "7" and field[2] != "2"  and field[7] != "5" and field[12] != "8" and field[3] != "3" and field[8] != "6" and field[13] != "9"):
        end = True
        for i in range(15):
            print(field[i], end=" ")
            if (i == 4 or i == 9):
                print(end="\n")
        print("НИЧЬЯ")
