# https://leetcode.com/problems/longest-palindromic-substring/

# 팰린드롬이란, 서로 대칭하는 문자열을 의미한다.
# 'acbca' 혹은 'acbbca' 등 짝수 문자열, 홀수 문자열로 두가지 타입이 있다.

# 주어진 문자열에서 가장 긴 팰린드롬 문자열을 반환
def longestPalindrome(s: str) -> str:
    # expand() 팰린드롬 판별 및 투 포인터 확장
    # left    ==> 중심을 기준으로 왼쪽 포커스(포인터)
    # right   ==> 중심을 기준으로 오른쪽 포커스
    # 반환값    ==> 팰린드롬 문자열
    def expand(left: int, right: int) -> str:

        # 1. left >= 0 and right < len(s)    ==> 좌우로 확장하되, s 문자열 범위안에서 확장
        #    s 문자열 범위 ==> 0 ~ len(s)
        # 2. s[left] == s[right]    ==> 중심을 기준으로 좌우 문자가 같은가?
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # while 마지막 반복에서 각 - + 되었으므로 원위치하여 반환
        #   s[left] == s[right] 시점의 포커스까지가 팰린드롬 문자열임
        return s[left + 1:right]

    # 문자열이 한개의 단어로 되었거나, 문자열 s 자체가 팰린드롬일 경우
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    # 문자열 길이 만큼 반복하며, i 를 기준으로 좌우로 펼치며 팰린드롬 검사 진행
    # 팰린드롬 문자열 타입에 맞게, 짝수 타입 ( i +2 ), 홀수 타입 ( i + 1 ) 으로 각각 진행
    for i in range(len(s) - 1):

        # result는 최근에 발견한 가장 긴 팰린드롬 물자열을 가지고있으며,
        # max( key=len ) 을 통하여 이전에 발견한 팰린드롬과 최근 발견한 팰린드롬의 길이를 비교
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)

    return result


str = 'babad'
print('str = ', str)
print(longestPalindrome(str))

str = 'cbbd'
print('str = ', str)
print(longestPalindrome(str))
