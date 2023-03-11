import itertools

# 입력
H, W, K = map(int, input().split())
c = [ input() for i in range(H) ]

# 잔여 remaining_steps번의 '열에 대한 조작'으로, 최대 몇 개의 칸을 검은 색으로 할 수 있는지 반환하는 함수
def paint_row(H, W, d, remaining_steps):
	# 각 열에 대해 (흰색 칸의 갯수, 열의 번호)의 튜플을 기록하고, 내림차순으로 정렬한다
	column = [ ([ d[i][j] for i in range(H) ].count('.'), j) for j in range(W) ]
	column.sort(reverse = True)

	# 열에 대해 조작을 수행한다
	for j in range(remaining_steps):
		idx = column[j][1]
		for i in range(H):
			d[i][idx] = '#'
	
	# 검은색 칸의 갯수를 세어서 반환한다
	return sum(map(lambda l: l.count('#'), d))

# 행을 칠하는 방법을 전탐색
# (여기에서는 '비트 전탐색'이 아니라 itertools.product를 사용해 2^H개의 칠하는 방법을 모두 열가한다)
answer = 0
for v in itertools.product([ 0, 1 ], repeat = H):
	# 행에 대해 조작을 수행한다(paint_row 함수로 몇 개의 d[i][j]를 바꿔 쓰기 위해, d는 string 배열이 아닌, 2차원 리스트로 한다)
	d = [ list(c[i]) for i in range(H) ]
	remaining_steps = K
	for i in range(H):
		if v[i] == 1:
			d[i] = [ '#' ] * W
			remaining_steps -= 1
	if remaining_steps >= 0:
		subanswer = paint_row(H, W, d, remaining_steps)
		answer = max(answer, subanswer)

# 출력
print(answer)