# 입력
# A는 (종료 시작, 시작 시각)으로 되어 있는 것에 주의[종료 시각 기준 오름차순 정렬을 위해]
N = int(input())
A = []
for i in range(N):
	l, r = map(int, input().split())
	A.append([r, l])

# 정렬
A.sort()

# 종료 시각이 빠른 것부터 탐욕적으로 취해 간다(CurrentTime은 현재 시각)
CurrentTime = 0
Answer = 0
for i in range(N):
	if CurrentTime <= A[i][1]:
		CurrentTime = A[i][0]
		Answer += 1

# 출력
print(Answer)
