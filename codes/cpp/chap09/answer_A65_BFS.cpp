// ###############################
// # 너비 우선 탐색을 사용한 구현
// ###############################

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int N, A[100009], dp[100009];
vector<int> G[100009];
int dist[100009]; // 거리

// 노드 1부터 각 노드까지의 거리를 구하는 함수
void GetDistance() {
	queue<int> Q;
	for (int i = 1; i <= N; i++) dist[i] = -1;
	Q.push(1);
	dist[1] = 0;

	// 큐를 사용한 계산
	while (!Q.empty()) {
		int pos = Q.front(); Q.pop();
		for (int i = 0; i < G[pos].size(); i++) {
			int to = G[pos][i];
			if (dist[to] == -1) {
				dist[to] = dist[pos] + 1;
				Q.push(to);
			}
		}
	}
}

int main() {
	// 입력
	cin >> N;
	for (int i = 2; i <= N; i++) {
		cin >> A[i];
		G[A[i]].push_back(i);
	}

	// 노드 1부터의 거리를 구한다
	GetDistance();

	// 거리의 내림차순으로 정렬한다
	vector<pair<int, int>> List;
	for (int i = 1; i <= N; i++) {
		List.push_back(make_pair(dist[i], i));
	}
	sort(List.begin(), List.end());
	reverse(List.begin(), List.end());

	// 동적 계획 알고리즘(dp[x]는 사원 x의 부하의 수)
	for (int i = 0; i < List.size(); i++) {
		int idx = List[i].second;
		dp[idx] = 0;
		for (int j = 0; j < G[idx].size(); j++) dp[idx] += (dp[G[idx][j]] + 1);
	}

	// 공백으로 구분해서 출력
	for (int i = 1; i <= N; i++) {
		if (i >= 2) cout << " ";
		cout << dp[i];
	}
	cout << endl;
	return 0;
}
