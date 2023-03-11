from collections import deque

# 입력(여기에서는 책과 달리 램프의 번호가 0-indexed가 되도록 구현하고 있다)
N, M = map(int, input().split())
A = list(map(int, input().split()))
actions = [ list(map(lambda x: int(x) - 1, input().split())) for i in range(M) ] # ここでは X[i], Y[i], Z[i] を 0-indexed に変換して受け取る

# 노드 pos의 상태에서 '램프 x, y, z의 상태'를 반전시켰을 때의 노드 번호를 반환하는 함수
def get_next(pos, x, y, z):
	# pos의 2진법 표기를 사용해, 노드 pos가 나타내는 램프의 상태 state를 계산
	# （pos の 2^i の位は (pos // (2 ** i)) % 2 で計算できる → 1.4 節を参照）
	state = [ (pos // (2 ** i)) % 2 for i in range(N) ]
	# ランプ x, y, z を反転
	state[x] = 1 - state[x]
	state[y] = 1 - state[y]
	state[z] = 1 - state[z]
	# ランプの状態 state を指す頂点の番号を計算
	# （2 進法を 10 進法に変換する方法は 1.4 節を参照）
	ret = 0
	for i in range(N):
		if state[i] == 1:
			ret += 2 ** i
	return ret

# グラフに辺を追加
G = [ list() for i in range(2 ** N) ]
for i in range(2 ** N):
	for x, y, z in actions:
		nextstate = get_next(i, x, y, z)
		G[i].append(nextstate)

# 시작 지점/골 지점의 노드 번호를 결정한다
start = 0
for i in range(N):
	if A[i] == 1:
		start += 2 ** i
goal = 2 ** N - 1

# 너비 우선 탐색 초기화
dist = [ -1 ] * (2 ** N)
dist[start] = 0
Q = deque()
Q.append(start)

# 너비 우선 탐색
while len(Q) >= 1:
	pos = Q.popleft() # 큐 Q의 맨 앞 요소를 제거하고, 그 값을 pos에 대입한다
	for nex in G[pos]:
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.append(nex)

# 답을 출력
print(dist[goal])

# 注意 1：この問題に対してはより簡潔な実装もありますので、
#         もしよければ answer_A70_extra.py もご覧ください。