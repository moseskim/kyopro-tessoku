#include <iostream>
#include <vector>
#include <queue>
using namespace std;

long long N, D;
long long X[200009], Y[200009];
vector<long long> G[375]; // G[i]는 i번째 날부터 시작하는 업무의 급여 리스트
long long Answer = 0;

int main() {
	// 입력
	cin >> N >> D;
	for (int i = 1; i <= N; i++) {
		cin >> X[i] >> Y[i];
		G[X[i]].push_back(Y[i]);
	}

	// 답을 구한다
	priority_queue<long long> Q;
	for (int i = 1; i <= D; i++) {
		// i번째 날부터 시작하는 업무를 큐에 추가
		for (int j : G[i]) Q.push(j);

		// 할 업무를 선택하고, 그 업무를 큐에서 삭제한다
		if (!Q.empty()) {
			Answer += Q.top();
			Q.pop();
		}
	}

	// 출력
	cout << Answer << endl;
	return 0;
}
