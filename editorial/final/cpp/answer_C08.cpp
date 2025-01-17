#include <iostream>
#include <string>
#include <vector>
using namespace std;

int N;
string S[1009]; int T[1009];

// 당첨 번호가 A2일 때, A1은 몇 등인지를 반환한다
int Hantei(string A1, string A2) {
	int Diff = 0;
	for (int i = 0; i < 4; i++) {
		if (A1[i] != A2[i]) Diff += 1;
	}
	if (Diff == 0) return 1; // 전부 같을 때 1등
	if (Diff == 1) return 2; // 자리가 1자리만 다르면 2등
	return 3;
}

int main() {
	// 입력
	cin >> N;
	for (int i = 1; i <= N; i++) cin >> S[i] >> T[i];

	// 전탐색
	vector<string> Answer;
	for (int num = 0; num <= 9999; num++) {
		// 정수 num을 4자리의 문자열로 치환한다
		string ID = to_string(num);
		while (ID.size() < 4) ID = "0" + ID;

		// 모든 정보가 올바른가를 확인
		bool flag = true;
		for (int i = 1; i <= N; i++) {
			if (Hantei(S[i], ID) != T[i]) flag = false;
		}

		// 만약 모든 정보가 올바르다면
		if (flag == true) {
			Answer.push_back(ID);
		}
	}

	// 출력
	if (Answer.size() != 1) {
		cout << "Can't Solve" << endl;
	}
	else {
		cout << Answer[0] << endl;
	}
	return 0;
}
