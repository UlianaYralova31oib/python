pets = {}

pet_name = input("Введите кличку питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

def get_suffix(age):
    if age == 1:
        return "год"
    elif 1 < age < 5:
        return "года"
    else:
        return "лет"

suffix = get_suffix(pet_age)
print(f"Это {pet_type} по кличке \"{pet_name}\". Возраст питомца: {pet_age} {suffix}. Имя владельца: {owner_name}")

