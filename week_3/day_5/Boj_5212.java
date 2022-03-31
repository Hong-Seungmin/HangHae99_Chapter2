package day_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/5212
public class Boj_5212 {
    public static void main(String[] args) throws IOException {
        int[] dr = new int[]{0, 0, 1, -1};
        int[] dc = new int[]{1, -1, 0, 0};

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        String[] board = new String[R];
        for (int i = 0; i < R; i++) {
            board[i] = br.readLine();
        }

//        for (int i = 0; i < board.length; i++) {
//            System.out.println(board[i]);
//        }

        boolean[][] visited = new boolean[R][C];
        StringBuilder sb;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (board[r].charAt(c) == 'X') {
                    visited[r][c] = true;
                    int cnt = 0;
                    for (int i = 0; i < 4; i++) {
                        int nr = r + dr[i];
                        int nc = c + dc[i];

                        if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
                            if (!visited[nr][nc] && board[nr].charAt(nc) == '.') {
                                cnt += 1;
                            }
                        }else{
                            cnt += 1;
                        }
                    }
                    if (cnt >= 3) {
                        sb = new StringBuilder(board[r]);
                        sb.setCharAt(c, '.');
                        board[r] = sb.toString();
                    }
                }
            }
        }

        for (String s : board) {
            System.out.println(s);
        }
        System.out.println();

        int startR = 0;
        int endR = R - 1;
        int startC = 0;
        int endC = C - 1;
        boolean[] flag = new boolean[]{false, false, false, false};
        while (true) {
            if (!board[startR].contains("X")) {
                startR++;
                flag[0] = true;
            } else if(!flag[0] && startR == 0) flag[0] = true;
            if (!board[endR].contains("X")) {
                endR--;
                flag[1] = true;
            } else if(!flag[1] && endR == R - 1) flag[1] = true;
            int r = 0;
            boolean startFlag = true;
            boolean endFlag = true;
            while (r != R) {
                if (startFlag && board[r].charAt(startC) == 'X') {
                    startFlag = false;
                    flag[2] = true;
                }
                if (endFlag && board[r].charAt(endC) == 'X') {
                    endFlag = false;
                    flag[3] = true;
                }
                r++;
            }
            if (startFlag)
                startC++;
            if (endFlag)
                endC--;

            int cnt = 0;
            for (int i = 0; i < 4; i++) {
                if (flag[i]) cnt++;
            }
            if (cnt == 4) break;
        }

        for (int r = startR; r <= endR; r++) {
            System.out.println(board[r].substring(startC, endC + 1));
        }
    }
}
