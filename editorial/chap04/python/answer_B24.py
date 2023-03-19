import bisect

# 배열 A의 최장 증가 부분열(LIS)의 길이를 계산한다
# 배열 dp를 사용하지 않는 구현 방법을 이용한다
def Get_LISvalue(A):
	LEN = 0
	L = []
	for i in range(N):
		pos = bisect.bisect_left(L, A[i])
		if pos == LEN:
			L.append(A[i])
			LEN += 1
		else:
			L[pos] = A[i]
	return LEN

# 입력
N = int(input())
X = [ None ] * N
Y = [ None ] * N
for i in range(N):
	X[i], Y[i] = map(int, input().split())

# 정렬
tmp = []
for i in range(N):
	tmp.append([X[i], -Y[i]])
tmp.sort()

# LIS를 구해야할 배열은?
A = []
for i in range(N):
	A.append(-tmp[i][1])

# 출력
print(Get_LISvalue(A))
