import java.util.*;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 입력
		int N = sc.nextInt();
		int[][] A = new int[N][2];
		for (int i = 1; i <= N; i++) {
			A[i - 1][0] = sc.nextInt();
			A[i - 1][1] = sc.nextInt();
		}

		// 배열 A를 종료 시각(A[x][1]) 기준 오름차순 정렬
		Arrays.sort(A, (a1, a2) -> Integer.compare(a1[1], a2[1]));

		// 종료 시각이 빠른 것부터 탐욕적으로 취해 간다(CurrentTime은 현재 시각)
		int CurrentTime = 0;
		int Answer = 0;
		for (int i = 1; i <= N; i++) {
			if (CurrentTime <= A[i - 1][0]) {
				CurrentTime = A[i - 1][1];
				Answer += 1;
			}
		}

		// 출력
		System.out.println(Answer);
	}
};
