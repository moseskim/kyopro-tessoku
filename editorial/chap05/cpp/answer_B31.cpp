#include <iostream>
using namespace std;

int main() {
	long long N;
	cin >> N;

	long long A1 = (N /   3); // 3으로 나누어 떨어지는 것의 개수
	long long A2 = (N /   5); // 5으로 나누어 떨어지는 것의 개수
	long long A3 = (N /   7); // 5으로 나누어 떨어지는 것의 개수
	long long A4 = (N /  15); // 3, 5으로 나누어 떨어지는 것(=15의 배수)의 개수
	long long A5 = (N /  21); // 3, 7으로 나누어 떨어지는 것(=21의 배수)의 개수
	long long A6 = (N /  35); // 5, 7으로 나누어 떨어지는 것(=35의 배수)의 개수
	long long A7 = (N / 105); // 3, 5, 7으로 나누어 떨어지는 것(=105의 배수)의 개수
	cout << A1 + A2 + A3 - A4 - A5 - A6 + A7 << endl;
	return 0;
}
