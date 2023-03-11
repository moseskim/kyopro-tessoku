# 입력
N, K = map(int, input().split())
S = input()

# ON となっているものの個数を数える
numON = 0
for i in range(N):
	if S[i] == '1':
		numON += 1

# 답을 출력
if numON%2 == K%2:
	print("Yes")
else:
	print("No")
