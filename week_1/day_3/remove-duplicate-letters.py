# https://leetcode.com/problems/remove-duplicate-letters/

# Given a string s, remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.

# 주어진 문자열에서 중복된 글자를 제거하여, 유니크한 글자만 남은 문자열을 반환하되,
# 가능한 여러 결과 문자열 중 가능한 오름차순 첫번째항으로 반환하자.
# ***문자열을 재조합하면 안되고, 고정된 문자열에서 제거만 가능하다.***
# Example 2:
#
# Input: s = "(cb)acd(c)b(c))" ()를 제거
# Output: "acdb"
# class Solution:
import collections


# 1. 중복 여부를 위해 각 단어마다 횟수를 카운트 한다.
# 2. 스택에 포함 문자 여부를 체크한다.
# 3. 주어진 문자열에서 문자를 추출하면 카운트 횟수를 감소한다.
# 4. 스택의 top과 현재 문자를 비교한다.
# 4-1. top이 크다면 top의 중복단어가 있을때 pop한다.
# 4-2. 4번 과정을 반복한다.
# 5. top보다 작거나, top이 고유하다면 문자를 push한다.
# 6. 2번부터 반복한다.
def removeDuplicateLetters(self, s: str) -> str:
    # 리스트를 스택으로 사용
    stack = []

    # 스택에 들어있는 문자 확인용 ( push할때 set에도 넣고, pop할때 set에도 뺀다)
    check_stack = set()

    # 문자열의 각 단어별 횟수를 세려 중복 갯수를 확인한다. 0이면 고유하다는 의미이다.
    cnt_s_list = collections.defaultdict(int)

    # 각 문자별 횟수를 찾는다.
    for char in s:
        cnt_s_list[''.join(char)] += 1

    # 문자열 s 에서 각 문자마다 검사한다.
    for char in s:
        # 추출한 문자는 어떻게든 처리되니 cnt 감소는 선처리한다.
        cnt_s_list[char] -= 1

        # 스택이 비었으면 무조건 추가한다.
        if len(stack) == 0:
            stack.append(char)
            check_stack.add(char)
            continue

        # 스택안에 들어있는 문자인지 확인한다.
        if char in check_stack:
            continue

        # 스택의 top 문자와 비교하여 top이 크다면 반복하며 pop 한 뒤 push 한다.
        # cnt_s_list의 값이 0이면 top은 고유한 문자이니 pop 하지 않는다.
        # 스택이 비었다면 반복을 멈춘다.
        top = stack[-1]
        while len(stack) != 0 and char < top and cnt_s_list[top] != 0:
            # 중복된 단어는 제거한다.
            pop = stack.pop()
            check_stack.remove(pop)

            # 새로운 top 을 준비한다.
            if len(stack) != 0:
                top = stack[-1]

        stack.append(char)
        check_stack.add(char)

    return ''.join(stack)


print(removeDuplicateLetters('', "cdabdcbae"))
