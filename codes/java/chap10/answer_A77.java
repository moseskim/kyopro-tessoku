import java.util.*;

class Main {
	public static void main(String[] args) {
		// 입력
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int L = sc.nextInt();
		int K = sc.nextInt();
		int[] A = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			A[i] = sc.nextInt();
		}

		// 二分探索（left: 現在の下限 ／ right: 現在の上限）
		int left = 1, right = 1000000000;
		while (left < right) {
			int mid = (left + right + 1) / 2;
			boolean answer = check(N, L, K, A, mid);
			if (answer == false) {
				right = mid - 1; // 답이 전반 부분으로 좁혀진다
			}
			else {
				left = mid;      // 답이 후반 부분으로 좁혀진다
			}
		}

		// 출력
		System.out.println(left);
	}

	// スコアの最大値が x 以上かを判定する関数
	static boolean check(int N, int L, int K, int[] A, int x) {
		int count = 0;      // 現時点で何回切ったかを表す
		int lastKireme = 0; // 가장 마지막에 어디에서 잘랐는가를 나타낸다
		for (int i = 1; i <= N; i++) {
			if (A[i] - lastKireme >= x && L - A[i] >= x) {
				count += 1;
				lastKireme = A[i];
			}
		}
		return (count >= K);
	}
}