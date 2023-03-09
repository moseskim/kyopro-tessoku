#include <iostream>
using namespace std;

long long H, W;
char c[39][39];
long long dp[39][39];

int main() {
	// 입력
	cin >> H >> W;
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) cin >> c[i][j];
	}

	// 동적 계획 알고리즘
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			if (i == 1 && j == 1) {
				dp[i][j] = 1;
			}
			else {
				dp[i][j] = 0;
				if (i >= 2 && c[i - 1][j] == '.') dp[i][j] += dp[i - 1][j];
				if (j >= 2 && c[i][j - 1] == '.') dp[i][j] += dp[i][j - 1];
			}
		}
	}

	// 출력
	cout << dp[H][W] << endl;
	return 0;
}
