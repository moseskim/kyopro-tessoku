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

		// 등산 알고리즘
		int[] answer = hillClimbing(N, points);

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

	// 등산 알고리즘을 이용해 답을 구하는 함수
	static int[] hillClimbing(int N, Point2D[] points) {
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
			// 무작위로 반전시킬 구간 [L, R]을 선택한다
			int L = 2 + rnd.nextInt(N - 1); // 2 이상 N 이하인 무작위 정수
			int R = 2 + rnd.nextInt(N - 1); // 2 이상 N 이하인 무작위 정수
			if (L > R) {
				// L과 R을 비교
				int z = L; L = R; R = z;
			}
			// P[L], P[L+1], ..., P[R]의 순서를 역전시킨다
			for (int i = L, j = R; i < j; i++, j--) {
				// P[i]과 P[j]를 교환
				int z = P[i]; P[i] = P[j]; P[j] = z;
			}
			double newScore = getScore(N, points, P);
			// 개선되면 점수를 업데이트, 악화되면 원래대로 되돌린다
			if (currentScore >= newScore) {
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

	// 2차원의 점을 다루는 클래스 Point2D
	static class Point2D {
		int x, y;
		public Point2D(int x, int y) {
			this.x = x;
			this.y = y;
		}
		// 2덤 사이의 거리를 구하는 함수
		double dist(Point2D p) {
			return Math.sqrt((x - p.x) * (x - p.x) + (y - p.y) * (y - p.y));
		}
	}
}