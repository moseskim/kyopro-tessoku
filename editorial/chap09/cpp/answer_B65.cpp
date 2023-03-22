#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
// 입력된 변수, 답
int N, T, A[100009], B[100009];
int Answer[100009];
 
// 그래프/깊이 우선 탐색
vector<int> G[100009];
bool visited[100009];
 
// 깊이 우선 탐색을 수행하는 함수(pos는 현재 위치)
// 반환 값은 사원 pos의 계급
int dfs(int pos) {
	// 최초, 사원 pos의 계급은 0으로 설정한다
	visited[pos] = true;
	Answer[pos] = 0;
 
	// 탐색한다
	for (int i = 0; i < G[pos].size(); i++) {
		int nex = G[pos][i];
		if (visited[nex] == false) {
			int ret = dfs(nex);
			Answer[pos] = max(Answer[pos], ret + 1); // 계급을 업데이트 한다
		}
	}
 
	// 값을 반환한다
	return Answer[pos];
}
 
int main() {
	// 입력
	cin >> N >> T;
	for (int i = 1; i <= N - 1; i++) {
		cin >> A[i] >> B[i];
		G[A[i]].push_back(B[i]); // A[i]→B[i]의 뱡향에 에지를 추가
		G[B[i]].push_back(A[i]); // B[i]→A[i]의 방향에 에지를 추가
	}
 
	// 깊이 우선 탐색
	dfs(T);
 
	// 출력
	for (int i = 1; i <= N; i++) {
		if (i >= 2) cout << " ";
		cout << Answer[i];
	}
	cout << endl;
	return 0;
}
