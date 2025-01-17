# 입력
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# 점수의 최댓값이 x 이상인지 판정하는 함수
def check(x):
	cnt = 0         # 현 시점에서 몇 번 잘랐는가를 나타낸다
	last_kireme = 0 # 가장 마지막에 어디에서 잘랐는가를 나타낸다
	for i in range(N):
		if A[i] - last_kireme >= x and L - A[i] >= x:
			cnt += 1
			last_kireme = A[i]
	return cnt >= K

# 바이너리 서치(left: 현재의 상한/ right: 현재의 하한)
left, right = 1, 10 ** 9
while left < right:
	mid = (left + right + 1) // 2
	answer = check(mid)
	if answer == False:
		right = mid - 1 # 답이 전반 부분으로 좁혀진다
	else:
		left = mid      # 답이 후반 부분으로 좁혀진다

# 출력
print(left)