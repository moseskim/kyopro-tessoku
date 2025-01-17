// 이 C++ 프로그램은 문제 C20의 해설 12번째 페이지 '한층 더 높이'까지를 구현한 것입니다.
// 이 프로그램을 제출하면 89,056,925점을 얻을 수 있습니다(제출에 따라 득점은 다소 달라집니다).

#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// Union-Find 트리
class UnionFind {
public:
	int par[401];
	int siz[401];

	// N 노드의 Union-Find를 작성
	void init(int N) {
		for (int i = 1; i <= N; i++) par[i] = -1; // 최초에는 부모가 없다
		for (int i = 1; i <= N; i++) siz[i] = 1; // 최초에는 그룹의 노드 수가 1
	}

	// 노드 x의 루트를 반환하는 함수
	int root(int x) {
		while (true) {
			if (par[x] == -1) break; // 1개 앞(부모)이 없으면, 여기가 루트
			x = par[x]; // 1 개 앞(부모)로 진행한다
		}
		return x;
	}

	// 요소 u와 v를 통합하는 함수
	void unite(int u, int v) {
		int RootU = root(u);
		int RootV = root(v);
		if (RootU == RootV) return; // u와 v가 같은 그룹일 때는 처리를 수행하지 않는다
		if (siz[RootU] < siz[RootV]) {
			par[RootU] = RootV;
			siz[RootV] = siz[RootU] + siz[RootV];
		}
		else {
			par[RootV] = RootU;
			siz[RootU] = siz[RootU] + siz[RootV];
		}
	}

	// 요소 u와 v가 같은 그룹인지 반환하는 함수
	bool same(int u, int v) {
		if (root(u) == root(v)) return true;
		return false;
	}
};

int N, K, L, A[401], B[401], C[51][51]; vector<int> G[401];
int answer[401];

// 깊이 우선 탐색(9.2절 참조)
bool visited[401];
void dfs(int pos) {
	visited[pos] = true;
	for (int i = 0; i < G[pos].size(); i++) {
		int nex = G[pos][i];
		if (answer[nex] == answer[pos] && visited[nex] == false) dfs(nex);
	}
}

double get_score() {
	// 답이 올바른지 깊이 우선 탐색(DFS)를 사용해서 확인
	for (int i = 1; i <= K; i++) visited[i] = false;
	for (int i = 1; i <= L; i++) {
		// 특별구 i에 속하는 노드 pos를 찾는다
		int pos = -1;
		for (int j = 1; j <= K; j++) {
			if (answer[j] == i) {
				pos = j;
			}
		}
		if (pos == -1) return 0.0; // 존재하지 않는 특별구가 있다!
		dfs(pos);
	}
	for (int i = 1; i <= K; i++) {
		if (visited[i] == false) return 0.0; // 연결되지 않은 특별구가 있다!
	}
	// 점수 계산
	int p[21], q[21];
	for (int i = 1; i <= L; i++) {
		p[i] = 0;
		q[i] = 0;
	}
	for (int i = 1; i <= K; i++) {
		p[answer[i]] += A[i];
		q[answer[i]] += B[i];
	}
	int pmin = *min_element(p + 1, p + L + 1);
	int pmax = *max_element(p + 1, p + L + 1);
	int qmin = *min_element(q + 1, q + L + 1);
	int qmax = *max_element(q + 1, q + L + 1);
	return min(double(pmin) / pmax, double(qmin) / qmax);
}

int main() {
	// 입력
	cin >> N >> K >> L;
	for (int i = 1; i <= K; i++) {
		cin >> A[i] >> B[i];
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> C[i][j];
		}
	}
	
	// 그래프 작성
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (i != N && C[i][j] != 0 && C[i + 1][j] != 0 && C[i][j] != C[i + 1][j]) {
				G[C[i][j]].push_back(C[i + 1][j]);
				G[C[i + 1][j]].push_back(C[i][j]);
			}
			if (j != N && C[i][j] != 0 && C[i][j + 1] != 0 && C[i][j] != C[i][j + 1]) {
				G[C[i][j]].push_back(C[i][j + 1]);
				G[C[i][j + 1]].push_back(C[i][j]);
			}
		}
	}
	// G[i]의 중복을 제거한다(erase/unique에 관해서는 p.103의 코드 참조)
	for (int i = 1; i <= K; i++) {
		sort(G[i].begin(), G[i].end());
		G[i].erase(unique(G[i].begin(), G[i].end()), G[i].end());
	}
	
	// 탐욕 알고리즘(합병을 K - L = 380번 반복한다)
	UnionFind uf;
	uf.init(K);
	for (int i = 1; i <= K - L; i++) {
		int min_size = 1000000000;
		int vertex1 = -1;
		int vertex2 = -1;
		for (int j = 1; j <= K; j++) {
			for (int k = 0; k < G[j].size(); k++) {
				int v = G[j][k];
				if (uf.same(j, v) == false) {
					// 노드 j의 지구와 노드 v의 지구를 합병하면...?
					int size1 = uf.siz[uf.root(j)];
					int size2 = uf.siz[uf.root(v)];
					if (min_size > size1 + size2) {
						min_size = size1 + size2;
						vertex1 = j;
						vertex2 = v;
					}
				}
			}
		}
		uf.unite(vertex1, vertex2);
	}
	
	// Union-Find 트리의 상태에서 답을 낸다
	vector<int> roots;
	for (int i = 1; i <= K; i++) {
		roots.push_back(uf.root(i));
	}
	sort(roots.begin(), roots.end());
	roots.erase(unique(roots.begin(), roots.end()), roots.end());
	for (int i = 1; i <= K; i++) {
		for (int j = 0; j < roots.size(); j++) {
			if (roots[j] == uf.root(i)) {
				answer[i] = j + 1;
			}
		}
	}
	
	// 등산 알고리즘(0.95초 루프를 돌린다)
	double TIME_LIMIT = 0.95;
	int ti = clock();
	double current_score = get_score();
	while (double(clock() - ti) / CLOCKS_PER_SEC < TIME_LIMIT) {
		int v = rand() % K + 1; // 1 이상 K 이하인 무작위 정수
		int x = rand() % L + 1; // 1 이상 L 이하인 무작위 정수
		int old_x = answer[v];
		// 우선 변경하고, 점수를 평가한다
		answer[v] = x;
		double new_score = get_score();
		// 점수 변화에 따라, 변경을 채용할 확률을 결정한다
		if (new_score != 0.0 && current_score <= new_score) current_score = new_score;
		else  answer[v] = old_x;
	}
	
	// 출력
	for (int i = 1; i <= K; i++) {
		cout << answer[i] << endl;
	}
	
	return 0;
}
