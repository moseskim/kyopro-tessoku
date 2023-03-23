#include <iostream>
#include <deque>
#include <string>
using namespace std;

// 입력으로 주어진 변수
int Q;
char QueryType[300009]; string X[300009];

// 덱
deque<string> Z1, Z2;

int main() {
	// 입력
	cin >> Q;
	for (int i = 1; i <= Q; i++) {
		cin >> QueryType[i];
		if (QueryType[i] == 'A' || QueryType[i] == 'B') cin >> X[i];
	}

	// 쿼리 처리
	for (int i = 1; i <= Q; i++) {
		// [A] 가장 마지막에 들어간다
		if (QueryType[i] == 'A') {
			Z2.push_back(X[i]);
		}
		// [B] 중앙에 들어간다
		if (QueryType[i] == 'B') {
			Z1.push_back(X[i]);
		}
		// [C] 선두가 빠진다
		if (QueryType[i] == 'C') {
			Z1.pop_front();
		}
		// [D] 선두를 답한다
		if (QueryType[i] == 'D') {
			cout << Z1.front() << endl;
		}

		// 미세 조정(전반의 덱 Z1이 너무 큰 경우)
		while ((int)Z1.size() - (int)Z2.size() >= 2) {
			string r = Z1.back();
			Z1.pop_back();
			Z2.push_front(r);
		}
		// 미세 조정(후반의 덱 Z2가 너무 큰 경우)
		while ((int)Z1.size() - (int)Z2.size() <= -1) {
			string r = Z2.front();
			Z2.pop_front();
			Z1.push_back(r);
		}
	}
	return 0;
}
