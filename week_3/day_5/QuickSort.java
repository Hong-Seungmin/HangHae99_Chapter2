package day_5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

// 퀵소트 구현
public class QuickSort {
    // 숫자 출력 범위 지정
    private static final int NUM_MAX = 50;

    public static void main(String[] args) {
        QuickSort quickSort = new QuickSort();

        ArrayList<Integer> intList = new ArrayList<>();

        // 리스트에 임의값 등록
        Random random = new Random();
        for (int i = 0; i < QuickSort.NUM_MAX; i++)
            intList.add(random.nextInt(QuickSort.NUM_MAX));

        // 원본 출력
        intList.forEach(System.out::println);
        System.out.println("----");

        // 정렬
        quickSort.sort(intList, 0, intList.size() - 1);

        // 수정본 출력
        intList.forEach(System.out::println);

    }

    // 피봇을 기준으로 파트를 나누어 각각 정렬
    public void sort(ArrayList<Integer> list, int startIndex, int endIndex) {
        // 서로 만나면 끝
        if (startIndex >= endIndex) return;

        // 정렬 진행 후 다음 피봇 지정
        int pivotIndex = this.partitionSortingList(list, startIndex, endIndex);

        // 피봇 기준으로 좌,우 다시 정렬
        this.sort(list, startIndex, pivotIndex - 1);
        this.sort(list, pivotIndex + 1, endIndex);
    }

    // 피봇 기준 파트단위 정렬
    private int partitionSortingList(ArrayList<Integer> list, int startIndex, int endIndext) {
        // 피봇은 마지막 인덱스값으로 지정
        // 타겟은 -1부터 진행하여, 인덱스0 부터 스왑할 수 있도록 지정 (스왑전 +1 되니 -1로 초기화함)
        int pivot = list.get(endIndext);
        int targetIndex = startIndex - 1;

        // 피봇값과 비교하여 일치한다면 스왑 진행
        // 피봇값을 기준으로 타겟인덱스 좌,우로 작고, 큰 값을 가진 배열이 된다.
        for (int currentIndex = startIndex; currentIndex < endIndext; currentIndex++) {
            if (list.get(currentIndex) <= pivot) {
                targetIndex += 1;

//                int swapTmp = list.get(targetIndex);
//                list.set(targetIndex, list.get(currentIndex));
//                list.set(currentIndex, swapTmp);
                Collections.swap(list,targetIndex,currentIndex);
            }
        }

        // 다음 피봇인덱스의 기준점 생성
        // 피봇값이 현재 파트의 가운데 값이므로 타겟과 스왑
        targetIndex += 1;
        Collections.swap(list, targetIndex, endIndext);

        return targetIndex;
    }
}
