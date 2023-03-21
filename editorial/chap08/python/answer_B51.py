# 입력
S = input()

# 왼쪽부터 순서대로 확인해 나간다
# 문자열은 0번째 문자부터 시작하는 것에 주의
Stack = []
for i in range(len(S)):
	if S[i] == '(':
		Stack.append(i + 1)
	if S[i] == ')':
		print(Stack.pop(), i + 1)
