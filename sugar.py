num = int(input())
n = []

for i in range(0, int(num/5+1)):
    for j in range(0, int((num - 5 * i)/3+1)):
        if(num == 5*i + 3*j):
            n.append(i+j)

if(n):
    print(min(n))
else: print(-1)
