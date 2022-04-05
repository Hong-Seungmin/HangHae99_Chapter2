package day_4;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

// https://www.acmicpc.net/problem/4485
public class Boj_4485 {
    static int[][] distance;
    static int[][] board;

    static int[] dx = new int[]{0, 0, 1, -1};
    static int[] dy = new int[]{-1, 1, 0, 0};

    public static void main(String[] args) {
        int cnt = 1;
        Scanner sc = new Scanner(System.in);
        while (true) {
            int n = sc.nextInt();

            if (n == 0) break;

            board = new int[n][n];
            distance = new int[n][n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    board[i][j] = sc.nextInt();
                    distance[i][j] = Integer.MAX_VALUE;
                }
            }

            dijkstra(n - 1);

            System.out.println("Problem "+ cnt++ +": "+distance[n - 1][n - 1]);
        }
    }

    static void dijkstra(int endPoint) {
        // pq[v] = [x, y, cost]
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[2]));

        pq.offer(new int[]{0, 0, board[0][0]});
        distance[0][0] = board[0][0];

        while (!pq.isEmpty()) {
            int[] next = pq.poll();
            int x = next[0];
            int y = next[1];
            int cost = next[2];

            if (cost > distance[x][y]) continue;

            for (int i = 0; i < 4; i++) {
                int adjX = x+dx[i];
                int adjY = y+dy[i];

                if (isValid(adjX,adjY,endPoint)){
                    int adjCost = cost + board[adjX][adjY];

                    if (adjCost < distance[adjX][adjY]){
                        distance[adjX][adjY] = adjCost;
                        pq.offer(new int[] {adjX, adjY, adjCost});
                    }
                }
            }
        }
    }

    static boolean isValid(int x, int y, int endPoint) {
        return x >= 0 && y >= 0 && x <= endPoint && y <= endPoint;
    }
}
