package day_2;

// https://www.acmicpc.net/problem/5052

import com.sun.xml.internal.fastinfoset.util.StringArray;

import java.io.*;
import java.util.Arrays;

public class JAVA_5052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter((new OutputStreamWriter(System.out)));
        String str = br.readLine();

        int t = Integer.parseInt(str);

        for (int i = 0; i < t; i++) {
            str = br.readLine();
            int n = Integer.parseInt(str);
            String[] strs = new String[n];
            for (int j = 0; j < n; j++) {
                strs[j] = br.readLine();
            }
            Arrays.sort(strs);
            boolean flag = true;
            for (int j = 0; j < n - 1; j++) {
                if (strs[j + 1].startsWith(strs[j])) {
                    flag = false;
                    break;
                }
            }
            if(flag){
                bw.write("YES\n");
            }else{
                bw.write("NO\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
