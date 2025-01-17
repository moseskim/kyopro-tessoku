import java.util.*;

class Main {
	public static void main(String[] args) {
		// 입력
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] T = new int[N + 1];
		int[] D = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			T[i] = sc.nextInt();
			D[i] = sc.nextInt();
		}

		// D[i]의 오름차순으로 정렬한다
		PairInt[] problems = new PairInt[N];
		for (int i = 0; i < N; i++) {
			problems[i] = new PairInt(D[i + 1], T[i + 1]);
		}
		Arrays.sort(problems);
		for (int i = 0; i < N; i++) {
			T[i + 1] = problems[i].second;
			D[i + 1] = problems[i].first;
		}

		// 동적 계획 알고리즘：前準備
		int maxD = 0; // D[i] の最大値（書籍内のコードでは「1440」という定数を使っているが、ここでは代わりに MAX_D を使うことにする）
		for (int i = 1; i <= N; i++) {
			maxD = Math.max(maxD, D[i]);
		}
		int[][] dp = new int[N + 1][maxD + 1];
		for (int i = 0; i <= N; i++) {
			for (int j = 0; j <= maxD; j++) {
				dp[i][j] = -1000000000;
			}
		}

		// 동적 계획 알고리즘
		dp[0][0] = 0;
		for (int i = 1; i <= N; i++) {
			for (int j = 0; j <= maxD; j++) {
				if (j > D[i] || j < T[i]) {
					dp[i][j] = dp[i - 1][j];
				}
				else {
					dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - T[i]] + 1);
				}
			}
		}

		// 답을 구해서 출력
		int answer = 0;
		for (int i = 0; i <= maxD; i++) {
			answer = Math.max(answer, dp[N][i]);
		}
		System.out.println(answer);
	}
	
	// int 타입의 쌍의 클래스 PairInt
	static class PairInt implements Comparable<PairInt> {
		int first, second;
		public PairInt(int first, int second) {
			this.first = first;
			this.second = second;
		}
		@Override public int compareTo(PairInt p) {
			// PairInt 型同士の比較をする関数
			if (this.first < p.first || (this.first == p.first && this.second < p.second)) {
				return -1;
			}
			if (this.first > p.first || (this.first == p.first && this.second > p.second)) {
				return 1;
			}
			return 0;
		}
	}
}