from collections import deque

# 입력
Q = int(input()) # 쿼리 수
queries = [ input().split() for i in range(Q) ] # 쿼리 정보(각 요소는 ["1", 제목을_나타내는_문자열] 또는 ["2"] 또는 ["3"]）

# 쿼리 처리
S = deque()
for q in queries:
	if q[0] == "1":
		S.append(q[1])
	if q[0] == "2":
		print(S[-1])
	if q[0] == "3":
		S.pop()