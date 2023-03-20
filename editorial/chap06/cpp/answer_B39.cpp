#include <iostream>
using namespace std;
 
int N, D;
int X[2009], Y[2009];
bool used[2009]; // used[i]는 업무 i 선택 여부
int Answer = 0;
 
int main() {
	// 입력
	cin >> N >> D;
	for (int i = 1; i <= N; i++) cin >> X[i] >> Y[i];
 
	// 답을 구한다
	for (int i = 1; i <= D; i++) {
		int maxValue = 0; // 급여의 최댓값
		int maxID = -1;   // 급여가 최대가 되는 업무의 번호
		for (int j = 1; j <= N; j++) {
			if (used[j] == true) continue;
			if (maxValue < Y[j] && X[j] <= i) {
				maxValue = Y[j];
				maxID = j;
			}
		}
 
		// 선택할 수 있는 업무가 있는 경우
		if (maxID != -1) {
			Answer += maxValue;
			used[maxID] = true;
		}
	}
 
	// 출력
	cout << Answer << endl;
	return 0;
}
