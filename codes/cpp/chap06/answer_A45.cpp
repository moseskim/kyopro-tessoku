#include <iostream>
using namespace std;

int main() {
	// 입력
	int N; char C, A[200009];
	cin >> N >> C;
	for (int i = 1; i <= N; i++) cin >> A[i];

	// 점수 계산
	int score = 0;
	for (int i = 1; i <= N; i++) {
		if (A[i] == 'W') score += 0;
		if (A[i] == 'B') score += 1;
		if (A[i] == 'R') score += 2;
	}
	// 출력
	if (score % 3 == 0 && C == 'W') cout << "Yes" << endl;
	else if (score % 3 == 1 && C == 'B') cout << "Yes" << endl;
	else if (score % 3 == 2 && C == 'R') cout << "Yes" << endl;
	else cout << "No" << endl;
	return 0;
}
