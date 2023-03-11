# 입력
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 配列の準備
Incorrect = [ 0 ] * (N + 1)

# 不正解数を求める
for i in range(M):
	Incorrect[A[i]] += 1

# 답을 출력
for i in range(1, N+1):
	print(M - Incorrect[i])
