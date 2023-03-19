# 입력
T = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
	L[i], R[i] = map(int, input().split())

# "前の時刻との差" に加算
B = [ 0 ] * (T + 1)
for i in range(N):
	B[L[i]] += 1
	B[R[i]] -= 1

# 누적합을 구한다
Answer = [ None ] * (T + 1)
Answer[0] = B[0]
for d in range(1, T+1):
	Answer[d] = Answer[d-1] + B[d]

# 출력
for d in range(T):
	print(Answer[d])
