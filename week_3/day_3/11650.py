# https://www.acmicpc.net/problem/11650

# 주어진 좌표 x,y를 정렬한다.
# x를 우선 정렬하고,
# x가 같다면, y를 정렬한다.
# 정렬은 오른차순으로 한다.

# 입력은 첫째 줄에 좌표의 개수 n을 입력하고,
# 둘째 줄부터 각 좌표를 "x y"로 한줄씩 입력한다.

n = int(input())
coordinates = []

for i in range(n):
    coordinates.append(tuple(map(int, input().split())))

coordinates.sort(key=lambda num: (num[0], num[1]))

for i in range(n):
    print(coordinates[i][0], coordinates[i][1])