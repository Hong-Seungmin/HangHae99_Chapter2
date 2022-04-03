package day_1;

// https://www.acmicpc.net/problem/9024

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 주어진 정수 배열 S에서 두 수를 더하여, 다른 정수 K와 가장 가까운 조합의 수를 출력한다.
public class Boj_9024 {

    // 메모리 초과 된다고한다.
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int tCount = Integer.parseInt(br.readLine());
//
//        for (int i = 0; i < tCount; i++) {
//            StringTokenizer st = new StringTokenizer(br.readLine());
//            int n = Integer.parseInt(st.nextToken());
//            int k = Integer.parseInt(st.nextToken());
//
//            st = new StringTokenizer(br.readLine());
//            int[] s = new int[n];
//            for (int j = 0; j < n; j++) {
//                s[j] = Integer.parseInt(st.nextToken());
//            }
//
//            Arrays.sort(s);
////            System.out.println("s = " + Arrays.toString(s) + " K = " + k);
//
//            int count = 0;
//            int gap = 200000000;
//            for (int j = 0; j < n; j++) {
//                int start = j + 1;
//                int end = n - 1;
//
//                while (start <= end) {
//                    int mid = (start + end) / 2;
//                    int sum = s[j] + s[mid];
//                    int abs_gap = Math.abs(sum - k);
//
//                    if (abs_gap < gap) {
//                        gap = abs_gap;
//                        count = 1;
//                    } else if (abs_gap == gap) {
//                        count += 1;
//                    }
//
//                    if (sum < k) {
//                        start = mid + 1;
//                    } else if (sum > k) {
//                        end = mid - 1;
//                    } else {
//                        break;
//                    }
//                }
//            }
//            System.out.println(count);
//        }
//      br.close()
//    }

    // 이것도 메모리 초과 뜬다..
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tCount = Integer.parseInt(br.readLine());

        for (int i = 0; i < tCount; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int[] s = new int[n];
            for (int j = 0; j < n; j++) {
                s[j] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(s);
//            System.out.println("s = " + Arrays.toString(s) + " K = " + k);

            int count = 0;
            int gap = 200000000;
            int left = 0;
            int right = n - 1;

            while (left < right) {
                int sum = s[left] + s[right];
                int abs_gap = Math.abs(sum - k);

                if (abs_gap < gap) {
                    gap = abs_gap;
                    count = 1;
                } else if (abs_gap == gap) {
                    count += 1;
                }

                if (sum < k) {
                    left = left + 1;
                } else if (sum > k) {
                    right = right - 1;
                } else {
                    left += 1;
                    right -=1;
                }
            }

            System.out.println(count);
        }
        br.close();
    }
}
