
//https://programmers.co.kr/learn/courses/30/lessons/17686

import java.util.Arrays;

public class Prog_17686 {

    public static void main(String[] args) {
        Prog_17686.Solution sol = new Prog_17686.Solution();

        String[] strs = new String[]{"img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"};
//        int[] citations = new int[]{10, 9, 7, 6, 2, 1};
        System.out.println(Arrays.toString(sol.solution(strs)));
    }

    static class Solution {
        public String[] solution(String[] files) {
            Document[] docs = new Document[files.length];
            for (int i = 0; i < files.length; i++) {
                docs[i] = new Document(files[i]);
            }

            Arrays.sort(docs, (o1, o2) -> {
                if (o1.head.compareTo(o2.getHead()) < 0) {
                    return -1;
                } else if (o1.head.compareTo(o2.getHead()) == 0) {
                    return Integer.parseInt(o1.number) - Integer.parseInt(o2.number);
                }
                return 1;
            });
//            for (int i = 0; i < files.length; i++) {
//                System.out.println(docs[i].head);
//                System.out.println(docs[i].number);
//                System.out.println(docs[i].tail);
//                System.out.println("---");
//            }
            String[] answer = new String[files.length];

            for (int i = 0; i < files.length; i++) {
                answer[i] = docs[i].toString();
            }
            return answer;
        }
    }

    static class Document {
        String fileName;
        String head = "";
        String number = "";
        String tail = "";

        @Override
        public String toString() {
            return fileName;
        }

        public String getHead() {
            return head;
        }

        public String getNumber() {
            return number;
        }

        public String getTail() {
            return tail;
        }

        public Document(String fileName) {
            this.fileName = fileName;

            int index = 0;

            // head 추출
            while (index != fileName.length()) {
                char ch = fileName.charAt(index);
                if (ch >= '0' && ch <= '9') {
                    break;
                }
                this.head += ch;
                index += 1;
            }
            this.head = this.head.toLowerCase();

            //number 추출
            while (index != fileName.length()) {
                char ch = fileName.charAt(index);
                if (ch < '0' || ch > '9') {
                    break;
                }
                this.number += ch;
                index += 1;
            }


            while (index != fileName.length()) {
                char ch = fileName.charAt(index);
                this.tail += ch;
                index += 1;
            }
        }

        public String getFileName() {
            return fileName;
        }


    }
}


