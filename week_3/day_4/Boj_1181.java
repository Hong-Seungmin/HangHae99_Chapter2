package day_4;

import java.io.*;
import java.util.Arrays;

// https://www.acmicpc.net/problem/1181
public class Boj_1181 {

    // 입력된 단어들을 정렬하여 출력한다.
    // 정렬은 1. 길이가 짧은것부터, 2. 길이가 같다면 사전 순으로
    // 중복된 단어는 출력하지 않는다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        String[] words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        // 우선순위에 맞게 정렬
        Arrays.sort(words, ((o1, o2) -> {
            if (o1.length() < o2.length()) {
                return -1;
            } else if (o1.length() == o2.length()) {
                return o1.compareTo(o2);
            } else {
                return 1;
            }
        }));

        // 중복단어 제거
        //words를 스트림객체로 전환 -> 중복제거 -> 어레이객체로 전환
        words = Arrays.stream(words).distinct().toArray(String[]::new);
        for (String word : words) {
            bw.write(word + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
