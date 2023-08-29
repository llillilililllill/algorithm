num = int(input())
sum = 0
for i in range(1, num+1):
    h = int(i/100)
    t = int((i%100)/10)
    o = int(i%10)
    if(h == 0):
        sum = sum + 1
    else:
        if(h-t == t-o):
            sum = sum + 1

print(sum)