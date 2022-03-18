n, k = int(input("введите количество досок: ")), int(input("введите ширину рояля: "))
fence = []
min_sum = None


def amount(i1, i2, res):
    for d in range(i1, i2):
        res += fence[d]
    return res


if n < k or k < 1 or n > 1.5 * 10 ** 5:
    print("Input error")
else:
    for i in range(0, n):
        fence.append(int(input("Введите высоту доски %s: " % (i + 1))))

for i in range(0, n-k+1):
    if not min_sum:
        min_sum = amount(0, k, 0)
        continue

    if amount(i, i+k, 0) < min_sum:
        min_sum = amount(i, i+k, 0)
        ind = i + 1

print(f"минимальная сумма высот равна {min_sum} при j = {ind}.")
