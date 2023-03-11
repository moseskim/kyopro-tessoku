import java.util.*;
import java.io.*;

class Main {
	public static void main(String[] args) throws IOException {
		// 입력(고속의 입력을 위해, Scanner 대신 BufferedReader를 사용하고 있습니다)
		BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(buff.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] A = new int[M + 1];
		int[] B = new int[M + 1];
		for (int i = 1; i <= M; i++) {
			st = new StringTokenizer(buff.readLine());
			A[i] = Integer.parseInt(st.nextToken());
			B[i] = Integer.parseInt(st.nextToken());
		}
		
		// 인접 리스트 작성
		ArrayList<Integer>[] G = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			G[i] = new ArrayList<Integer>(); // G[i]는 노드 i에 인접하는 노드의 리스트
		}
		for (int i = 1; i <= M; i++) {
			G[A[i]].add(B[i]); // 노드 A[i]에 인접하는 노드로서 B[i]를 추가
			G[B[i]].add(A[i]); // 노드 B[i]에 인접하는 노드로서 A[i]를 추가
		}
		
		// 출력(G[i].size()는 노드 i에 인접하는 노드의 리스트의 크기 = 차수)
		//(빠른 출력을 위해 System.out.println가 아니라 PrintWriter를 사용한다)
		PrintWriter output = new PrintWriter(System.out);
		for (int i = 1; i <= N; i++) {
			output.print(i + ": {");
			for (int j = 0; j < G[i].size(); j++) {
				if (j >= 1) {
					output.print(", ");
				}
				output.print(G[i].get(j)); // G[i].get(j)는 노드 i에 인접하는 노드 중 j+1번째의 것
			}
			output.println("}");
		}
		output.flush();
	}
}