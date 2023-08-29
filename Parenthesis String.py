a = []

def replace(str):
    str = str.replace("()", '')
    if(str.find("()") != -1):
        str = replace(str)
    return str

a.append(int(input()))
for i in range(a[0]):
    a.append(input())

for i in range(1, a[0] + 1):
    if(a[i].find("()") != -1):
        a[i] = replace(a[i])

for i in range(1, a[0] + 1):
    if(a[i]): print("NO")
    else: print("YES")