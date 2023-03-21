mod = 2147483647

# 문자열의 l~r번째를 앞에서부터 읽었을 때의 해시 값을 반환하는 함수
def GetHashLeft(l: int, r: int) -> int:
	val = H[r] - Power100[r - l + 1] * H[l - 1]
	return val % mod

# 문자열의 l~r번째를 뒤에서부터 읽었을 때의 해시 값을 반환하는 함수
def GetHashRight(l: int, r: int) -> int:
	l, r = N + 1 - r, N + 1 - l
	val = HRev[r] - Power100[r - l + 1] * HRev[l - 1]
	return val % mod

# 입력
N, Q = map(int, input().split())
S = input()
Query = [tuple(map(int, input().split())) for _ in range(Q)]

#S의 문자열을 수치로 변환
S = list(S)
for i in range(N):
	S[i] = ord(S[i]) - ord('a') + 1
SRev = S[::-1]

# 100의 n 제곱을 사전에 계산
Power100 = [1] * (N + 1)
for i in range(N):
	Power100[i + 1] = Power100[i] * 100 % mod

# S의 해시 값을 사전에 계산
H = [1] * (N + 1)
for i in range(N):
	H[i + 1] = (H[i] * 100 + S[i]) % mod

# SRev의 해시값을 사전에 계산
HRev = [1] * (N + 1)
for i in range(N):
	HRev[i + 1] = (HRev[i] * 100 + SRev[i]) % mod

# 쿼리 처리
for L, R in Query:
	v1 = GetHashLeft(L, R)
	v2 = GetHashRight(L, R)
	# 왼쪽부터 읽었을 때/오른쪽부터 읽었을 때의 해시 값이 일치하면 회문
	if v1 == v2:
		print("Yes")
	else:
		print("No")
