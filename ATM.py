n = int(input())
a = list(map(int, input().split()))

b = 0
a.sort()

for i in range(0, n+1):
    b += sum(a[0:i])

print(b)
