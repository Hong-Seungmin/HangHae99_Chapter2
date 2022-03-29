package day_4;

import java.io.*;
import java.util.*;

// https://www.acmicpc.net/problem/1707

// 입력된 그래프의 노드들을 탐색하여,
// 두 그룹으로 나누어진 이분 그래프가 생기는지 판별한다.
// * 정점은 1부터 V 까지이다.

// 이분 그래프의 특성을 찾아보면,
// 같은 or 홀수과 짝수의 깊이(level)의 정점들은 모두 같은 상태값을 가져야한다.
// 즉, 이동할때마다 처음 탐색한 정점이라면, 현재와 다른 상태값을 부여하고,
// 탐색했던 정점이라면, 상태값을 확인을 한다.
// 같은 값이라면 이분 그래프가 아니게 된다.
// 특성을 보면, 사이클이 없는 트리는 이분 그래프가 되는것 같다.
public class Boj_1707 {
    // 방문 여부 및 상태값 정의
    static final int NOT_VISITED = 0;
    //    static final int VISITED = -1; // *방문을 했다면, 홀짝 중 하나이다.
    static final int VISIT_ODD = 1;
    static final int VISIT_EVEN = 2;

    // 정점 정보 기록
    static int[] isVisited;
    static Hashtable<Integer, ArrayList<Integer>> hashtable;

    // 이분그래프인지 검증 기록
    static boolean isBipartiteGraph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter((new OutputStreamWriter(System.out)));

        // 테스트케이스 입력 및 테스트 진행
        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            // 정점 V, 간선 E의 개수
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());

            // 정점 방문 정보 ( 기본값 0 )
            isVisited = new int[V];

            // 이분그래프 판별 초기화
            isBipartiteGraph = true;

            hashtable = new Hashtable<>();

            // 각 정점들의 연결상태 보관
            for (int num = 0; num < E; num++) {
                st = new StringTokenizer(br.readLine());

                // 정점 정보
                int v1 = Integer.parseInt(st.nextToken());
                int v2 = Integer.parseInt(st.nextToken());

                v1 -= 1;
                v2 -= 1;

                // 양방향 등록
                if (hashtable.containsKey(v1)) {
                    hashtable.get(v1).add(v2);
                } else {
                    hashtable.put(v1, new ArrayList<>(Collections.singletonList(v2)));
                }
                if (hashtable.containsKey(v2)) {
                    hashtable.get(v2).add(v1);
                } else {
                    hashtable.put(v2, new ArrayList<>(Collections.singletonList(v1)));
                }

            }

            for (int v = 0; v < V; v++) {
                if (isBipartiteGraph) {
                    if (isVisited[v] == NOT_VISITED) {
                        // 최상단 정점은 홀수로 간주한다.
                        // 홀수로 부여하여 탐색을 시작한다.
                        //bfs(v, VISIT_ODD);
                        dfs(v, VISIT_ODD);
                    }
                } else {
                    break;
                }
            }
            bw.write((isBipartiteGraph ? "YES" : "NO") + "\n");

        }
        bw.flush();
        bw.close();
        br.close();
    }

    public static void dfs(int v, int status) {
        if (isVisited[v] == NOT_VISITED) {
            isVisited[v] = status;

            // 간선이 있는 정점의 자식들을 탐색한다.
            // *간선이 없는 정점은 hashtable에 들어있지 않다.
            if (hashtable.containsKey(v)) {
                for (int childV : hashtable.get(v)) {
                    if (isVisited[childV] == status) {
                        isBipartiteGraph = false;
                        return;
                    } else if (isVisited[childV] == NOT_VISITED) {
                        dfs(childV, status == VISIT_ODD ? VISIT_EVEN : VISIT_ODD);
                    }
                }
            }
        }
    }

    public static void bfs(int v, int status) {

    }
}

