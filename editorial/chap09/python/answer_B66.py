# 에지를 줄이면서 연결성을 답하는 것은 어려우므로, 쿼리를 역방향으로 해서 에지를 늘리면서 답한다

N, M = map(int, input().split())

edge = []
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge.append((A, B))

# 마지막까지 있는 에지를 구한다
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
last = [True] * M
for q in query:
    if q[0] == 1:
        q[1] -= 1
        last[q[1]] = False
    else:
        q[1] -= 1
        q[2] -= 1

# union-find
uf = [-1] * N
def root(i: int) -> int:
    # path halving
    while True:
        if uf[i] < 0:
            return i
        if uf[uf[i]] < 0:
            return uf[i]
        uf[i] = uf[uf[i]]
        i = uf[i]
def unite(i: int, j: int):
    i = root(i)
    j = root(j)
    if i == j:
        return
    # 병합 기법 (union by size)
    if uf[i] > uf[j]:
        i, j = j, i
    uf[i] += uf[j]
    uf[j] = i

ans = []
for i in range(M):
    if last[i]:
        A, B = edge[i]
        unite(A, B)

for q in reversed(query):
    if q[0] == 1:
        A, B = edge[q[1]]
        unite(A, B)
    else:
        _, U, V = q
        ans.append("Yes" if root(U) == root(V) else "No")

for s in reversed(ans):
    print(s)
