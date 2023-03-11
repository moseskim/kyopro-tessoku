# 최대 플로용 에지의 구조체
class maxflow_edge:
	def __init__(self, to, cap, rev):
		self.to = to
		self.cap = cap
		self.rev = rev

# 깊이 우선 탐색
def dfs(pos, goal, F, G, used):
	if pos == goal:
		return F # 골 도달: 플로를 흘려 보낸다!
	# 탐색한다
	used[pos] = True
	for e in G[pos]:
		# 용량이 1 이상이고, 아직 방문하지 않은 노드에만 진행한다
		if e.cap > 0 and not used[e.to]:
			flow = dfs(e.to, goal, min(F, e.cap), G, used)
			# 플로를 흘려 보내는 경우, 잔여 그래프의 용량을 flow 만큼 증감시킨다
			if flow >= 1:
				e.cap -= flow
				G[e.to][e.rev].cap += flow
				return flow
	# 모든 에지를 탐색해도 발견하지 못했다...
	return 0

# 노드 s에서 노드 t까지의 최대 플로의 총유량을 반환한다(노드 수 N, 에지 리스트 edges)
def maxflow(N, s, t, edges):
	# 초기 상태의 잔여 그래프를 구축
	# (여기는 책과 다소 그 구현이 달라, 8번째 행은 G[a]에 추가된 뒤이므로 len(G[a]) - 1로 되어 있음에 주의)
	G = [ list() for i in range(N + 1) ]
	for a, b, c in edges:
		G[a].append(maxflow_edge(b, c, len(G[b])))
		G[b].append(maxflow_edge(a, 0, len(G[a]) - 1))
	INF = 10 ** 10
	total_flow = 0
	while True:
		used = [ False ] * (N + 1)
		F = dfs(s, t, INF, G, used)
		if F > 0:
			total_flow += F
		else:
			break # 플로를 흘려 보낼 수 없다면 조작 종류
	return total_flow

# 입력
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 답을 구해서 출력
answer = maxflow(N, 1, N, edges)
print(answer)