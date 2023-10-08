word = input("Введите слово:")
vowels = {}
if not word.islower():
    print("False")
else:
    consonants = 0
    vowels_count = 0
    for letter in word:
        if letter in vowels:
            vowels_count += 1
        elif letter.isalpha():
            consonants += 1
            print("Количество согласных букв:",consonants)
            print("Количество гласных букв:", vowels_count)
    
   
