# https://leetcode.com/problems/daily-temperatures/

from typing import List


# 주어진 정수 리스트에서 각 인덱스마다
# 현재 인덱스에 해당하는 값보다 더 큰 값이 나오는 인덱스와의 인덱스 차이를 반환한다.
class Solution:

    # 1. 주어진 리스트 s 와 같은 길이의 리스트를 0으로 초기화하여 생성한다.
    # 2. s를 탐색하며, {값,인덱스}를 스택에 넣는다.
    # 3-1. s[값]과 스택의 top[값]과 비교하여, top이 더 작다면,
    #    스택을 pop하여 s의 현재 인덱스와 차이값을 answer[top[인덱스]]에 넣는다.
    # 3-2. top이 더 크거나 or 같은거나 or 스택이 비을때까지 반복한다.
    # 4. 더이상 반복하지 못하면, 스택에 현재 s의 {값,인덱스}를 넣는다.
    # 5. 2번부터 다시 진행하여, s를 탐색한다.
    # * 최종적으로 s의 탐색을 마치고, 스택이 남아있다면 0으로 처리한다.
    # ** 초기 answer를 0으로 초기화 하였기 때문에 자동으로 0이 입력된다.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # answer를 0으로 초기화하여, 입력되지 않은 인덱스는 자동으로 0으로 입력한다.
        answer = [0 for _ in range(len(temperatures))]
        # {값,인덱스}를 넣을 스택을 리스트로 구성한다.
        stack = []

        # 일일온도를 가진 temperatures를 인덱스와 값을 기준으로 탐색한다.
        for i, cur_temp in enumerate(temperatures):
            # 스택이 비었거나, 스택의 top이 현재 temperatures의 값보다 클때까지 반복한다.
            # 스택에 항목이 있으면서, top의 온도가 더 작다면,
            # 더 큰값 or 스택이 비었을때까지 pop하여 스택을 탐색한다.
            # 스택 pop한 항목의 인덱스와 현재 temperatures의 인덱스를 비교하여 answer[pop[index]]에 차이값을 넣는다.
            while stack and cur_temp > stack[-1]['temp']:
                top_idx = stack.pop()['idx']
                answer[top_idx] = i - top_idx

            # 스택이 비었거나, temperatures의 온도가 top보다 작거나 같다면 스택에 {인덱스,온도}를 넣어준다.
            stack.append({'idx': i, 'temp': cur_temp})

        return answer
