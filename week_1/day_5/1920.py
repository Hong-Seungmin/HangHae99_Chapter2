# https://www.acmicpc.net/problem/1920

# 첫번째로 입력한 n 만큼 두번째 정수를 n만큼 입력한다.
# 세번째로 입력한 m 만큼 네번째로 정수를 m만큼 입력한다.
# n개의 정수들에서 m개의 정수가 존재하는지 확인 후
# m의 정수가 존재하면 1 없다면 0 을 각 m의 순서에 맞게 출력한다.
import collections

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

aDict = collections.defaultdict(bool)
for num in a:
    aDict[num] = True

for num in b:
    if aDict[num]:
        print(1)
    else:
        print(0)
