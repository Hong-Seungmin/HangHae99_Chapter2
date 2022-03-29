package day_4;

import java.util.ArrayList;
import java.util.Arrays;

// https://leetcode.com/problems/merge-intervals/
public class Merge_intervals {
    public static void main(String[] args) {
        Merge_intervals test = new Merge_intervals();
        int[][] intervals = new int[][]{{2, 6}, {8, 10}, {1, 3}, {15, 18}, {1, 2}, {8, 9}, {8, 11}};
        System.out.println(Arrays.deepToString(test.merge(intervals)));
    }

    // 주어진 배열[][]는 [[start_idx, end_idx],...]로 구성되어있다.
    // 모든 시작지점과 종료지점을 병합하여, 중복이 없는 구간을 배열로 반환하라.
    // ex. [[1,5], [2,7], [10,13], [12,15]] ==> [[1,7], [10,15]]
    public int[][] merge(int[][] intervals) {
        // 주어진 배열을 오름차순 정렬, 우선순위는 [i1,i2] 기준으로 i1 -> i2 순으로 정렬
        Arrays.sort(intervals, ((o1, o2) -> {
            if (o1[0] < o2[0]) {
                return -1;
            } else if (o1[0] == o2[0]) {
                return o1[1] - o2[1];
            } else {
                return 1;
            }
        }));

//        for (int[] interval : intervals) {
//            System.out.println(interval[0] + " " + interval[1]);
//        }

        // 머지 진행
        // n번 항목의 end가 n+1번 항목의 start보다 작을때까지 n번 반복 후,
        // [n의 start, n+n의 end] 병합 후 result에 보관
        ArrayList<int[]> result = new ArrayList<>();
        for (int i = 0; i < intervals.length; i++) {
            int startMin = intervals[i][0];
            int endMax = intervals[i][1];
            int n = i;
            while (n < intervals.length - 1 && endMax >= intervals[n + 1][0]) {
                endMax = Math.max(endMax, intervals[n + 1][1]);
                n += 1;
            }
            // [startMin, endMax] 보관
            result.add(new int[]{startMin, endMax});

            i = n;
        }

//        result.forEach(num -> {
//            System.out.println(num[0] + " " + num[1]);
//        });
        return result.toArray(new int[result.size()][2]);
    }
//1 2
//1 3
//2 6
//8 9
//8 10
//8 11
//15 18
}
