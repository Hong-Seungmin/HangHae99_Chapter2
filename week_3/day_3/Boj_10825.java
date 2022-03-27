package day_3;

import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

// https://www.acmicpc.net/problem/10825
public class Boj_10825 {

    // 1. 학생의 수 N 을 입력한 다음,
    // 2. N만큼 각 학생의 이름과 성적을 한줄씩 입력한다.
    // - 국어점수 최우선으로 내림차순 정렬한다.
    // - 영어점수를 다음으로 오름차순 정렬한다. (국어가 동점일때)
    // - 수학점수를 다음으로 내림차순 정렬한다. (국어,영어가 동점일때)
    // - 모든 점수가 동일하면 이름을 기준으로 오름차순 정렬한다.
    // 3. 이름을 출력한다.
    public static void main(String[] args) throws IOException {

        // 1차 시도에서 시간초과가 떠서 입출력을 바꾸었다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 학생 수를 입력한다.
        int n = Integer.parseInt(br.readLine());

        // 학생들을 담을 공간을 생성한다.
        Student[] score = new Student[n];

        // 학생들의 성적을 입력한다.
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            score[i] = new Student(
            input[0],
            Integer.parseInt(input[1]),
            Integer.parseInt(input[2]),
            Integer.parseInt(input[3])
            );

        }

        // 성적비교를 위해 sort 기준을 만들어준다.
        // * return값이 양수일 경우 a, b의 위치를 바꾼다 생각하면 된다.
        Arrays.sort(score, (a, b) -> {

            // a가 작다면 서로 교환하여 작은 수 a를 뒤로 보낸다. (내림차순)
            if (a.kor < b.kor) {
                return 1;
            } else if (a.kor == b.kor) {
                // a가 크다면, a를 뒤로 보낸다. (오름차순)
                if (a.eng > b.eng) {
                    return 1;
                } else if (a.eng == b.eng) {
                    // a가 작다면, a를 뒤로 보낸다. (내림차순)
                    if (a.math < b.math) {
                        return 1;
                    } else if (a.math == b.math) {
                        return a.name.compareTo(b.name);
                    }
                }
            }
            return -1;
        });

        for (int i = 0; i < n; i++) {
            bw.write(score[i].name + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }


}
class Student {
    String name;
    int kor;
    int eng;
    int math;

    Student(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }
}

//Donghyuk 80 60 100
//Sangkeun 80 60 50
//Sunyoung 80 70 100

