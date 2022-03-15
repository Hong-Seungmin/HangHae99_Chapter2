# https://leetcode.com/problems/jewels-and-stones/

# 주어진 jewerls를 참조하여, stones에서 jewerl의 갯수를 반환하라.
import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsDict = collections.defaultdict(int)

        for stone in stones:
            jewelsDict[stone] += 1

        # 되는지 해봤는데 되더라..
        # 우측부터 해석하면 된다.
        # jewels에서 i에 대한 리스트를 만들고, 그 리스트를 이용하여 i를 jewelsDict에서 찾아 리스트를 만들고, 그 리스트를 sum한다.
        # 즉, 위 반복문에서 +1 한 stone 중 jewels만 값을 리스트로 뽑아내어 sum한 것이다.
        return sum([jewelsDict[i] for i in [i for i in jewels]])
