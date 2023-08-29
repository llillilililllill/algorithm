import sys
sys.setrecursionlimit(10**6)

num = int(input())
result = [0] * num

for number in range(num):

    N, M, K = map(int, input().split())

    ground = [[False] * N for _ in range(M)]

    for i in range(K):
        a, b = map(int, input().split())
        ground[b][a] = i+1

    graph = [[False] * (K) for _ in range(K)]

    for i in range(M):
        for j in range(N):
            if not i == M-1:
                if ground[i][j] != False and ground[i + 1][j] != False:
                    graph[ground[i][j]-1][ground[i + 1][j]-1] = True
                    graph[ground[i + 1][j]-1][ground[i][j]-1] = True

            if not j == N-1:
                if ground[i][j] != False and ground[i][j + 1] != False:
                    graph[ground[i][j]-1][ground[i][j + 1]-1] = True
                    graph[ground[i][j + 1]-1][ground[i][j]-1] = True

    visited = [False] * K


    def dfs(V):
        visited[V] = True  # 해당 V값 방문처리
        for i in range(1, K):
            if not visited[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
                dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)




    for i in range(K):
        if visited[i] == False:
            dfs(i)
            result[number] += 1

for i in range(num):
    print(result[i])
