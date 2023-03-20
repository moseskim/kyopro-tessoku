# 입력
N, D = map(int, input().split())
X = [ None ] * N
Y = [ None ] * N
for i in range(N):
	X[i], Y[i] = map(int, input().split())

# 배열 준비
# used[i]는 업무 i 선택 여부
used = [ False ] * N

# 답을 구한다
Answer = 0
for i in range(1, D+1):
	maxValue = 0 # 급여의 최댓값
	maxID = -1   # 급여가 최대가 되는 업무의 번호
	for j in range(N):
		if used[j] == False and maxValue < Y[j] and X[j] <= i:
			maxValue = Y[j]
			maxID = j

	# 선택할 수 있는 업무가 있는 경우
	if maxID != -1:
		Answer += maxValue
		used[maxID] = True

# 출력
print(Answer)
