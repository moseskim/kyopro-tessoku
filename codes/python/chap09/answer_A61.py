# 입력
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 인접 리스트 작성
G = [ list() for i in range(N + 1) ] # G[i]는 노드 i에 인접하는 노드의 리스트
for a, b in edges:
	G[a].append(b) # 노드 a에 인접하는 노드로 b를 추가
	G[b].append(a) # 노드 b에 인접하는 노드로 a를 추가

# 출력
for i in range(1, N + 1):
	output = ''
	output += str(i)
	output += ': {'
	output += ', '.join(map(str, G[i])) # 예를 들어, G[i] = {2, 7, 5}일 때, 여기에서 "2, 7, 5"라는 문자열이 output 뒤에 연결된다
	output += '}'
	print(output)