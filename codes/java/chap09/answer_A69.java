import java.util.*;

class Main {
	public static void main(String[] args) {
		// 입력
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String[] C = new String[N + 1];
		for (int i = 0; i < N; i++) {
			C[i + 1] = sc.next();
		}

		// 클래스를 구성한다
		MaximumFlow Z = new MaximumFlow(2 * N + 2);
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (C[i].charAt(j - 1) == '#') {
					Z.addEdge(i, j + N, 1);
				}
			}
		}
		for (int i = 1; i <= N; i++) {
			Z.addEdge(2 * N + 1, i, 1);     // 's → 파란색'의 에지
			Z.addEdge(i + N, 2 * N + 2, 1); // '빨간색 → t'의 에지
		}

		// 답을 구해서 출력
		int answer = Z.maxFlow(2 * N + 1, 2 * N + 2);
		System.out.println(answer);
	}
	
	// 최대 플로를 구하기 위한 에지 의 클래스 FlowEdge
	static class FlowEdge {
		int to, cap, rev;
		public FlowEdge(int to, int cap, int rev) {
			this.to = to;
			this.cap = cap;
			this.rev = rev;
		}
	}

	// 최대 플로를 수행하는 클래스 MaximumFlow
	static class MaximumFlow {
		int n;
		boolean[] used;
		ArrayList<FlowEdge>[] G;

		// 노드 수 N인 잔여 그래프를 준비
		public MaximumFlow(int n) {
			this.n = n;
			used = new boolean[n + 1];
			G = new ArrayList[n + 1];
			for (int i = 1; i <= n; i++) {
				G[i] = new ArrayList<FlowEdge>();
			}
		}

		// 노드 a에서 b로 향하는, 상한 c 리터/초의 에지를 추가
		void addEdge(int a, int b, int c) {
			int currentGa = G[a].size();
			int currentGb = G[b].size();
			G[a].add(new FlowEdge(b, c, currentGb));
			G[b].add(new FlowEdge(a, 0, currentGa));
		}

		// 깊이 우선 탐색(F는 시작부터 pos에 도달하는 과정에서의 "잔여 그래프의 에지의 용량"의 최솟값)
		// 반환값은 흘려 보낸 플로의 양(흘려 보내지 못한 경우는 0을 반환한다)
		int dfs(int pos, int goal, int F) {
			// 골에 도착: 플로를 흘려 보낼 수 있다! 
			if (pos == goal) {
				return F;
			}
			used[pos] = true;
			// 탐색한다
			for (int i = 0; i < G[pos].size(); i++) {
				FlowEdge e = G[pos].get(i);
				// 용량 0인 에지는 사용할 수 없다
				if (e.cap == 0) {
					continue;
				}
				// 이미 방문한 노드에 가도 의미가 없다
				if (used[e.to]) {
					continue;
				}
				// 목적지까지의 패스를 찾는다
				int flow = dfs(e.to, goal, Math.min(F, e.cap));
				// 플로를 흘려 보낼 수 있는 경우, 잔여 그래프의 용량을 flow만큼만 증가시킨다
				if (flow >= 1) {
					G[pos].get(i).cap -= flow;
					G[e.to].get(e.rev).cap += flow;
					return flow;
				}
			}
			// 모든 에지를 탐색해도 찾아내지 못했다...
			return 0;
		}

		// 노드 s에서 노드 t까지의 최대 플로의 총유량을 반환한다
		int maxFlow(int s, int t) {
			final int INF = 1000000000;
			int totalFlow = 0;
			while (true) {
				Arrays.fill(used, false);
				int f = dfs(s, t, INF);
				// 플로를 흘려 보낼 수 없다면 조작 종료
				if (f == 0) {
					break;
				}
				totalFlow += f;
			}
			return totalFlow;
		}
	}
}