x = int(input("Введите минимальную сумму инвестиций:"))
a = int(input("Введите сумму,которую может вложить Майкл:"))
b = int(input("Введите сумму,которую может вложить Иван:"))
if a >= x and b>=x:
    print(2)
elif a >= x:
    print("Майкл")
elif b >= x:
    print("Иван")
elif a + b >= x:
    print(1)
else:
    print(0)

