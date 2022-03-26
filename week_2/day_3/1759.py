# https://www.acmicpc.net/problem/1759

# 주어진 문자열을 이용하여 암호가 될 수 있는 모든 사전식 오름차순 문자열을 출력하라.
# 입력된 C개의 알파벳에서 L개를 추출하여 문자열을 조합해야한다.
# 입력은 L과 C 그리고 C개의 알파벳 소문자를 입력한다.
# 출력은 L개의 문자로 이루어진 가능한 모든 문자열을 출력한다.

L, C = map(int, input().split())
main_str = input().split()
# 사전식으로 출력해야함으로 정렬을 한다.
main_str.sort()


# start_index부터 main_str을 탐색한다.
# *main_index[start_index:]
def dfs(start_index):
    # 길이를 만족하면 자음 모음 갯수를 세아린 후 적합하면 answer에 등록한다.
    if len(answer) == L:
        cnt_vowel = 0
        cnt_consnant = 0
        # 각 글자별로 판단
        for char in answer:
            # 모음 확인
            if char in ('a', 'e', 'i', 'o', 'u'):
                cnt_vowel += 1
            # 자음 확인
            else:
                cnt_consnant += 1
        # 결과에 만족하면 answer를 출력한다.
        if cnt_vowel >= 1 and cnt_consnant >= 2:
            print(''.join(answer))
        # 결과 유무에 상관없이 L글자라면 True를 반환하여, pop을 유도한다.
        return True

    # start_index에 동적인 갭을 주어 중복을 방지한다.
    # *이부분이 설계하면서도 헤깔리는 변수이다..
    # *더 쉬운방법을 찾아봐야한다.
    start_index_gap = 0

    # main_str을 순번에 맞게 탐색한다.
    # 4글자를 만들수없는 범위(뒤쪽)까지 탐색을한다. 이부분은 변경하여야한다.
    # 첫 호출(start_index가 0일때)는 중간까지 탐색, 그 이후는 점차 끝까지 범위를 조절해야한다.
    # (완료) 나름 처리하지 않아도 될 부분은 줄였다. C - L + start_index + 1 // 반복이 1은 미만됨으로 1 더한것이다.
    for char in main_str[start_index:C - L + start_index + 1]:
        answer.append(char)
        if dfs(start_index + 1 + start_index_gap):
            answer.pop()
            continue
        answer.pop()
        start_index_gap += 1

    return False


answer = []
dfs(0)
