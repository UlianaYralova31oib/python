def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        return result

def factorials_list(n):
    fact = factorial(n)
    result_list = [factorial(x) for x in 
                   range(fact, 0, -1)]
    return result_list

input_number = 3
print("Факториал числа", input_number, ":", factorial(input_number))
print("Список факториалов в убывающем порядке:", factorials_list(input_number))
