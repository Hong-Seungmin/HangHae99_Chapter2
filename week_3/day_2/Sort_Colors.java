package day_2;

// https://leetcode.com/problems/sort-colors/
public class Sort_Colors {
    // nums에는 [0,1,2]가 주어지고, 이를 중간 숫자(1)을 기준으로 좌우 정렬하여야한다.
    // 외부 정렬함수를 쓰지 않고, 한번(O(n))에 정렬을 해보자.
    public void sortColors(int[] nums) {
        int length = nums.length;

        // 가운데 숫자 mid를 찾는다.
        // * 주어진 문제는 [0,1,2]으로 제한되어, 1이 mid이긴 하다.
        // * 연습삼아 mid를 찾는 로직을 구성해보았다.
        int mid = 0; // mid는 주어질 수 있는 가장 작은 숫자로 초기화한다.
        for (int num : nums) {
            if (num / 2 > mid) {
                mid = num / 2;
            }
        }

        // 정렬을 시작한다.
        // 0번 인덱스부터 순차적으로 탐색하여,
        // mid와 비교.
        //  -mid보다 작거나 같다면, 제자리.
        //  -mid보다 크다면, 중간 이후 인덱스(k)와 변경.
        // 포인터는 순차이동 i, 작은값 교체용 j, 큰값 교체용 k 를 사용한다.
        int j = 0;
        int k = length;
        for (int i = 0; i < k; i++) {
            // mid보다 작으면, i,j인덱스 값을 스왑한다.
            // 그리고 j의 올려줌으로써 교체한 값을 확정한다.
            if (nums[i] < mid) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                j += 1;
            }
            // mid보다 크다면, 뒷쪽 인덱스 k의 값과 스왑한다,
            // 그리고 k 인덱스를 내림으로써 교체한 값을 확정한다.
            else if(nums[i] > mid){
                k -= 1;  //length 부터 시작함으로 먼저 내려준다.
                int tmp = nums[i];
                nums[i] = nums[k];
                nums[k] = tmp;
                i -= 1; //원래 k인덱스의 값을 연산하기 위해 i를 올리지 않게 내려준다.
            }
        }
    }

    public static void main(String[] args) {
        Sort_Colors test = new Sort_Colors();
        test.sortColors(new int[]{0, 1, 1, 2, 2, 0, 1});
    }
}

