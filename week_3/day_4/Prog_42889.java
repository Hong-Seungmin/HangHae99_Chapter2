package day_4;
// https://programmers.co.kr/learn/courses/30/lessons/42889?language=java

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Prog_42889 {
    public static void main(String[] args) {
        Prog_42889 sol = new Prog_42889();
        int[] answer = sol.solution(5, new int[]{2, 1, 2, 6, 2, 4, 3, 3});

        for (int i : answer) {
            System.out.println("i = " + i);
        }
    }

    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];

        Integer[] tmp = Arrays.stream(stages).boxed().toArray(Integer[]::new);
        Arrays.sort(tmp, Collections.reverseOrder());

        stages = Arrays.stream(tmp).mapToInt(Integer::intValue).toArray();

//        int stageClearTop = Arrays.stream(stages).max().getAsInt();
        // [스테이지번호, 유저수]
        ArrayList<Integer[]> stageUserCnt = new ArrayList<>();
        int cnt = 0;
        for (int i = 0; i < stages.length - 1; i++) {
            cnt += 1;
            if (stages[i] != stages[i + 1]) {
                stageUserCnt.add(new Integer[]{stages[i], cnt});
                cnt = 0;
            }
        }
        stageUserCnt.add(new Integer[]{stages[stages.length - 1], cnt + 1});


        ArrayList<Double[]> failRate = new ArrayList<>();
        int sum = 0;
        for (Integer[] stage : stageUserCnt) {
            double stageNum = stage[0];
            double userCnt = stage[1];

            sum += userCnt;

            failRate.add(new Double[]{stageNum, userCnt / sum});
        }

        failRate.sort((((o1, o2) -> {
            if (o1[1] > o2[1]) {
                return -1;
            } else if (o1[1].equals(o2[1])) {
                return (int) (o1[0] - o2[0]);
            } else {
                return 0;
            }
        })));

        boolean[] visited = new boolean[N + 1];
        cnt = 0;
        for (Double[] s : failRate) {
            int stageNum = s[0].intValue();
//            System.out.println(s[0] + " " + s[1]);
            if (s[0] != N + 1) {
                visited[stageNum] = true;
                answer[cnt++] = stageNum;
//                System.out.println("cnt : "+ cnt);
            }
        }

        for (int i = 1; i <= N; i++) {
            if (!visited[i])
                answer[cnt++] = i;
        }

        return answer;
    }
}
