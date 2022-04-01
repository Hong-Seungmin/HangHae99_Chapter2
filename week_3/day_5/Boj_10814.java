package day_5;

// https://www.acmicpc.net/problem/10814

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

// 정렬 우선순위 문제이다.
// 나이는 오름차순, 이름은 먼저 입력된 순서로 출력하면된다.
// * 우선순위랄것도 없이, 입력된 배열 그대로 나이순으로 정렬하면 될것 같다.
public class Boj_10814 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        ArrayList<Human> users = new ArrayList<>();
        for(int i=0; i< N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            users.add(new Human(Integer.parseInt(st.nextToken()), st.nextToken()));
        }

        Collections.sort(users);

        users.forEach(System.out::println);
    }

    static class Human implements Comparable<Human>{
        public int age;
        public String name;
        public Human(int age, String name) {
            this.age = age;
            this.name = name;
        }

        @Override
        public int compareTo(Human o) {
            return this.age - o.age;
        }

        @Override
        public String toString(){
            return this.age +" "+ this.name;
        }
    }
}
