#include <iostream>
using namespace std;
 
int main() {
	// 입력
	int A, B;
	cin >> A >> B;
	
	// 答えを求める
	bool Answer = false;
	for (int i = A; i <= B; i++) {
		if (100 % i == 0) Answer = true;
	}
	
	// 출력
	if (Answer == true) cout << "Yes" << endl;
	else cout << "No" << endl;
	return 0;
}
