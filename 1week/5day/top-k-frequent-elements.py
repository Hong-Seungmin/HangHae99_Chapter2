# https://leetcode.com/problems/top-k-frequent-elements/
import collections
from typing import List


# 주어진 정수 리스트에서 가장 빈번한 정수를 k 갯수로 반환한다.
# k가 2이면서, 1이 가장 빈번하고 3이 다음으로 빈번하다면, [1,3]을 반환.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = collections.defaultdict(int)

        for n in nums:
            numsDict[n] += 1

        # numsDickt의 아이템을 뽑아와서, 값을 기준으로 (x[1]) 내림차순 정렬
        sortedNumsDict = dict(sorted(numsDict.items(), key=lambda x: x[1], reverse=True))

        # 정렬된 딕셔너리의 키를 뽑아서 k만큼 반환
        return list(sortedNumsDict.keys())[:k]
