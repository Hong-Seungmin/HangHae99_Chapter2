package day_3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

//https://leetcode.com/problems/network-delay-time/
public class Network_Delay_Time {
    // 방향성이 있는 그래프에서 k노드로부터 송신된 신호가 모든 노드가 수신하기 까지의 시간을 반환한다.
    // 모든 노드가 수신이 불가능하다면 -1을 반환한다.
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] times = new int[][]{{3, 5, 78}, {2, 1, 1}, {1, 3, 0}, {4, 3, 59}, {5, 3, 85}, {5, 2, 22}, {2, 4, 23}, {
                1, 4, 43}, {4, 5, 75}, {5, 1, 15}, {1, 5, 91}, {4, 1, 16}, {3, 2, 98}, {3, 4, 22}, {5, 4, 31}, {1, 2, 0}, {2, 5, 4}, {
                4, 2, 51}, {3, 1, 36}, {2, 3, 59}};


        System.out.println(sol.networkDelayTime(times, 5, 5));
    }
}

class Solution {
    int n;
    int[] distance;
    ArrayList<Node>[] sources;

    public int networkDelayTime(int[][] times, int n, int k) {
        sources = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            sources[i] = new ArrayList<>();
        }
        for (int[] v :
                times) {
            sources[v[0]].add(new Node(v[1], v[2]));
        }

        distance = new int[n + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[0] = 0;

        dijkstra(k);

        System.out.println(Arrays.toString(distance));
        int result = Arrays.stream(distance).max().getAsInt();
        return result == Integer.MAX_VALUE ? -1 : result;
    }

    private void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));
        distance[start] = 0;

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();

            if (curNode.cost > distance[curNode.dst]) {
                continue;
            }

            for (Node node :
                    sources[curNode.dst]) {
                int cost = curNode.cost + node.cost;
                if (distance[node.dst] > cost) {
                    distance[node.dst] = cost;
                    node.cost = cost;
                    pq.add(node);
                }
            }
        }
    }
}

class Node implements Comparable<Node> {
    int dst;
    int cost;

    public Node(int dst, int cost) {
        this.dst = dst;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}