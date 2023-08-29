
a = []
b = []
n = []
sum = 0
time = 0

def score(s):
    if(s == "D0"): return 1.0
    if(s == "D+"): return 1.5
    if(s == "C0"): return 2.0
    if(s == "C+"): return 2.5
    if(s == "B0"): return 3.0
    if(s == "B+"): return 3.5
    if(s == "A0"): return 4.0
    if(s == "A+"): return 4.5


for i in range(20):
    a.append(input())
    b.append("X")
    n.append(0)

for i in range(len(a)):
    a[i] = a[i][-6:]

    if(a[i][-1:] == "P" or a[i][-1:] == "F"):
        if(a[i][-1:] == "F"):
            n[i] = a[i][1]
            b[i] = 0
    else:
        b[i] = score(a[i][-2:])
        n[i] = a[i][0]

for i in range(len(b)):
    if(b[i] != "X"):
        sum = sum + b[i] * float(n[i])
        time = time + int(n[i])

grade = sum / time

print(grade)