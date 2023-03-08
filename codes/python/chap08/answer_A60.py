from collections import deque

# 입력
N = int(input())
A = list(map(int, input().split()))

# 스택 변화 재현
# (스택에는 (날짜, 주가) 튜플을 기록한다)
answer = [ None ] * N
level2 = deque()
for i in range(N):
	if i >= 1:
		level2.append((i, A[i - 1]))
		while len(level2) >= 1:
			kabuka = level2[-1][1] # 주가는 튜플의 2번째 요소
			if kabuka <= A[i]:
				level2.pop()
			else:
				break
	if len(level2) >= 1:
		answer[i] = level2[-1][0] # 날짜는 튜플의 1번째 요소
	else:
		answer[i] = -1

# answer를 공백으로 구분해서 출력
print(*answer)