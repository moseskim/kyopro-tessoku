# 입력
Q = int(input()) # 쿼리 수
queries = [ input().split() for i in range(Q) ] # 쿼리 정보(각 요소는 ["1", 이름을_나타내는_문자열, 득점을_나타내는_문자열] 또는 ["2", 이름을_나타내는_문자열]）

# 쿼리 처리
Map = {}
for q in queries:
	if q[0] == "1":
		Map[q[1]] = q[2]
	if q[0] == "2":
		print(Map[q[1]])