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

# 1. 주어진 문자열 s 의 앞에서부터 pop
# 2. if. pop한 문자와 스택의 top 문자와 비교
#        top 문자가 더 크다면 ( ex, pop = a / top = b )
#            if. s 에서 top 문자 중복 확인
#            중복 문자가 있다면,
#                top 문자를 pop 한 뒤, 2번부터 다시 진행
#            중복 문자가 없다면,
#                pop 문자를 스택에 push
#        top 문자가 더 작다면 ( ex, pop = b / top = a )
#            s 에서 top 문자를 제거 한 뒤 스택에 push
# 3. 1번부터 다시 진행
def removeDuplicateLetters(self, s: str) -> str:
    stack = []  # 리스트를 스택으로 사용
    asd = {c: i for i, c in enumerate(s)}
    print(asd)
    list_s = list(s)
    list_s.reverse()  # 리버스 후 pop으로 진행하면 첫문자부터 나온다.

    while list_s:
        s_pop = list_s.pop()  # 문자열 s의 pop 문자
        if len(stack) == 0:  # 스택이 비었으면 바로 넣는다.
            stack.append(s_pop)
            continue

        stack_top = stack[-1]  # stack의 top 문자
        if stack_top > s_pop:  # 스택의 top 문자가 더 크다면,
            if list_s.count(stack_top) > 0:  # 중복 문자가 있다면,
                stack.pop()  # top 문자 제거
                list_s.append(s_pop)  # 이부분 개선 필요... 2번부터 진행하기 힘듬.. 일단, 다시 롤백해서 1번부터 진행하기로함
            else:  # 중복 문자가 없다면,
                if stack.count(s_pop) == 0:
                    stack.append(s_pop)
        elif stack_top < s_pop:  # 스택의 top 문자가 더 작으면,
            if stack.count(s_pop) == 0:
                stack.append(s_pop)

    return ''.join(stack)


print(removeDuplicateLetters('', "cdabdcbae"))
