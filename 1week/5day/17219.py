# https://www.acmicpc.net/problem/17219

# 비밀번호가 저장된 사이트의 주소와 비밀번호를 이용하여
# 주어진 사이트 주소에 대한 비밀번호를 출력하면 된다.
# 사이트 주소의 갯수(n)와 찾고자하는 사이트의 갯수(m)를 첫줄에 입력하고
# 둘째줄부터, 비밀번호가 기록된 [사이트주소 비밀번호] 양식으로 매줄(n줄) 적어준다
# 비밀번호가 있는 사이트를 다 적었다면,
# 그 다음줄부터 찾고자하는 사이트의 주소를 매줄(m줄) 적어준다.
import collections

n, m = map(int,input().split())

siteDict = {}

for _ in range(n):
    addr, pw = input().split()
    siteDict[addr] = pw

for _ in range(m):
    print(siteDict[input()])
