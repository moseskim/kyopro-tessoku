#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 입력으로 주어진 변수
int N, K;
int L[100009], R[100009];

// 시각 i까지 몇 개 출석 가능한가 cntL[i]/시각 i 이후 몇 개 출석 가능한가 cntR[i]
int cntL[200009];
int cntR[200009];

int main() {
	// 입력
	cin >> N >> K;
	for (int i = 1; i <= N; i++) cin >> L[i] >> R[i];

	// 시각을 보정한다
	for (int i = 1; i <= N; i++) R[i] += K;
	
	// 왼쪽부터 구간 스케줄링(Part1: 정렬)
	vector<pair<int, int>> tmp1;
	for (int i = 1; i <= N; i++) tmp1.push_back(make_pair(R[i], L[i]));
	sort(tmp1.begin(), tmp1.end());

	// 왼쪽부터 구간 스케줄링(Part 2: 탐욕 알고리즘)
	int CurrentTime1 = 0; // 현재 시각
	int Num1 = 0; // 현재 출석한 회의의 개수
	for (int i = 0; i < tmp1.size(); i++) {
		if (CurrentTime1 <= tmp1[i].second) {
			CurrentTime1 = tmp1[i].first;
			Num1 += 1;
			cntL[CurrentTime1] = Num1;
		}
	}

	// 오른쪽부터 구간 스케줄링(Part1: 정렬)
	vector<pair<int, int>> tmp2;
	for (int i = 1; i <= N; i++) tmp2.push_back(make_pair(L[i], R[i]));
	sort(tmp2.begin(), tmp2.end());
	reverse(tmp2.begin(), tmp2.end());

	// 오른쪽부터 구간 스케줄링(Part2: 탐욕 알고리즘)
	int CurrentTime2 = 200000; // 현재 시각
	int Num2 = 0; // 현재 출석한 회의의 개수
	for (int i = 0; i < tmp2.size(); i++) {
		if (CurrentTime2 >= tmp2[i].second) {
			CurrentTime2 = tmp2[i].first;
			Num2 += 1;
			cntR[CurrentTime2] = Num2;
		}
	}

	// cntL, cntR을 구한다
	// 여기에서, 보정 후의 R[i]의 값은 절대로 200000을 넘지 않는 것에 주의
	for (int i = 1; i <= 200000; i++) cntL[i] = max(cntL[i], cntL[i - 1]);
	for (int i = 199999; i >= 0; i--) cntR[i] = max(cntR[i], cntR[i + 1]);

	// 답을 구한다
	for (int i = 1; i <= N; i++) {
		cout << cntL[L[i]] + cntR[R[i]] + 1 << endl;
	}
	return 0;
}
