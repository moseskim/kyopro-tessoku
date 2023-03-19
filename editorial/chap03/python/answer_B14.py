import bisect
import sys

# '배열 A에 있는 카드에서 몇 장을 선탠했을 때의 합계'로서 생각할 수 있는 것을 열거
# 비트 전탐색을 사용한다
def Enumerate(A):
	SumList = []
	for i in range(2 ** len(A)):
		sum = 0 # 현재의 합곗값
		for j in range(len(A)):
			wari = (2 ** j)
			if (i // wari) % 2 == 1:
				sum += A[j]
		SumList.append(sum)
	return SumList

# 입력
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 카드를 반씩 나눈다
L1 = A[0:(N//2)]
L2 = A[(N//2):N]

# 각각에 대해 '얻을 수 있는 카드의 합계'를 전열거
Sum1 = Enumerate(L1)
Sum2 = Enumerate(L2)
Sum1.sort()
Sum2.sort()

# 바이너리 서치로 Sum1[i] + Sum2[j] = K가 되는 것이 존재하는지 찾는다
for i in range(len(Sum1)):
	pos = bisect.bisect_left(Sum2, K-Sum1[i])
	if pos<len(Sum2) and Sum2[pos]==K-Sum1[i]:
		print("Yes")
		sys.exit(0)

# 찾아내지 못한 경우
print("No")
