from heapq import heappush, heappop

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    g[A].append((B, C))
    g[B].append((A, C))

INF = 1 << 61
cost = [INF] * N
back = [-1] * N
q = []

# 노드에 방문한 부분을 함수로 잘라낸다
def push(prev: int, i: int, c: int):
    if cost[i] <= c:
        return
    cost[i] = c
    back[i] = prev
    heappush(q, (c, i))

# 복원 사정상 뒤에서부터 Dijkstra 알고리즘
push(-1, N - 1, 0)
while q:
    c, x = heappop(q)
    if cost[x] != c:
        continue # 같은 노드에서 여러번 탐색하지 않는다(최악의 경우 Θ(N^2) 시간이 됩니다)
    for j, d in g[x]:
        push(x, j, c + d)

# 최단 경로를 복원
ans = [0]
while ans[-1] != N - 1:
    ans.append(back[ans[-1]])

for x in ans:
    print(x + 1)