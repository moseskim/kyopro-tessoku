# 입력
N = int(input())
problems = [ list(map(int, input().split())) for i in range(N) ] # 튜플 (T[i], D[i])가 N개 나열된 매열이 된다

# D[i]의 오름차순으로 정렬한다
problems.sort(key = lambda p: p[1])

# 동적 계획 알고리즘: 사전 준비
MAX_D = max(map(lambda p: p[1], problems)) # D[i]의 최댓값(책의 코드에서는 '1440'이라는 상수를 사용했지만, 여기에서는 대신 MAX_D를 사용한다)
dp = [ [ -(10 ** 10) ] * (MAX_D + 1) for i in range(N + 1) ]

# 동적 계획 알고리즘
dp[0][0] = 0
for i in range(N):
	t, d = problems[i] # 책의 T[i], D[i]에 대응
	for j in range(MAX_D + 1):
		if j > d or j < t:
			dp[i + 1][j] = dp[i][j]
		else:
			dp[i + 1][j] = max(dp[i][j], dp[i][j - t] + 1)

# 답을 출력
answer = max(dp[N])
print(answer)