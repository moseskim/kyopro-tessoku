# 입력
N = int(input())
S = input()

# 배열 준비
ret1 = [ None ] * N
ret2 = [ None ] * N

# 답을 구한다(전반)
streak1 = 1 # streak1은 '몇 개의 A가 연속되어 있는가' + `
ret1[0] = 1
for i in range(N-1):
	if S[i] == 'A':
		streak1 += 1
	if S[i] == 'B':
		streak1 = 1
	ret1[i+1] = streak1

# 답을 구한다(후반)
streak2 = 1
ret2[N-1] = 1
for i in reversed(range(N-1)):
	if S[i] == 'A':
		streak2 = 1
	if S[i] == 'B':
		streak2 += 1
	ret2[i] = streak2

# 출력
Answer = 0
for i in range(N):
	Answer += max(ret1[i], ret2[i])
print(Answer)
