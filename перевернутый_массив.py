n = int(input("Введите количество чисел:"))
numbers = []
for _ in range (n):
num  = int(input())
numbers.append(num )
reversed_numbers = list (reversed(numbers))
print("Перевёрнутый массив:")
for num  in reversed_numbers:
    print(num )
