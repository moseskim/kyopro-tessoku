import bisect

# 입력
N, W, L, R = map(int, input().split())
X = list(map(int, input().split()))

# 서쪽 가장자리를 발판 0, 동쪽 가장자리를 발판 N+1로 간주한다
X = [ 0 ] + X + [ W ]

# 동적 계획 알고리즘(책의 sum[i]은 이 코드의 dpsum[i]에 대응)
MOD = 10 ** 9 + 7 # = 1000000007
dp = [ 0 ] * (N + 2)
dpsum = [ 0 ] * (N + 2)
dp[0] = 1
dpsum[0] = 1
for i in range(1, N + 2):
	posl = bisect.bisect_left(X, X[i] - R)
	posr = bisect.bisect_left(X, X[i] - L + 1) - 1
	# dp[i] 값을 누적합으로 계산(C++과 달리, (음의 값) % MOD도 0 이상 MOD-1 이하가 되는 것에 주의)
	dp[i] = (dpsum[posr] if posr >= 0 else 0) - (dpsum[posl - 1] if posl >= 1 else 0)
	dp[i] %= MOD
	# 누적합 dpsum[i]의 값을 업데이트
	dpsum[i] = dpsum[i - 1] + dp[i]
	dpsum[i] %= MOD

# 출력
print(dp[N + 1])