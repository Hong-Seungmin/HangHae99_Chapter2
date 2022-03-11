from typing import List


# 숫자들을 2개씩 짝지은 뒤 각각의 페어 중 작은 값들을 합하여야한다.
# 여러 조합 중 가장 큰 합을 출력한다.
# 2개씩 짝짓는 규칙 중 가장 효과적인 방법은 작은 수는 작은 수끼리, 큰수는 큰수끼리 짝을 짓는 것이다.
# 그러기 위해선 정렬을 한 뒤 순차적으로 짝을 지으면 효과적이다.

# 주어진 숫자 List를 이용하여 모든 숫자를 2개 단위 페어로 맺은 뒤 페어 중 적은 값들의 합을 구한다.
# 여러 조합 중 가장 큰 합을 반환한다.

# 주어진 숫자 List를 오름차순 정렬 후 순차적으로 짝을지어 적은 숫자를 더하여 반환한다.
def arrayPairSum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()  # 주어진 List를 정렬한다. (오름차순)

    # 적은 숫자부터 탐색하여 짝을 짓고, 그 짝 중 작은 값을 합한다.
    for n in nums:
        # 순서에 맞게 짝을 짓는다.
        pair.append(n)

        # 2개의 숫자가 찍이 지어진다면 적은 값을 구하여 sum에 더한다.
        if len(pair) == 2:
            sum += min(pair)
            pair = []  # pair 변수를 재활용하기 위해 비워둔다.

    return sum


# 정렬된 숫자 List에서 짝수번째 숫자가 arrayPairSum()의 작은 숫자와 같은 것을 이용한다.
# 짝을 짓는 절차가 생략되어 공간복잡도가 낮아진다.
def arrayPairSum2(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    # index를 얻기 위해 enumerate()를 확용한다.
    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum


nums = [1, 4, 3, 2]
print('nums = [1, 4, 3, 2]')
print(arrayPairSum(nums))
print(arrayPairSum2(nums))
