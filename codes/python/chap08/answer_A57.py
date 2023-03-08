# 입력
N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [ list(map(int, input().split())) for i in range(Q) ]

# 전 계산(여기에서는 책과 달리 0-indexed로 구현했습니다)
LEVELS = 30
dp = [ [ None ] * N for i in range(LEVELS) ]
for i in range(0, N):
	dp[0][i] = A[i] - 1
for d in range(1, LEVELS):
	for i in range(0, N):
		dp[d][i] = dp[d - 1][dp[d - 1][i]]

# 쿼리 처리(여기에서는 책과 달리 0-indexed로 구현했습니다)
for X, Y in queries:
	current_place = X - 1
	for d in range(29, -1, -1):
		if ((Y >> d) & 1) == 1:
			current_place = dp[d][current_place]
	print(current_place + 1) # current_place는 0-indexed로 계산했으므로 1을 더해서 출력한다

# 주의 1: 책의 C++ 프로그램에서 'Y의 2^d의 자리를 꺼낸다'는 C++에서는 (Y / (1 << d)) % 2로 구현했습니다.
#        Python에서도 19번째 행은 (Y // (2 ** d)) % 2로 구현했으나, ((Y >> d) & 1)로 계산하면 상수배 측면에서 보다 빠릅니다.
# 주의 2: 이 프로그램의 평균적인 실행 시간은 2초에 아슬아슬하게 들어오므로, 제출 상황에 따라 TLE가 될 수 있습니다.
#        같은 프로그램을 PyPy3으로 제출하면 0,5로 정도의 실행 시간에 AC를 할 수 있습니다.
