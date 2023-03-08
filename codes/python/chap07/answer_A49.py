import copy

# 1번의 조작(P[i], Q[i], R[i])을 나타내는 구조체
class round:
	def __init__(self, p, q, r):
		self.p = p
		self.q = q
		self.r = r

# 국면의 상태를 나타내는 구조체
class state:
	# 국면 상태 초기화
	def __init__(self, n):
		self.score = 0      # 잠정 점수
		self.x = [ 0 ] * n  # 현재 배열 X의 값
		self.lastmove = '?' # 마지막 동작('A' 또는 'B', 단, 초기 상태에서는 '?'로 해 둔다)
		self.lastpos = -1   # Beam[i-1][어디]에서 전이했는가(단, 초기 상태에서는 -1로 해 둔다)

# 빔 서치를 수행하는 함수
def beam_search(N, T, rounds):
	# 2차원 배열 beam을 준비하고, 0번째 수의 상태를 설정
	WIDTH = 10000
	beam = [ list() for i in range(T + 1) ]
	beam[0].append(state(N))

	# 빔 서치
	for i in range(T):
		candidate = list()
		for j in range(len(beam[i])):
			# 조작 A인 경우
			sousa_a = copy.deepcopy(beam[i][j])
			sousa_a.lastmove = 'A'
			sousa_a.lastpos = j
			sousa_a.x[rounds[i].p] += 1
			sousa_a.x[rounds[i].q] += 1
			sousa_a.x[rounds[i].r] += 1
			sousa_a.score += sousa_a.x.count(0) # 점수에 'sousa_a.x에 포함된 0의 갯수'를 가산
			# 조작 B인 경우
			sousa_b = copy.deepcopy(beam[i][j])
			sousa_b.lastmove = 'B'
			sousa_b.lastpos = j
			sousa_b.x[rounds[i].p] -= 1
			sousa_b.x[rounds[i].q] -= 1
			sousa_b.x[rounds[i].r] -= 1
			sousa_b.score += sousa_b.x.count(0) # 점수에 'sousa_a.x에 포함된 0의 갯수'를 가산
			# 후보에 추가
			candidate.append(sousa_a)
			candidate.append(sousa_b)
		# 정렬해서 beam[i+1]의 결과를 계산한다
		candidate.sort(key = lambda s: -s.score)
		beam[i + 1] = copy.deepcopy(candidate[:WIDTH]) # 최대 candidate의 상위 WIDTH건만 기록할 수 있다
	
	# 빔 서치 복원
	current_place = 0
	answer = [ None ] * T
	for i in range(T, 0, -1):
		answer[i - 1] = beam[i][current_place].lastmove
		current_place = beam[i][current_place].lastpos
	return answer


# 입력
T = int(input())
rounds = [ None ] * T
for i in range(T):
	p, q, r = map(int, input().split())
	rounds[i] = round(p - 1, q - 1, r - 1) # 책과 달리, 여기에서는 0-indexed로 하기 위해 1을 뺀다

# 빔 서치를 수행하고 답을 구한다(책과 달리, 빔 서치 복원은 함수 안에서 수행한다)
answer = beam_search(20, T, rounds)

# 출력
for c in answer:
	print(c)

# 주의 1: 이 프로그램은 Python으로 제출하면 빔 폭 200정도, PyPy3으로 제출하면 빔 폭 350 정도로, 실행 시간 제한 1초에 아슬아슬하게 됩니다.
# 주의 2: 여기에서는 deepcopy 함수를 사용했으나, 이 함수가 실행 속도를 늦추는 원인이 됩니다.
#        이것을 사용하지 않고 구현하면, 프로그램의 속도가 보다 빨라져, 빔 폭을 늘릴 수 있습니다. 생각해 보십시오.
