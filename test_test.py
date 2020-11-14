print("поиск совпадений")
A = [2, False, 9.1, 2 - 1j, "hello", 5, "python"]
B = [5, 3, "HELLO", 7, 12.5, "Python", True, False]
print("1-й список:", A)
print("2-й список:", B)
print("Совпадения:")
i = 0
for a in A:
    i = i + 1
    j = 0
    for b in B:
        j = j + 1
        if a == b:
            # если элементы совпадают
            txt = str(i) + "-й элемент 1-го списка и "
            txt = txt + str(j) + "-й элемент 2-го списка - " + str(a)
            print(txt)
print("finish")

