import bisect

# 입력
N = int(input())
A = list(map(int, input().split()))

# 배열 T 작성(중복을 제거한다)
T = list(set(A))
T.sort()

# 답을 구한다
B = [ None ] * N
for i in range(N):
	B[i] = bisect.bisect_left(T, A[i])
	B[i] += 1

# 답을 공백으로 구분해서 출력한다
Answer = [str(i) for i in B]
print(" ".join(Answer))
