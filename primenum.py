x, y = map(int, input().split())

a = [0] * (y+1)

for i in range(2, y+1):
    for j in range(2, y+1):
        if(i*j > y): break
        a[i*j] += 1

for i in range(x, y + 1):
    if(a[i] == 0 and i != 1): print(i)