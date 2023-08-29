n = int(input())
sum = [0,0,0,0,0,0]
def pizza(n, i, x):
    a = i * (n-i)
    b = [0,0,0,0,0]
    c = [0,0,0,0,0]

    if(i != 1):
        for j in range(1, int(i/2+1)):
            b[j] = pizza(i, j, x)

    for j in range(1, int((n-i)/2+1)):
        c[j] = pizza(n-i, j, x)

    return a + max(c) + max(b)

for i in range(1, int(n/2+1)):
    x = i
    sum[i] = pizza(n, i, x-1)

print(max(sum))
