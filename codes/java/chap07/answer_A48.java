import java.util.*;

class Main {
	public static void main(String[] args) {
		// 입력
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Point2D[] points = new Point2D[N + 1];
		for (int i = 1; i <= N; i++) {
			points[i] = new Point2D(sc.nextInt(), sc.nextInt());
		}

		// 담금질 알고리즘
		int[] answer = simulatedAnnealing(N, points);

		// 답을 출력
		for (int i = 1; i <= N + 1; i++) {
			System.out.println(answer[i]);
		}
	}

	// 합계 거리를 계산하는 함수
	static double getScore(int N, Point2D[] points, int[] P) {
		double score = 0.0;
		for (int i = 1; i <= N; i++) {
			score += points[P[i]].dist(points[P[i + 1]]);
		}
		return score;
	}

	// 담금질 알고리즘을 이용해 답을 구하는 함수
	static int[] simulatedAnnealing(int N, Point2D[] points) {
		// 초기 해 생성
		int[] P = new int[N + 2];
		for (int i = 1; i <= N; i++) {
			P[i] = i;
		}
		P[N + 1] = 1;
		
		// 등산 알고리즘
		final int NUM_LOOPS = 200000;
		Random rnd = new Random();
		double currentScore = getScore(N, points, P);
		for (int t = 1; t <= NUM_LOOPS; t++) {
			// 무작위로 반전시킬 구간 [L, R]을 선택
			int L = 2 + rnd.nextInt(N - 1); // 2 이상 N 이하인 무작위 정수
			int R = 2 + rnd.nextInt(N - 1); // 2 이상 N 이하인 무작위 정수
			if (L > R) {
				// L과 R을 교환
				int z = L; L = R; R = z;
			}
			// P[L], P[L+1], ..., P[R]의 순서를 역전시킨다
			for (int i = L, j = R; i < j; i++, j--) {
				// P[i]과 P[j]을 교환
				int z = P[i]; P[i] = P[j]; P[j] = z;
			}
			double newScore = getScore(N, points, P);
			// 7.2절의 해답으로부터 변경한 유일한 부분(probability는 채용 확률)
			// (rnd.nextDouble()로 0 이사 1 미만의 무작위 실수를 생성)
			double T = 30.0 - 28.0 * t / NUM_LOOPS;
			double probability = Math.exp(Math.min((currentScore - newScore) / T, 0.0));
			if (rnd.nextDouble() < probability) {
				currentScore = newScore;
			}
			else {
				for (int i = L, j = R; i < j; i++, j--) {
					// P[i]와 P[j]를 교환
					int z = P[i]; P[i] = P[j]; P[j] = z;
				}
			}
		}

		return P;
	}

	// 二次元の点を扱うクラス Point2D
	static class Point2D {
		int x, y;
		public Point2D(int x, int y) {
			this.x = x;
			this.y = y;
		}
		// 2 点間の距離を求める関数
		double dist(Point2D p) {
			return Math.sqrt((x - p.x) * (x - p.x) + (y - p.y) * (y - p.y));
		}
	}
}