# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 중복된 문자가 없는 서브스트링 중 가장 긴 서브스트링의 길이를 반환하라.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0  # 가장 긴 서브스트링의 길이 보관
        p1 = 0 # 서브스트링 시작 인덱스

        # 한 글자씩 탐색하며 중복이 생기면,
        # 서브스트링의 시작지점을 (중복지점 +1) 부터 다시 탐색한다.
        for i, char in enumerate(s):

            # 시작지점부터 인덱스까지 서브스트링 지정
            subString = s[p1:i]

            # 서브스트링 안에 기준 글자가 중복으로 있다면,
            # 중복글자와 시작인덱스를 더하여, 중복글자 다음 글자를 시작지점으로 한다.
            if char in subString:
                gapLength = subString.find(char) + 1
                p1 += gapLength
                continue

            subStringLength = 1 + i - p1  # 현재 인덱스 - 시작지점 = 현재 길이
            if maxLength < subStringLength:  # 서브스트링이 더 길면 바꾼다.
                maxLength = subStringLength

        return maxLength


asd = Solution
print(asd.lengthOfLongestSubstring('', "pwwkew"))
# print("123456"[2:2+2].find("3"))
