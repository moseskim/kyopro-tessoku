# 입력
N = int(input())

# 10의 N 제곱을 구한다
Power10 = [ None ] * 17
for i in range(17):
	Power10[i] = 10 ** i

# R[i][j]의 값을 계산
R = [ [ None ] * 10 for i in range(17) ]
for i in range(16):
	# 아래부터 i번째 자리의 숫자를 구한다
	Digit = (N // Power10[i]) % 10;

	# R[i][j]의 값을 구한다
	for j in range(10):
		if j < Digit:
			R[i][j] = (N // Power10[i + 1] + 1) * Power10[i]
		if j == Digit:
			R[i][j] = (N // Power10[i + 1]) * Power10[i] + (N % Power10[i]) + 1
		if j > Digit:
			R[i][j] = (N // Power10[i + 1]) * Power10[i]

# 답을 구한다
Answer = 0
for i in range(16):
	for j in range(10):
		Answer += j * R[i][j]

# 출력
print(Answer)
