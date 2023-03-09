import java.util.*;
import java.io.*;

class Main {
	public static void main(String[] args) throws IOException {
		// 입력（高速な入出力のため、Scanner の代わりに BufferedReader を使っています）
		BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(buff.readLine());
		int N = Integer.parseInt(st.nextToken());
		int[] A = new int[N + 1];
		st = new StringTokenizer(buff.readLine());
		for (int i = 2; i <= N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		// 隣接リストの作成
		ArrayList<Integer>[] G = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			G[i] = new ArrayList<Integer>();
		}
		for (int i = 2; i <= N; i++) {
			G[A[i]].add(i); // '상사→부하' 방향으로 에지를 추가
		}

		// 동적 계획 알고리즘(dp[x]는 사원 x의 부하의 수)
		int[] dp = new int[N + 1]; // Java에서는 new로 초기화한 배열의 요소는 0이 되는 것에 주의
		for (int i = N; i >= 1; i--) {
			for (int j = 0; j < G[i].size(); j++) {
				dp[i] += (dp[G[i].get(j)] + 1);
			}
		}
		
		// 答えを空白区切りで出力（高速な出力のため、System.out.println ではなく PrintWriter を使っています）
		PrintWriter output = new PrintWriter(System.out);
		for (int i = 1; i <= N; i++) {
			if (i >= 2) {
				output.print(" ");
			}
			output.print(dp[i]);
		}
		output.println();
		output.flush();
	}
}