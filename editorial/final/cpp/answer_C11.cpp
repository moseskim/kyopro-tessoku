#include <iostream>
#include <algorithm>
using namespace std;

long long N, K;
double A[100009];

// 나눗셈의 값이 x일 때의 의석 수는?
long long check(double x) {
	long long sum = 0;
	for (int i = 1; i <= N; i++) sum += (long long)(A[i] / x);
	return sum;
}

int main() {
	// 입력
	cin >> N >> K;
	for (int i = 1; i <= N; i++) cin >> A[i];

	// 바이너리 서치
	double Left = 1, Right = 1000000000, Mid;
	double Border = 0; // 현재의 보더(합계 의석 수가 K 이상인 가장 큰 값)
	for (int i = 1; i <= 60; i++) {
		Mid = (Left + Right) / 2.0;

		// 나눗셈의 값은 Mid 보다 큰가?
		long long val = check(Mid);
		if (val >= K) {
			Left = Mid;
			Border = max(Border, Mid);
		}
		else {
			Right = Mid;
		}
	}

	// 출력
	for (int i = 1; i <= N; i++) {
		if (i >= 2) cout << " ";
		cout << (long long)(A[i] / Border);
	}
	cout << endl;
	return 0;
}
