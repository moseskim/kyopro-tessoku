def f(x):
	return x*x*x + x

N = int(input())

# 바이너리 서치
Left = 0.0
Right = 100.0
for i in range(20):
	Mid = (Left + Right) / 2
	val = f(Mid)

	# 탐색 범위를 좁힌다
	if val > N:
		Right = Mid # 왼쪽 절반으로 좁힌다
	else:
		Left = Mid # 오른쪽 절반으로 좁힌다

# 출력
print(Mid)
