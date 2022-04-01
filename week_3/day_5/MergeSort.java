package day_5;

import java.util.ArrayList;
import java.util.Random;

public class MergeSort {
    private static final int NUM_MAX = 20;

    public static void main(String[] args) {
        MergeSort mergeSort = new MergeSort();

        ArrayList<Integer> intList = new ArrayList<>();

        // 리스트에 임의값 등록
        Random random = new Random();
        for (int i = 0; i < MergeSort.NUM_MAX; i++)
            intList.add(random.nextInt(MergeSort.NUM_MAX));

        // 원본 출력
        intList.forEach(System.out::println);
        System.out.println("----");

        // 정렬
        intList = mergeSort.sort(intList);

        // 수정본 출력
        intList.forEach(System.out::println);

    }

    // 머지 정렬
    // sort() 에서는 분할을 한다.
    // 분할된 개별 리스트를 merge()로 보내어 합병하는 구조이다.
    public ArrayList<Integer> sort(ArrayList<Integer> list) {
        if (list.size() == 1) return list;

        // 가운데를 기준으로 좌,우 분할 한다.
        int mid = list.size() / 2;
        ArrayList<Integer> leftList = new ArrayList<>(list.subList(0, mid));
        ArrayList<Integer> rightList = new ArrayList<>(list.subList(mid, list.size()));

        // merge()로 좌,우를 보내어 다시 합병한다.
        return this.merge(sort(leftList), sort(rightList));
    }

    // list1과 list2의 첫 인덱스부터 비교하며, 크기순으로 새로운 list에 담아 반환한다.
    private ArrayList<Integer> merge(ArrayList<Integer> list1, ArrayList<Integer> list2) {
        ArrayList<Integer> result = new ArrayList<>();

        int i = 0;
        int j = 0;

        // 어느 한쪽이 끝날때까지 반복
        while (i < list1.size() && j < list2.size()) {
            if (list1.get(i) < list2.get(j)) {
                result.add(list1.get(i));
                i += 1;
            } else {
                result.add(list2.get(j));
                j += 1;
            }
        }

        // 남은 부분 정리
        while (i < list1.size()) {
            result.add(list1.get(i));
            i++;
        }
        while (j < list2.size()) {
            result.add(list2.get(j));
            j++;
        }

        return result;
    }
}
