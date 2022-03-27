package day_3;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

// https://www.acmicpc.net/problem/10825
public class Boj_10825 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String[][] score = new String[n][4];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 4; j++) {
                score[i][j] = sc.next();
            }
        }

        Arrays.sort(score, (a, b) -> {
            if(Integer.parseInt(a[1]) < Integer.parseInt(b[1])){
                return 1;
            } else if(Integer.parseInt(a[1]) == Integer.parseInt(b[1])){
                if(Integer.parseInt(a[2]) > Integer.parseInt(b[2])){
                    return 1;
                } else if(Integer.parseInt(a[2]) == Integer.parseInt(b[2])){
                    if(Integer.parseInt(a[3]) < Integer.parseInt(b[3])){
                        return 1;
                    } else if(Integer.parseInt(a[3]) == Integer.parseInt(b[3]) ){
                        return a[0].compareTo(b[0]);
                    }
                }
            }
            return -1;
        });

        for(int i=0; i < n; i++){
            System.out.println(score[i][0]);
        }
    }
}

//Donghyuk 80 60 100
//Sangkeun 80 60 50
//Sunyoung 80 70 100

