package day_3;
// https://www.acmicpc.net/problem/1012

import java.io.*;
import java.util.StringTokenizer;

// 섬의 갯수를 찾는 문제와 동일하다.
// 서로 인접한 배추가 심어진 구역의 갯수를 찾으면 된다.
// 단, 섬문제는 지도가 주어졌으나, 배추는 좌표가 주어졌다는 차이가 있다.
// 당장에는 좌표만 이용하여 구할 수 있을 것으로 느껴진다.
public class Boj_1012 {
    // 인접구역의 상대 좌표
    static int[] dx = new int[]{0, 0, 1, -1};
    static int[] dy = new int[]{1, -1, 0, 0};

    // 가로(M), 세로(N) 크기
    static int[] M;
    static int[] N;

    // 배추의 개수
    static int[] K;

    // 배추가 심어진 위치
    static boolean[][] baeChuXY;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 배추 구역 개수
        int baechuCount;

        // 가로,세로 범위 입력 받은 뒤, 초기 세팅
        int T = Integer.parseInt(br.readLine());
        M = new int[T];
        N = new int[T];
        K = new int[T];
        for (int caseNum = 0; caseNum < T; caseNum++) {
            baechuCount = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            M[caseNum] = Integer.parseInt(st.nextToken());
            N[caseNum] = Integer.parseInt(st.nextToken());

            K[caseNum] = Integer.parseInt(st.nextToken());

            baeChuXY = new boolean[M[caseNum]][N[caseNum]];
            for (int i = 0; i < K[caseNum]; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                // 배추 위치 기록
                baeChuXY[x][y] = true;
            }
            // ^^^테스트 케이스별 초기화 완료^^^

            // 로직 구역 계산 시작
            for (int x = 0; x < M[caseNum]; x++) {
                for (int y = 0; y < N[caseNum]; y++) {
                    if (baeChuXY[x][y]) {
                        // dfs로 배추를 발견하면 baeChuXY를 false로 변경
                        countBAECHU(x, y, caseNum);
                        baechuCount += 1;
                    }
                }
            }
//            System.out.println(count);
            bw.write(baechuCount + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }

    // dfs로 배추를 발견하면 baeChuXY를 false로 변경
    public static void countBAECHU(int x, int y, int t) {
        for (int i = 0; i < 4; i++) {
            int relX = x + dx[i];
            int relY = y + dy[i];

            if (relX < 0 || relX >= M[t] || relY < 0 || relY >= N[t] || !baeChuXY[relX][relY]) {
                continue;
            }

            baeChuXY[relX][relY] = false;
            countBAECHU(relX, relY, t);
        }
    }
}
