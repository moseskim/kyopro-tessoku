from collections import deque

# 입력(여기에서는 책과 달리 램프의 번호가 0-indexed가 되도록 구현하고 있다)
N, M = map(int, input().split())
A = list(map(int, input().split()))
actions = [ list(map(lambda x: int(x) - 1, input().split())) for i in range(M) ] # ここでは X[i], Y[i], Z[i] を 0-indexed に変換して受け取る

# 시작 지점/골 지점의 노드 번호를 결정한다
start = sum(A[i] * (2 ** i) for i in range(N))
goal = 2 ** N - 1

# 너비 우선 탐색 초기화
dist = [ -1 ] * (2 ** N)
dist[start] = 0
Q = deque()
Q.append(start)

# 너비 우선 탐색
# (여기에서는 그래프를 실제로 갖지 않고, pos에서 나오는 에지를 그대로 계산해서 너비 우선 탐색을 수행한다)
while len(Q) >= 1:
	pos = Q.popleft() # 큐 Q의 맨 앞 요소를 제거하고, 그 값을 pos에 대입한다
	for x, y, z in actions:
		# 비트 연산 XOR를 사용한다(XOR에 관해서는 칼럼 1 참조)
		# 램프 k를 반전시키는 것은, 노드 번호의 2^k의 자리를 반전시키는 것, 즉, 2^k를 XOR 시키는 것과 같다.
		nex = pos ^ (1 << x) ^ (1 << y) ^ (1 << z)
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.append(nex)

# 답을 출력
print(dist[goal])

# 주의 1: 비트 연산은 곱셈 (*), 나눗셈(//), 제곱(**) 등의 연산에 비해 속도가 빠르므로,
#        이 프로그램은 answer_A70.py에 비해 약 1/5의 실행 시간에 답을 구할 수 있습니다.