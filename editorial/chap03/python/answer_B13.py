# A[l]부터 A[r]까지의 합곗값
def sum(l, r, S):
	return S[r+1] - S[l]

# 입력
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 누적합을 구한다
S = [ 0 ] * (N + 1)
for i in range(1, N+1):
	S[i] = S[i-1] + A[i-1]

# 배열 준비(R은 0번째부터 시작하는 것에 주의)
R = [ None ] * N

# 자벌레 알고리즘
for i in range(N):
	if i == 0:
		R[i] = -1
	else:
		R[i] = R[i - 1]
	while R[i] < N-1 and sum(i,R[i]+1,S) <= K:
		R[i] += 1

# 답을 구한다
Answer = 0
for i in range(N):
	Answer += (R[i] - i + 1)
print(Answer)
