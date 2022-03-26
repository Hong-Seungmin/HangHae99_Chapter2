# https://leetcode.com/problems/3sum/

from typing import List


# 주어진 숫자 List에서 합이 0이 되는 숫자 3개의 조합을 출력한다.
# 조합과 순열의 중 조합의 방식으로 풀어야하기에 정렬을 사용한 중복숫자를 찾아내야한다.

# 브루트 포스로 계산
# 3개의 숫자를 순차적으로 탐색 모든 조합을 검사한 뒤 0이 되는 숫자 조합 List를 반환한다.
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    # 3개의 숫자 중 첫번째 숫자를 기준잡는다.
    for i in range(len(nums) - 2):
        # 중복숫자는 무시한다.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 3개의 숫자 중 두번째 숫자를 기준잡는다.
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # 3개의 숫자 중 세번째 숫자를 기준잡으며, 3개 숫자 모두 합하여 0이 되는지 확인한다.
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue

                # 숫자의 합이 0이 된다면 results 변수에 추가하여 보관한다.
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results


# 투 포인터를 이용하여 처리 ( 기준 숫자와 기준 숫자에서 처음(포인터1)과 끝(포인터2)숫자 )
# 기준숫자는 0부터 시작하며 숫자 List의 마지막 -2 번째까지 탐색한다.
# (-2번째인 이유는 합을 구하는 3개의 숫자 (기준숫자) (처음숫자) (끝숫자) 3개의 숫자 조합이 가능한 마지막이기 때문이다.
# 투포인터를 이용하여 시간복잡도를 n^2 이하로 처리하여 결과를 반환한다.
def threeSum2(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    # 기준숫자를 0부터 마지막 -2번째까지 탐색한다.
    for i in range(len(nums) - 2):

        # 이전 숫자와 비교하여 같은 숫자라면 무시한다.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # i(기준숫자)를 기준으로 left(처음)과 right(끝) 숫자를 구한다.
        left, right = i + 1, len(nums) - 1

        # left와 right가 같아질때까지 반복한다.
        # left와 right가 같다는 것은 더이상 조합할 숫자가 없다는 의미이다.
        while left < right:
            sum = nums[i] + nums[left] + nums[right]  # 기준숫자, 처음숫자, 끝숫자를 더한다.

            # 합이 음수라면 left를 움직여 더 큰 숫자를 합한다. (left는 오름차순으로 이동)
            if sum < 0:
                left += 1

            # 합이 양수라면 right를 움직여 더 작은 숫자를 합한다 (right는 내림차순으로 이동)
            elif sum > 0:
                right -= 1

            # 합이 0이라면 results List에 0이 되는 조합을 보관한다.
            else:
                results.append([nums[i], nums[left], nums[right]])

                # left와 right가 같다면 더이상 조합할 숫자가 없다.
                # left의 이동 방향과 right의 이동방향에 따라 중복된 숫자가 나타나면 무시한다.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 다음 조합할 숫자로 이동한다.
                # 처음 숫자는 오름차순으로 이동
                # 끝 숫자는 내림차순으로 이동
                left += 1
                right -= 1

    return results


nums = [-1, 0, 1, 2, -1, -4]
print('nums = ', nums)
print(threeSum(nums))
print(threeSum2(nums))
