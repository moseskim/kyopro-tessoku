#include <iostream>
using namespace std;
 
// 함수 f
double f(double x) {
	return x * x * x + x;
}
 
int main() {
	// 입력
	int N;
	cin >> N;
 
	// 바이너리 서치
	double Left = 0, Right = 100, Mid;
	for (int i = 0; i < 20; i++) {
		Mid = (Left + Right) / 2.0;
		double val = f(Mid);
 
		// 탐색 범위를 좁힌다
		if (val > 1.0 * N) Right = Mid; // 왼쪽 절반으로 좁힌다
		else Left = Mid; // 오른쪽 절반으로 좁힌다
	}
 
	// 출력
	printf("%.12lf\n", Mid);
	return 0;
}
