#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
 
int N, M, A[100009], B[100009];
vector<int> G[100009];     // 그래프
bool visited[100009];      // 노드 1이 파란색인가, 흰색인가
vector<int> Path, Answer;  // 이동 경로의 궤적
 
void dfs(int pos) {
	// 골 지점에 도착했다!
	if (pos == N) {
		Answer = Path;
		return;
	}
 
	// 그 외의 경우
	visited[pos] = true;
	for (int i = 0; i < G[pos].size(); i++) {
		int nex = G[pos][i];
		if (visited[nex] == false) {
			Path.push(nex); // 노드 nex를 경로에 추가
			dfs(nex);
			Path.pop(); // 노드 nex를 경로에서 삭제
		}
	}
	return;
}
 
int main() {
	// 입력
	cin >> N >> M;
	for (int i = 1; i <= M; i++) {
		cin >> A[i] >> B[i];
		G[A[i]].push_back(B[i]);
		G[B[i]].push_back(A[i]);
	}
 
	// 깊이 우선 탐색
	for (int i = 1; i <= N; i++) visited[i] = false;
	Path.push(1); // 노드 1(시작 지점)을 경로에 추가
	dfs(1);
 
    	// 스택의 요소를 '아래부터 순서대로' 기록
    	vector<int> Output;
    	while (!Answer.empty()) {
        	Output.push_back(Answer.top());
        	Answer.pop();
    	}
    	reverse(Output.begin(),Output.end());

	// 답 출력
	for (int i = 0; i < Answer.size(); i++) {
		if (i >= 1) cout << " ";
		cout << Answer[i];
	}
	cout << endl;
	return 0;
}
