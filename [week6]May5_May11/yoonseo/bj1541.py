arr = input().split('-')
num = []
for i in arr:
    sum = 0
    temp = i.split('+')
    for j in temp:
        sum += int(j)
    num.append(sum)
result = num[0]
for j in num[1:]:
    result -= j
print(result)