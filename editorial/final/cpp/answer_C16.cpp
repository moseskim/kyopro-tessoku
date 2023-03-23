#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
using namespace std;

// 입력 부분
int N, M, K;
int A[100009], B[100009], S[100009], T[100009];

// (시각, 출발/도착 여부, 노선 번호 또는 공항 번호)
// 출발 = 2/ 도착 =1/ 최초와 최후 = 0
// 여기에서, 출발 측의 번호가 큰 이유는 같은 시각일 때 도착을 더 빠르게 하기 위해서임
vector<tuple<int, int, int>> List;

// 노드 번호의 정보
int VertS[100009]; // 노선 i 도착
int VertT[100009]; // 노선 i 출발
vector<int> Airport[100009];

// 그래프 및 dp[i]
vector<pair<int, int>> G[400009];
int dp[400009];

int main() {
	// 입력
	cin >> N >> M >> K;
	for (int i = 1; i <= M; i++) {
		cin >> A[i] >> S[i] >> B[i] >> T[i];
		T[i] += K; // 도착 시각 보정
	}

	// 노드가 되는 (공항, 시각) 쌍을 '시각의 오름차순으로' 정렬
	for (int i = 1; i <= M; i++) List.push_back(make_tuple(S[i], 2, i));
	for (int i = 1; i <= M; i++) List.push_back(make_tuple(T[i], 1, i));
	for (int i = 1; i <= N; i++) List.push_back(make_tuple(-1, 0, i));
	for (int i = 1; i <= N; i++) List.push_back(make_tuple(2100000000, 0, i));
	sort(List.begin(), List.end());

	// 각 노선의 노드 번호를 구한다
	// 여기에서, 노드 번호는 시각의 오름차순으로 1, 2, ..., List.size()가 된다
	for (int i = 0; i < List.size(); i++) {
		if (get<1>(List[i]) == 2) VertS[get<2>(List[i])] = i + 1;
		if (get<1>(List[i]) == 1) VertT[get<2>(List[i])] = i + 1;
	}

	// 각 공항의 노드 번호를 구한다(공항에서의 대기에 대응하는 실선을 구할 때 사용한다)
	for (int i = 0; i < List.size(); i++) {
		if (get<1>(List[i]) == 0) Airport[get<2>(List[i])].push_back(i + 1);
		if (get<1>(List[i]) == 1) Airport[B[get<2>(List[i])]].push_back(i + 1);
		if (get<1>(List[i]) == 2) Airport[A[get<2>(List[i])]].push_back(i + 1);
	}

	// 그래프를 만든다(에지가 역방향으로 되어 있는 것에 주의!)
	for (int i = 1; i <= M; i++) {
		G[VertT[i]].push_back(make_pair(VertS[i], 1)); // 노선에 대응하는 에지(점선)
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 0; j < (int)Airport[i].size() - 1; j++) {
			int idx1 = Airport[i][j];
			int idx2 = Airport[i][j + 1];
			G[idx2].push_back(make_pair(idx1, 0)); // 공항에서의 대기에 대응하는 에지(실선)
		}
	}

	// 그래프에 시작점(노드 0)과 종점(노드 List.size()+1)을 추가
	for (int i = 1; i <= N; i++) {
		G[Airport[i][0]].push_back(make_pair(0, 0));
		G[List.size() + 1].push_back(make_pair(Airport[i][Airport[i].size() - 1], 0));
	}

	// 동적 계획 알고리즘에 따라 dp[i]의 값을 구한다
	// 노드 번호는 시각의 오름차순으로 되어 있으므로, dp[1]에서 순서대로 계산하면 된다
	dp[0] = 0;
	for (int i = 1; i <= List.size() + 1; i++) {
		for (int j = 0; j < G[i].size(); j++) {
			dp[i] = max(dp[i], dp[G[i][j].first] + G[i][j].second);
		}
	}

	// 출력
	cout << dp[List.size() + 1] << endl;
	return 0;
}
