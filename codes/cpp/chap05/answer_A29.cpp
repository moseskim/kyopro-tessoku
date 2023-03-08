#include <iostream>
using namespace std;

// a의 b제곱을 m으로 나눈 나머지를 반환하는 함수
// 변수 a는 a^1 → a^2 → a^4 → a^8 → a^16 → ･･･으로 변화
long long Power(long long a, long long b, long long m) {
	long long p = a, Answer = 1;
	for (int i = 0; i < 30; i++) {
		int wari = (1 << i);
		if ((b / wari) % 2 == 1) {
			Answer = (Answer * p) % m; // 'a의 2^i 제곱'을 곱했을 떄
		}
		p = (p * p) % m;
	}
	return Answer;
}

int main() {
	long long a, b;
	cin >> a >> b;
	cout << Power(a, b, 1000000007) << endl;
	return 0;
}
