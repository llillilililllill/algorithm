n = int(input())
a = []
s = []
p = []
x = 1
y = 0
m = True

for i in range(n):
    a.append(int(input()))

for i in a:
    if i >= x:
        for j in range(x, i+1):
            s.append(j)
            p.append("+")
            y = x
            x += 1
        s.pop()
        p.append("-")
        y -= 1
    if s:
        if i == s[-1]:
            s.pop()
            p.append("-")
            y -= 1
            continue
        if i < s[-1]:
            print("NO")
            m = False
            break

if m:
    for i in p:
        print(i)

