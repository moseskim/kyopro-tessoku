#include <iostream>
#include <algorithm>
using namespace std;

class SegmentTree {
public:
	int dat[300000], siz = 1;

	// 요소 dat의 초기화를 수행한다(최초에는 전부 0)
	void init(int N) {
		siz = 1;
		while (siz < N) siz *= 2;
		for (int i = 1; i < siz * 2; i++) dat[i] = 0;
	}

	// 쿼리 1에 대한 처리
	void update(int pos, int x) {
		pos = pos + siz - 1;
		dat[pos] = x;
		while (pos >= 2) {
			pos /= 2;
			dat[pos] = max(dat[pos * 2], dat[pos * 2 + 1]);
		}
	}

	// 쿼리 2에 대한 처리
	// u는 현재의 셀 번호, [a, b)는 셀에 대응하는 반개구간, [l, r)은 구할 반개구간
	int query(int l, int r, int a, int b, int u) {
		if (r <= a || b <= l) return -1000000000; // 전혀 포함되지 않는 경우
		if (l <= a && b <= r) return dat[u]; // 온전히 포함된 경우
		int m = (a + b) / 2;
		int AnswerL = query(l, r, a, m, u * 2);
		int AnswerR = query(l, r, m, b, u * 2 + 1);
		return max(AnswerL, AnswerR);
	}
};

int N, Q;
int Query[100009], pos[100009], x[100009], l[100009], r[100009];
SegmentTree Z;

int main() {
	// 입력
	cin >> N >> Q;
	for (int i = 1; i <= Q; i++) {
		cin >> Query[i];
		if (Query[i] == 1) cin >> pos[i] >> x[i];
		if (Query[i] == 2) cin >> l[i] >> r[i];
	}

	// クエリ処理
	Z.init(N);
	for (int i = 1; i <= Q; i++) {
		if (Query[i] == 1) {
			Z.update(pos[i], x[i]);
		}
		if (Query[i] == 2) {
			// 最初のセルに対応する半開区間は [1, siz + 1)
			int Answer = Z.query(l[i], r[i], 1, Z.siz + 1, 1);
			cout << Answer << endl;
		}
	}
	return 0;
}
