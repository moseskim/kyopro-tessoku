import heapq

# 입력
Q = int(input()) # 쿼리 수
queries = [ input().split() for i in range(Q) ] # 쿼리 정보(각 요소는 ["1", 가격을_나타내는_문자열] 또는 ["2"] 또는 ["3"]）

# 쿼리 처리
T = []
for q in queries:
	if q[0] == "1":
		heapq.heappush(T, int(q[1]))
	if q[0] == "2":
		print(T[0]) # T[0]는 '우선 순위 큐 안의 최소 요소'로 되어 있다
	if q[0] == "3":
		heapq.heappop(T)

# 주의 1: Python의 heapq 모듈은 deque 모듈과 달리, 함수를 사용해 list를 조작하는 형식입니다.
# 주의 2: 우선 순위 큐의 최소 요소는 T[0]로 추출하지만, 예를 들어 작은 쪽부터 2번째 요소를 T[1]로 추출할 수 있다고 단정할 수 없음에 주의합니다.
