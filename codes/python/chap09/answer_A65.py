# 입력(A[2], ..., A[N]이 입력된 값이 되도록 한다)
N = int(input())
A = [ 0 ] * 2 + list(map(int, input().split()))

# 인접 리스트 작성
G = [ list() for i in range(N + 1) ]
for i in range(2, N + 1):
	G[A[i]].append(i) # 상사 → 부하의 방향으로 에지를 추가

# 동적 계획 알고리즘(dp[x]는 사원 x의 부하의 수)
dp = [ 0 ] * (N + 1)
for i in range(N, 0, -1):
	for j in G[i]:
		dp[i] += (dp[j] + 1)

# 답(dp[1], dp[2], ..., dp[N])을 공백으로 구분해서 출력
print(*dp[1:])