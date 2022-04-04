package day_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/1697
public class Boj_1697 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        br.close();

        boolean[] visited = new boolean[100001];
        Queue<Integer[]> queue = new LinkedList<>();
        queue.offer(new Integer[]{N, 0});
        while (!queue.isEmpty()) {
            Integer[] node = queue.poll();
            int n = node[0];
            int depth = node[1];

            if (n < 0 || n > 100000 || visited[n]) {
                continue;
            }

            visited[n] = true;

            if (n == K) {
                System.out.println(depth);
                break;
            }
            depth += 1;
            queue.offer(new Integer[]{n - 1, depth});
            queue.offer(new Integer[]{n + 1, depth});
            queue.offer(new Integer[]{n * 2, depth});
        }
    }
}
