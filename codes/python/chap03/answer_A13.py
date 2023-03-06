# 입력(A는 0번째부터 시작하는 것에 주의)
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 배열 준비(R은 0번째부터 시작하는 것에 주의)
R = [ None ] * N

# 자벌레 법
for i in range(0, N-1):
	# 시작 지점을 결정한다
	if i == 0:
		R[i] = 0
	else:
		R[i] = R[i - 1]

	# 한계까지 증가시킨다
	while R[i] < N-1 and A[R[i]+1]-A[i] <= K:
		R[i] += 1

# 출력
Answer = 0
for i in range(0, N-1):
	Answer += (R[i] - i)
print(Answer)
