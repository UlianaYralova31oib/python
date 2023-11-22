t = int(input())
n = int(input())
weights = []
for i in range(n):
    weights.append(int(input()))
    weights.sort()
    i = 0
    j = n-1
    boats = 0 
    while i <=j:
        if weights[j] + weights[i] <= t:
            i +=1
            j -=1
            boats +=1
            print(boats)

        
