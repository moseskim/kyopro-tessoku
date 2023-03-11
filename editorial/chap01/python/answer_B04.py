# 입력
N = input()

# 答えを求める
Answer = 0
for i in range(len(N)):
	keta = 0
	kurai = (2 ** (len(N) - 1 - i))
	if N[i] == '1':
		keta = 1
	Answer += keta * kurai

# 출력
print(Answer)
