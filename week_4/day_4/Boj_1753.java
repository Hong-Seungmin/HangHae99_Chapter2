package day_4;

import java.util.*;

// https://www.acmicpc.net/problem/1753
public class Boj_1753 {
    static List<List<Integer[]>> graph;
    static int[] distance;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();
        int e = sc.nextInt();
        int k = sc.nextInt();

        // graph의 항목을 정점의 개수 만큼 생성
        // 계산 편의상 0번 인덱스는 버린다.
        graph = new ArrayList<>();
        for (int i = 0; i < v + 1; i++) {
            graph.add(new ArrayList<>());
        }

        // 엣지의 개수만큼 리스트에 정보 입력
        // graph[src] = [dst, cost]
        for (int i = 0; i < e; i++) {
            graph.get(sc.nextInt()).add(new Integer[]{sc.nextInt(), sc.nextInt()});
        }

        // 최단거리 테이블을 가장 큰 수로 초기화
        // 계산 편의상 1개를 더 만들어 0번 인덱스는 버린다.
        distance = new int[v + 1];
        for (int i = 1; i < v + 1; i++) {
            distance[i] = Integer.MAX_VALUE;
        }

        // k번 노드를 기준으로 최단거리 계산 시작
        dijkstra(k);

        // 결과 출력
//        for (int vertex :
//                distance) {
//            System.out.println("vertex = " + vertex);
//        }
        for (int i = 1; i < v + 1; i++) {
            if (distance[i] == Integer.MAX_VALUE)
                System.out.println("INF");
            else System.out.println(distance[i]);
        }
    }

    public static void dijkstra(int start) {
        // 방문할 정점들을 우선순위 큐에 쌓는다.
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        // 시작 정점부터 방문목록에 추가한다.
        // 시작 정점은 비용이 없으므로 0 이다.
        pq.offer(new int[]{start, 0});
        distance[start] = 0;

        // 방문 목록이 없을때까지 반복
        while (!pq.isEmpty()) {
            // 방문할 정점의 정보를 추출한다.
            int[] dstVertex = pq.poll();
            int dst = dstVertex[0];
            int dstCost = dstVertex[1];

            // 최단경로 테이블보다 비용이 비싸면 방문할 이유가 없다. 패스
            if (dstCost > distance[dst]) {
                continue;
            }

            // if 문을 넘었다면 주석 코드 밑으로는 방문했다고 가정한다.

            // dst에서 방문할 수 있는 정점을 모두 탐색한다.
            // graph에서 인접 정점을 모두 본다.
            graph.get(dst).forEach((adj) -> {
                // 다음 방문지의 정보를 추출한다.
                int adj_dst = adj[0];
                // 다음 정점의 비용은 현재까지 비용 + 방문 비용이여야 한다. (누적)
                int adj_cost = adj[1] + dstCost;

                // 최단거리 테이블보다 인접 정점의 (누적)비용이 더 작다면,
                // 최단거리 테이블을 갱신하고, 다음 방문 목록에 추가한다.
                if (adj_cost < distance[adj_dst]) {
                    distance[adj_dst] = adj_cost;
                    pq.offer(new int[]{adj_dst, adj_cost});
                }
            });
        }
    }
}
