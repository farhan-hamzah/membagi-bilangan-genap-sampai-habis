num = int(input())
i = 0
while num > 0:
    if num%2 == 0:
        num = num/2
        i += 1
    else:
        num = num -1 
        i += 1
print(i)

