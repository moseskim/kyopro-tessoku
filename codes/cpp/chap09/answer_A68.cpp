#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Edge {
	int to, cap, rev;
};

class MaximumFlow {
public:
	int size_ = 0;
	bool used[409];
	vector<Edge> G[409];

	// 노드 수 N인 잔여 그래프를 준비
	void init(int N) {
		size_ = N;
		for (int i = 0; i <= size_; i++) G[i].clear();
	}

	// 노드 a에서 b로 향하는, 상한 c 리터/초의 에지를 추가
	void add_edge(int a, int b, int c) {
		int Current_Ga = G[a].size(); // 현 시점에서의 G[a]의 요소 수
		int Current_Gb = G[b].size(); // 현 시점에서의 G[b]의 요소 수
		G[a].push_back(Edge{ b, c, Current_Gb });
		G[b].push_back(Edge{ a, 0, Current_Ga });
	}

	// 깊이 우선 탐색(F는 시작부터 pos에 도달하는 과정에서의 "잔여 그래프의 에지의 용량"의 최솟값)
	// 반환값은 흘려 보낸 플로의 양(흘려 보내지 못한 경우는 0을 반환한다)
	int dfs(int pos, int goal, int F) {
		// 골에 도착: 플로를 흘려 보낼 수 있다! 
		if (pos == goal) return F;
		used[pos] = true;

		// 탐색한다
		for (int i = 0; i < G[pos].size(); i++) {
			// 용량 0인 에지는 사용할 수 없다
			if (G[pos][i].cap == 0) continue;

			// 이미 방문한 노드에 가도 의미가 없다
			if (used[G[pos][i].to] == true) continue;

			// 목적지까지의 패스를 찾는다
			int flow = dfs(G[pos][i].to, goal, min(F, G[pos][i].cap));

			// 플로를 흘려 보낼 수 있는 경우, 잔여 그래프의 용량을 flow만큼만 증가시킨다
			if (flow >= 1) {
				G[pos][i].cap -= flow;
				G[G[pos][i].to][G[pos][i].rev].cap += flow;
				return flow;
			}
		}

		// 모든 에지를 탐색해도 찾지 못했다･･･
		return 0;
	}

	// 노드 s에서 노드 t까지의 최대 플로의 총유량을 반환한다
	int max_flow(int s, int t) {
		int Total_Flow = 0;
		while (true) {
			for (int i = 0; i <= size_; i++) used[i] = false;
			int F = dfs(s, t, 1000000000);

			// 플로를 흘려 보낼 수 없다면 조작 종료
			if (F == 0) break;
			Total_Flow += F;
		}
		return Total_Flow;
	}
};

int N, M;
int A[409], B[409], C[409];
MaximumFlow Z;

int main() {
	// 입력
	cin >> N >> M;
	for (int i = 1; i <= M; i++) cin >> A[i] >> B[i] >> C[i];

	// 에지를 추가
	Z.init(N);
	for (int i = 1; i <= M; i++) {
		Z.add_edge(A[i], B[i], C[i]);
	}

	// 답을 출력
	cout << Z.max_flow(1, N) << endl;
	return 0;
}
