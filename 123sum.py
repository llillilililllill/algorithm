a = []
global answer

def one(n, x):
    n += 1
    num(n, x)

def two(n, x):
    n += 2
    num(n, x)

def three(n, x):
    n += 3
    num(n, x)

def num(n, x):
    global answer
    if(n == x):
        answer += 1
        return
    if(n > x):
        return
    one(n, x)
    two(n, x)
    three(n, x)

a.append(int(input()))
for i in range(a[0]):
    a.append(int(input()))

for i in range(1, a[0]+1):
    answer = 0
    num(0, a[i])
    print(answer)
