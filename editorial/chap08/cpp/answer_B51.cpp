#include <iostream>
#include <stack>
using namespace std;
 
int main() {
	// 입력
	string S;
	cin >> S;
 
	// 왼쪽부터 순서대로 확인해 나간다
	// 문자열은 0번째 문자부터 시작하는 것에 주의
	stack<int> Stack;
	for (int i = 0; i < S.size(); i++) {
		if (S[i] == '(') {
			Stack.push(i + 1);
		}
		if (S[i] == ')') {
			cout << Stack.top() << " " << i + 1 << endl;
			Stack.pop();
		}
	}
	return 0;
}
