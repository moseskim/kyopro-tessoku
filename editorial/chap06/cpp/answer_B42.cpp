#include <iostream>
#include <algorithm>
using namespace std;
 
long long N;
long long A[100009], B[100009];
 
// omote=1일 때 앞면의 총합이 양수,  ura=1일 때 뒷면의 총합이 양수
// omote=2일 때 앞면의 총합이 음수,  ura=2일 때 뒷면의 총합이 음수
long long solve(int omote, int ura) {
	long long sum = 0;
	for (int i = 1; i <= N; i++) {
		long long card1 = A[i]; if (omote == 2) card1 = -A[i];
		long long card2 = B[i]; if (ura == 2) card2 = -B[i];
		// 카드 i는 선택해야 하는가?
		if (card1 + card2 >= 0) {
			sum += (card1 + card2);
		}
	}
	return sum;
}
 
int main() {
	// 입력
	cin >> N;
	for (int i = 1; i <= N; i++) cin >> A[i] >> B[i];
 
	// 앞면의 총합의 음양과, 뒷면의 총합의 음양을 전탐색
	long long Answer1 = solve(1, 1);
	long long Answer2 = solve(1, 2);
	long long Answer3 = solve(2, 1);
	long long Answer4 = solve(2, 2);
 
	// 답을 출력
	cout << max({ Answer1,Answer2,Answer3,Answer4 }) << endl;
	return 0;
}
