# Union-Find 트리
class unionfind:
	# n 노드의 Union-Find 트리를 작성
	# (여기에서는 노드 번호가 1-indexed가 되도록 구현하고 있지만, 0-indexed인 경우는 par, size의 크기는 n이어도 좋다)
	def __init__(self, n):
		self.n = n
		self.par = [ -1 ] * (n + 1) # 최초에는 부모가 없다
		self.size = [ 1 ] * (n + 1) # 최초에는 그룹의 노드 수가 1
	
	# 노드 x의 루트를 반환하는 함수
	def root(self, x):
		# 1개 앞(부모)가 없어질 때(즉, 루트에 도달할 때)까지, 1개 앞(부모)로 계속 진행한다
		while self.par[x] != -1:
			x = self.par[x]
		return x
	
	# 요소 u, v를 통합하는 함수
	def unite(self, u, v):
		rootu = self.root(u)
		rootv = self.root(v)
		if rootu != rootv:
			# u와 v가 다른 그룹일 때만 처리를 수행한다
			if self.size[rootu] < self.size[rootv]:
				self.par[rootu] = rootv
				self.size[rootv] += self.size[rootu]
			else:
				self.par[rootv] = rootu
				self.size[rootu] += self.size[rootv]
	
	# 요소 u와 v가 같은 그룹인지 반환하는 함수
	def same(self, u, v):
		return self.root(u) == self.root(v)

# 입력
N, Q = map(int, input().split())
queries = [ list(map(int, input().split())) for i in range(Q) ]

# 쿼리 처리
uf = unionfind(N)
for tp, u, v in queries:
	if tp == 1:
		uf.unite(u, v)
	if tp == 2:
		if uf.same(u, v):
			print("Yes")
		else:
			print("No")