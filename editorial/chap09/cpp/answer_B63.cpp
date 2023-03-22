#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 입력
int H, W;
int sx, sy, start; // 시작 좌표(sx, xy)와 노드 번호 sx * H + sy
int gx, gy, goal;  // 골 좌표 (gx, gy)와 노드 번호 gx * W + gy
char c[59][59];

// 그래프/최단 경로
int dist[2509];
vector<int> G[2509];

int main() {
	// 입력
	cin >> H >> W;
	cin >> sx >> sy; start = sx * W + sy;
	cin >> gx >> gy; goal = gx * W + gy;
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) cin >> c[i][j];
	}

	// 가로 방향 에지 [(i, j) - (i, j+1)]를 그래프에 추가
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W - 1; j++) {
			int idx1 = i * W + j; // 노드 (i, j)의 노드 번호
			int idx2 = i * W + (j + 1); // 노드 (i, j+1)의 노드 번호
			if (c[i][j] == '.' && c[i][j + 1] == '.') {
				G[idx1].push_back(idx2);
				G[idx2].push_back(idx1);
			}
		}
	}

	// 세로 방향 에지 [(i, j) - (i+1, j)]를 그래프에 추가
	for (int i = 1; i <= H - 1; i++) {
		for (int j = 1; j <= W; j++) {
			int idx1 = i * W + j; // 노드 (i, j)의 노드 번호
			int idx2 = (i + 1) * W + j; // 노드 (i+j, j)의 노드 번호
			if (c[i][j] == '.' && c[i + 1][j] == '.') {
				G[idx1].push_back(idx2);
				G[idx2].push_back(idx1);
			}
		}
	}

	// 너비 우선 탐색 초기화
	for (int i = 1; i <= H * W; i++) dist[i] = -1;
	queue<int> Q;
	Q.push(start); dist[start] = 0;

	// 너비 우선 탐색
	while (!Q.empty()) {
		int pos = Q.front();
		Q.pop();
		for (int i = 0; i < G[pos].size(); i++) {
			int to = G[pos][i];
			if (dist[to] == -1) {
				dist[to] = dist[pos] + 1;
				Q.push(to);
			}
		}
	}

	// 답을 출력
	cout << dist[goal] << endl;
	return 0;
}
