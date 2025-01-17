# 정수 x가 몇 번째에 존재하는지 반환하는 함수
def search(x, A):
	L = 0
	R = N-1
	while L <= R:
		M = (L + R) // 2
		if x < A[M]:
			R = M - 1
		if x == A[M]:
			return M
		if x > A[M]:
			L = M + 1
	return -1 # 정수 x가 존재하지 않는다(주: 이 문제의 제약에서, -1이 반환되는 일은 없다)


# 입력(배열 X가 0번째부터 시작하는 것에 주의)
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 바이너리 서치를 수행한다(배열이 0번재부터 시작하므로, 답에 1을 더한다)
Answer = search(X, A)
print(Answer + 1)
