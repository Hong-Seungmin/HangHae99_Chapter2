package day_5;

import java.util.ArrayList;
import java.util.Random;

public class QuickSort {
    public static void main(String[] args) {
        QuickSort quickSort = new QuickSort();
        ArrayList<Integer> intList = new ArrayList<>();
        Random random = new Random();

        for (int i = 0; i < 5; i++)
            intList.add(random.nextInt(100));
        intList.forEach(System.out::println);
        System.out.println("----");
        quickSort.sort(intList, 0, intList.size() - 1);

        intList.forEach(System.out::println);

    }

    public void sort(ArrayList<Integer> list, int startIndex, int endIndex) {
        if (startIndex >= endIndex) return;

        int pivotIndex = this.partitionSortingList(list, startIndex, endIndex);

        this.sort(list, startIndex, pivotIndex - 1);
        this.sort(list, pivotIndex + 1, endIndex);
    }

    private int partitionSortingList(ArrayList<Integer> list, int startIndex, int endIndext) {
        int pivot = list.get(endIndext);
        int targetIndex = startIndex - 1;

        for (int currentIndex = startIndex; currentIndex < endIndext; currentIndex++) {
            if (list.get(currentIndex) <= pivot) {
                targetIndex += 1;

                int swapTmp = list.get(targetIndex);
                list.set(targetIndex, list.get(currentIndex));
                list.set(currentIndex, swapTmp);
            }
        }

        return targetIndex + 1;
    }
}
