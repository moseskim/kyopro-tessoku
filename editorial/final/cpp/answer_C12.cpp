#include <iostream>
#include <algorithm>
using namespace std;

int N, K;
int M, A[59], B[59];
int dp[19][309];

// l번째 페이지부터 r번째 페이지까지 사이에, 몇 개의 연결이 있는가?
int tsunagari(int l, int r) {
	int cnt = 0;
	for (int i = 1; i <= M; i++) {
		if (l <= A[i] && B[i] <= r) cnt++;
	}
	return cnt;
}

int main() {
	// 입력
	cin >> N >> M >> K;
	for (int i = 1; i <= M; i++) cin >> A[i] >> B[i];

	// 배열 dp 초기화
	for (int i = 0; i <= K; i++) {
		for (int j = 0; j <= N; j++) dp[i][j] = -1000000;
	}

	// 동적 계획 알고리즘（貰う遷移形式）
	dp[0][0] = 0;
	for (int i = 1; i <= K; i++) {
		for (int j = 1; j <= N; j++) {
			// k는 '앞 장이 어떤 페이지로 끝났는가?'
			for (int k = 0; k <= j - 1; k++) {
				dp[i][j] = max(dp[i][j], dp[i - 1][k] + tsunagari(k + 1, j));
			}
		}
	}

	// 출력
	cout << dp[K][N] << endl;
	return 0;
}
