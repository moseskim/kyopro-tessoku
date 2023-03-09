import java.util.*;
import java.io.*;

class Main {
	public static void main(String[] args) throws IOException {
		// 입력(고속의 입력을 위해, Scanner 대신 BufferedReader를 사용하고 있습니다)
		BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(buff.readLine());
		int N = Integer.parseInt(st.nextToken());
		int[] A = new int[N + 1];
		st = new StringTokenizer(buff.readLine());
		for (int i = 1; i <= N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}

		// 스택 변화 재현
		int[] answer = new int[N + 1];
		Stack<PairInt> level2 = new Stack<>();
		for (int i = 1; i <= N; i++) {
			if (i >= 2) {
				level2.push(new PairInt(i - 1, A[i - 1]));
				while (!level2.empty()) {
					int kabuka = level2.peek().second;
					if (kabuka <= A[i]) {
						level2.pop();
					}
					else {
						break;
					}
				}
			}
			// 기산일 특정
			if (!level2.empty()) {
				answer[i] = level2.peek().first;
			}
			else {
				answer[i] = -1;
			}
		}

		// 출력(고속 출력을 위해, System.out.println이 아닌 PrintWriter를 사용하고 있습니다)
		PrintWriter output = new PrintWriter(System.out);
		for (int i = 1; i <= N; i++) {
			if (i >= 2) {
				output.print(" ");
			}
			output.print(answer[i]);
		}
		output.println();
		output.flush();
	}
	
	// int 타입의 쌍의 클래스 PairInt
	static class PairInt {
		int first, second;
		public PairInt(int first, int second) {
			this.first = first;
			this.second = second;
		}
	}
}