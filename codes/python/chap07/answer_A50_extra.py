# 이 프로그램은 책 p.283 '한층 더 높이'를 구현한 담금질 알고리즘 코드입니다.
# 기반이 되는 등산 알고리즘에 관해서는 answer_A50.py를 참조하십시오.
# ※ 기대 점수는 대략 99.962억점입니다.

import math
import numpy as np
import random
import time
import sys

# 상수 설정, 입력
N = 100
Q = 1000
A = np.array([ list(map(int, input().split())) for i in range(N) ])

# 초기 해 생성
X = [ random.randint(0, N - 1) for i in range(Q) ]
Y = [ random.randint(0, N - 1) for i in range(Q) ]
H = [ 1 ] * Q
B = np.zeros((3 * N, 3 * N))
for i in range(Q):
	B[Y[i]][X[i]] += 1

# H = 1, 2, ..., N에 설정된 경우의 '증감분'을 가진 numpy 배열을 만든다
delta = [ None ] * (N + 1)
for i in range(1, N + 1):
	delta[i] = np.array([ [ max(i - abs(y) - abs(x), 0) for x in range(-i + 1, i) ] for y in range(-i + 1, i) ])

# 현재 점수를 얻는 함수
def get_score():
	return 200000000 - np.absolute(A - B[N:2*N, N:2*N]).sum()

# 등산 알고리즘 설정
# (현재 점수를 np.absolute(A - B[N:2*N, N:2*N]).sum()로 하고, 이것을 최대화하는 방법을 구현한다)
TIME_LIMIT = 5.4
current_score = get_score()
ti = time.time()

# 등산 알고리즘 시작
loops = 0
while time.time() - ti < TIME_LIMIT:
	# '작은 변경'을 무작위로 선택한다
	t = random.randint(0, Q - 1)
	h_limit = 14
	if current_score >= 199900000:
		h_limit = 1
	elif current_score >= 199500000:
		h_limit = 7
	old_x, new_x = X[t], X[t] + random.randint(-1, +1)
	old_y, new_y = Y[t], Y[t] + random.randint(-1, +1)
	old_h, new_h = H[t], H[t] + random.randint(-h_limit, +h_limit)
	if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or new_h <= 0 or new_h > N:
		continue
	
	# X[t] = new_x, Y[t] = new_y, H[t] = new_h로 변경(책의 Change(t, new_x, new_y, new_h) 호출에 대응)
	B[N+Y[t]-H[t]+1:N+Y[t]+H[t], N+X[t]-H[t]+1:N+X[t]+H[t]] -= delta[H[t]]
	X[t], Y[t], H[t] = new_x, new_y, new_h
	B[N+Y[t]-H[t]+1:N+Y[t]+H[t], N+X[t]-H[t]+1:N+X[t]+H[t]] += delta[H[t]]

	# 점수를 계산
	new_score = get_score()

	# 점수에 따라 채용 여부를 결정한다
	temperature = 180.0 - 179.0 * (time.time() - ti) / TIME_LIMIT
	probability = math.exp(min((new_score - current_score) / temperature, 0))
	if random.random() < probability:
		# 채용하는 경우
		current_score = new_score
	else:
		# 채용하지 않는 경우: X[t] = old_x, Y[t] = old_y, H[t] = old_h로 되돌린다(책의 Change(t, old_x, old_y, old_h) 호출에 대응)
		B[N+Y[t]-H[t]+1:N+Y[t]+H[t], N+X[t]-H[t]+1:N+X[t]+H[t]] -= delta[H[t]]
		X[t], Y[t], H[t] = old_x, old_y, old_h
		B[N+Y[t]-H[t]+1:N+Y[t]+H[t], N+X[t]-H[t]+1:N+X[t]+H[t]] += delta[H[t]]
	
	loops += 1

# 출력
print(Q)
for i in range(Q):
	print(X[i], Y[i], H[i])
print("score =", current_score, file = sys.stderr)
print("loops =", loops, file = sys.stderr)
