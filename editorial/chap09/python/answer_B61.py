# 입력
N, M = map(int, input().split())

# 친구의 수를 구한다
friend = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    friend[A] += 1
    friend[B] += 1

mx = max(friend)
ans = friend.index(mx)
print(ans + 1)
