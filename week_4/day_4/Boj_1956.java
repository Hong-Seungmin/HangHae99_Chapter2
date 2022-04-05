package day_4;

import java.util.*;

// https://www.acmicpc.net/problem/1956
public class Boj_1956 {
    static List<List<Integer[]>> graph;
    static int[] dist;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int v = sc.nextInt();
        int e = sc.nextInt();

        graph = new ArrayList<>();
        dist = new int[v + 1];
        for (int i = 0; i < v + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < e; i++) {
            graph.get(sc.nextInt()).add(new Integer[]{sc.nextInt(), sc.nextInt()});
        }

        int result = Integer.MAX_VALUE;
        for (int i = 1; i < v + 1; i++) {
            for (int j = 0; j < v + 1; j++) {
                dist[j] = Integer.MAX_VALUE;
            }
            dijkstra(i);
            result = Math.min(dist[i], result);
//            result = Math.min(dijkstra(i), result);
        }

        System.out.println(result == Integer.MAX_VALUE ? -1 : result);
    }

    static int dijkstra(int start) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        pq.offer(new int[]{start, 0});
//        dist[start] = 0;

        while (!pq.isEmpty()) {
            int[] next = pq.poll();
            int dstV = next[0];
            int dstC = next[1];

            if (dstC > dist[dstV]) {
                continue;
            }

            for (Integer[] i :
                    graph.get(dstV)) {
                int cost = i[1] + dstC;
//                if (i[0] == start) {
//                    return cost;
//                }
                if (dist[i[0]] > cost) {
                    dist[i[0]] = cost;
                    pq.offer(new int[] {i[0], cost});
                }
            }
        }

        return Integer.MAX_VALUE;
    }
}
