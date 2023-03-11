import sys

# 재귀 호출의 깊이 상한을 120000로 설정
sys.setrecursionlimit(120000)

# 깊이 우선 탐색을 수행하는 함수(pos는 현재 위치, visited[x]는 노드 x가 파란색인가를 나타내는 불리언값)
def dfs(pos, G, visited):
	visited[pos] = True
	for i in G[pos]:
		if visited[i] == False:
			dfs(i, G, visited)

# 입력
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 인접 리스트 작성
G = [ list() for i in range(N + 1) ] # G[i]는 노드 i에 인접하는 노드의 리스트
for a, b in edges:
	G[a].append(b) # 노드 a에 인접하는 노드로 b를 추가
	G[b].append(a) # 노드 b에 인접하는 노드로 a를 추가

# 깊이 우선 탐색
visited = [ False ] * (N + 1)
dfs(1, G, visited)

# 연결 여부 판정(answer = True일 때 연결)
answer = True
for i in range(1, N + 1):
	if visited[i] == False:
		answer = False

# 답 출력
if answer == True:
	print("The graph is connected.")
else:
	print("The graph is not connected.")