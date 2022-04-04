package day_3;

import java.util.*;

// https://leetcode.com/problems/cheapest-flights-within-k-stops/
public class Cheapest_Flights_Within_K_Stops {
    public static void main(String[] args) {
        Solution1 sol = new Solution1();

        int[][] flights = {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}};
        int cheapestPrice = sol.findCheapestPrice(4, flights, 0, 3, 1);
        System.out.println("cheapestPrice = " + cheapestPrice);
    }
}

class Solution1 {
    private final List<List<int[]>> graph = new ArrayList<>();

    private void init(int n, int[][] flights) {
        for (int i = 0; i < n; i++)
            graph.add(new ArrayList<>());
        for (int[] flight : flights)
            graph.get(flight[0]).add(new int[]{flight[1], flight[2]});
    }

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        init(n, flights);
        Queue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        queue.offer(new int[]{src, 0, 0});
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int city = current[0], distance = current[1], cost = current[2];
            if (city == dst)
                return cost;
            if (distance <= K) {
                for (int[] child : graph.get(city)) {
                    queue.offer(new int[]{child[0], distance + 1, cost + child[1]});
                }
            }
        }
        return -1;
    }
}