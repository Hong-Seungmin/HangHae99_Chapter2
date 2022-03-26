package day_2;

// 오랜만에 자바를 써보았다. 문법이 확실히 번거롭다..

public class Bubblesort {
    public static void main(String[] arg) {
        Bubblesort bubble = new Bubblesort();
        int[] nums = {6, 4, 8, 56};
        bubble.bubbleSort(nums);
        for (int num : nums) {
            System.out.println(num);
        }
    }

    public void bubbleSort(int[] nums) {
        int length = nums.length;

        for (int i = 1; i < length; i++) {
            for (int j = 0; j < length - i; j++) {
                if (nums[j] > nums[j + 1]) {
                    int tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                }
            }
        }

    }
}
