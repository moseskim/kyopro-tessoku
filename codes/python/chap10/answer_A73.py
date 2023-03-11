import heapq

# 입력
N, M = map(int, input().split())
roads = [ list(map(int, input().split())) for i in range(M) ]

# 그래프 작성
G = [ list() for i in range(N + 1) ]
for a, b, c, d in roads:
	if d == 1:
		G[a].append((b, 10000 * c - 1))
		G[b].append((a, 10000 * c - 1))
	else:
		G[a].append((b, 10000 * c))
		G[b].append((a, 10000 * c))

# 다이크스트라 알고리즘(다이크스트라 알고리즘에 대한 자세한 설명은 책 9.4절 및 ../chap09/answer_A64.py를 참조)
INF = 10 ** 10
kakutei = [ False ] * (N + 1)
cur = [ INF ] * (N + 1)
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1))
while len(Q) >= 1:
	pos = heapq.heappop(Q)[1]
	if kakutei[pos] == True:
		continue
	kakutei[pos] = True
	for e in G[pos]:
		if cur[e[0]] > cur[pos] + e[1]:
			cur[e[0]] = cur[pos] + e[1]
			heapq.heappush(Q, (cur[e[0]], e[0]))

# 답을 구해서 출력
# 마라톤 코스의 거리: cur[N] / 10000의 소수점 이하를 버린 값
# 코스 상의 나무의 수: cur[N]과 distance * 10000 의 차이
distance = (cur[N] + 9999) // 10000
num_trees = distance * 10000 - cur[N]
print(distance, num_trees)