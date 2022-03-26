package day_2;

public class InsertionSortList {
    public static void main(String[] args) {
        System.out.println("-");
        Solution sol = new Solution();
        int[] nums = new int[]{3, 6, 3, 5, 9, 6, 4, 2, 4, 8, 9, 65, 3, 2, 5};
        System.out.println("--");
        ListNode head = sol.push(nums);
        System.out.println("---");
        ListNode head2 = sol.insertionSortList(head);

        System.out.println("aa");
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
        System.out.println("bb");
        while (head2 != null) {
            System.out.println(head2.val);
            head2 = head2.next;
        }
        System.out.println("cc");
    }

}


class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}


class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode rootNode = new ListNode(-5001);
        ListNode curNode = rootNode;
        while (head != null) {
            ListNode tmpNode = head.next;
            while (curNode.next != null && curNode.next.val < head.val) {
                curNode = curNode.next;
            }
            head.next = curNode.next;
            curNode.next = head;
            head = tmpNode;

            if ( head != null && curNode.val > head.val){
                curNode = rootNode;
            }
        }
        return rootNode.next;
    }

    public ListNode push(int[] nums) {
        int length = nums.length;
        ListNode tmpNode = null;
        ListNode result = null;
        for (int num : nums) {
            ListNode node = new ListNode(num, null);
            if (tmpNode == null) {
                result = node;
            } else {
                tmpNode.next = node;
            }
            tmpNode = node;
        }
        return result;
    }
}

