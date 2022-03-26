# 2주차 4일

## 3월 22일
### [연습장 링크](https://jamboard.google.com/d/1EZq1AUI5OeHRADQeOz8iHx66xoEBRMkEKMn_gONsTPs/edit?usp=sharing)

- 이진트리가 시작되었다. 다른트리에비해 좌우 두가지 자식만 비교하면되어서 나름 쉬웠던 기억이 난다.

    두개 뿐이여서, 배열로도 표현이가능하고, 배열이라면 루트를 0번으로잡고 N*2+1(좌), N*2+1(우)로 자식을 찾을 수 있다.

- dfs를 반복문으로 구현한 알맞은 샘플을 구하였다. "이진트리 지름" 코드에 주석으로 설명하였다.

  예상대로? 감각? 에 맞게 부모,자식간의 구분하는 트리거는 있었지만..

  스택에서 뽑자마자 다시 넣는.. 기본적인 생각을 왜 못했을까 싶다.. 아무튼.. 힌트는 충분히 얻은것 같다. 다시 도전해봐야겠다.

- 비교연산자에 대해 공부를 해보았다. 단순히 ==와 is를 동등하다 생각하였는데,

  마침 오류가 발생하여 찾아보니 값이냐 참조냐 차이가 있다는걸 깨달았다, 덕분에 다른 연산자도 공부하였다.

---
- 며칠 전.. **ide 오류인가?** 싶어서 여러 조치를 하였지만 잘되지 않았던 문제가 있었다.

  그 문제는... `전역변수를 로컬에서 사용되지 않는`문제였다.
  
  즉, 전역에 a변수를 초기화하였고, def를 통한 함수 내부에서 a를 쓰려는데.. 왠걸??

  밑줄이 쫙 뜨면서 미참조? 오류가 뜨는것이다.. 뭐 대강 없는 변수에 무언가 하려한다는 기분이 들고..

  처음에는 ide 인덱싱 오류겠거니 싶어서 이것저것 해보았는데.. 결국 스코프 문제같은 기분이 들어 global을 처리하여 해결하긴하였다.

  방금도 동일한 이유가 발생하여 이번에는 확실하게 이유를 찾아보았더니..
  - 전역변수를 읽기는 가능하다.
  - 단, 쓰기작업은 못한다.

  라는 글을 찾게 되었다. 덧붙여서 global 말고 nonlocal이란 키워드도 발견하였다.

  프로그래밍언어의 키워드는 직관성이 정말 중요해 보인다. 키워드만 발견하였는데.. 어찌 사용할지 대강 느낌이온다.
  - global : `전역변수`를 로컬에서 사용하겠다는 의도
  - nonlocal : `다른 로컬변수`를 현재 스코프에서 사용하겟다는 의도

  아래는 스코프에 대한 예제이다.
```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

위 코드를 보면 마지막 출력에 `In global scope: global spam` 이 나오는 이유가 의아하지만,

역시나.. `do_global()`에서 `global spam`을 선언한 부분에서 **전역변수가 생성**되었다고 보면된다.