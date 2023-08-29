a = []
stack = []

a.append(int(input()))
for i in range(a[0]):
    a.append(input())


for i in range(1, a[0] + 1):
    if(a[i].find('pop') != -1):
        if(stack):
            print(stack.pop())
        else: print(-1)
    if(a[i].find('size') != -1):
        print(len(stack))
    if(a[i].find('push') != -1):
        stack.append(a[i].strip()[5:])
    if(a[i].find('empty') != -1):
        if(stack): print(0)
        else: print(1)
    if(a[i].find('top') != -1):
        if(stack):
            print(stack[-1])
        else: print(-1)
