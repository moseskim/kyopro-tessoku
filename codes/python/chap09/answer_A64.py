import heapq

# 입력
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 인접 리스트 작성(가중치가 있는 그래프이므로, 각 에지에 대해 (인접 노드, 가중치)의 튜플을 기록한다)
G = [ list() for i in range(N + 1) ]
for a, b, c in edges:
	G[a].append((b, c))
	G[b].append((a, c))

# 배열/큐의 초기화(큐에는 (거리, 노드 번호) 튜플을 기록한다)
INF = 10 ** 10
kakutei = [ False ] * (N + 1)
cur = [ INF ] * (N + 1)
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1))

# 다이크스트라 알고리즘
while len(Q) >= 1:
	# 다음으로 확정할 노드를 구한다
	# （ここでは、優先度付きキュー Q の最小要素を取り除き、その要素の 2 番目の値（頂点番号）を pos に代入する）
	pos = heapq.heappop(Q)[1]

	# Q의 최소 요소가 '이미 확정한 노드'인 경우
	if kakutei[pos] == True:
		continue
	
	# cur[x] 값을 업데이트 한다
	kakutei[pos] = True
	for e in G[pos]:
		# 책의 코드의 pos = e[0], cost = e[1]에 대응한다
		if cur[e[0]] > cur[pos] + e[1]:
			cur[e[0]] = cur[pos] + e[1]
			heapq.heappush(Q, (cur[e[0]], e[0]))

# 답을 출력
for i in range(1, N + 1):
	if cur[i] != INF:
		print(cur[i])
	else:
		print("-1")