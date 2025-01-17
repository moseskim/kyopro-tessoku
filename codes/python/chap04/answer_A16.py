# 입력(A, B가 0번째부터 시작하는 것에 주의)
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 동적 계획 알고리즘
dp = [ None ] * (N+1)
dp[1] = 0
dp[2] = A[0]
for i in range(3, N+1):
	dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

# 출력
print(dp[N])
