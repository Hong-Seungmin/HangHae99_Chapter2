import collections
from typing import List


# 애너그램은 문자열의 문자 조합을 바꾸어 새로운 문자열을 만든 것 이다.
# 'eat', 'tea', 'ate' 등이 애너그램 단어이다.

# 주어진 문자열 List에서 동일한 애너그램 단어를 그룹핑된 List로 반환한다.
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # dictionary를 사용하기에 키생성과 함께 초기화가 되는 defaultdict를 사용한다.
    # dictionary에 담길 값은 List이므로 List로 초기화한다.
    anagrams = collections.defaultdict(list)

    # 주어진 문자열 List에서 각 문자열을 추출하여 정렬 한 결과를 키값으로 지정하여 값을 넣는다.
    # 정렬을 통해 동일한 애너그램 단어는 동일한 키값을 가지게 된다.
    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print('strs = ', strs)
print(groupAnagrams(strs))
