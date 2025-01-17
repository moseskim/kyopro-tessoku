#include <iostream>
using namespace std;

int H, W, N;
int A[100009], B[100009], C[100009], D[100009];
int X[1509][1509], Z[1509][1509];

int main() {
	// 입력
	cin >> H >> W >> N;
	for (int t = 1; t <= N; t++) cin >> A[t] >> B[t] >> C[t] >> D[t];

	// 각 날짜에 대해 더한다
	for (int t = 1; t <= N; t++) {
		X[A[t]][B[t]] += 1;
		X[A[t]][D[t] + 1] -= 1;
		X[C[t] + 1][B[t]] -= 1;
		X[C[t] + 1][D[t] + 1] += 1;
	}

  // 2차원 누적합을 구한다
	for (int i = 0; i <= H; i++) {
		for (int j = 0; j <= W; j++) Z[i][j] = 0;
	}
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) Z[i][j] = Z[i][j - 1] + X[i][j];
	}
	for (int j = 1; j <= W; j++) {
		for (int i = 1; i <= H; i++) Z[i][j] = Z[i - 1][j] + Z[i][j];
	}

	// 출력
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			if (j >= 2) cout << " ";
			cout << Z[i][j];
		}
		cout << endl;
	}
	return 0;
}
