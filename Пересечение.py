numbers1 = set(map(int,input().split()))
numbers2 = set(map(int,input().split()))
common_numbers = numbers1.intersection(numbers2)
print(len(common_numbers))
