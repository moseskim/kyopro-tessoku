import heapq


G = [list() for _ in range(375)] # G[i]는 i번째 날부터 시작하는 업무의 급여 리스트

# 입력
N, D = map(int, input().split())
for _ in range(N):
	X, Y = map(int, input().split())
	G[X].append(Y)

# 답을 구한다
Q = []
Answer = 0
for i in range(1, D + 1):
	# i번째 날부터 시작하는 업무를 큐에 추가
	# heap은 최솟값을 추출하므로 -1배 한다
	for y in G[i]: heapq.heappush(Q, -y)

	# 할 업무를 선택하고, 그 업무를 큐에서 삭제한다
	if Q:
		Answer -= heapq.heappop(Q)

# 출력
print(Answer)
