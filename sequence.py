import sys
input = sys.stdin.readline

num = int(input())
a = list(map(int, input().split()))
dp = [1] * num

for i in range(num):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))