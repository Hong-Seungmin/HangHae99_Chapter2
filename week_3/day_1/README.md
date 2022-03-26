# 3주차 1일

## 3월 24일
### [연습장 링크](https://jamboard.google.com/d/1RRtbY93_O4TBnbjJpeqyfENN1hR6pqw5t6wcvkEVJTs/edit?usp=sharing)

- 오늘은 이번 주차에 대한 시험을 치루는 날이고, 성공적으로 완료하였다.

    문제를 막상 볼때는 **이게 무슨말인가..** 싶다가 문득 트리주차이니 트리문제겠거니 생각해보니

    의외로 쉽게 컨셉이 잡혔다. 즉, 나의 현재 상황이 눈에 보였다.
  - 아직은 문제에 대한 해법 키워드를 유추해내지 못한다. (핵심 분석이 부족하다)
  - dfs/bfs에 대해서는 어느정도 감각이 잡혀있다.

  이정도로 나의 상태가 분석된다. 그래도.. 한문제당 30분이내로 해결하였단 점에선 뿌듯하다. 

- 힙을 구현해보았다. [참고자료1](https://rninche01.tistory.com/entry/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-04-%ED%9E%99-%EC%A0%95%EB%A0%AC)
, [참고자료2](https://intrepidgeeks.com/tutorial/implement-python-heap-data-structure-using-module-x)

  힙자체의 구동원리는 알고있었다만.. 그래도 오랜만에 코드로 보니 버벅이긴 했다.

  참고자료에서 이리저리 효율을 주기위해 변형해보았지만.. 실패 하였다.
록
  그래도 예전 썡쌩했던 머리가 일부 돌아온것 같다. 다음엔 참고 없이 다시 짜봐야겠다.

## 3월 25일

- 파이썬에서 input() 과 sys.stdin.readline() 의 차이는??

  자세히 기억은 안나지만, 다른 언어에도 여러 입출력 함수가 있고,

  각각의 특성이 있었다, 이는 표준입출력 말고도 통신을 한다던가 할때 스트림? 을 어떻게 제어하느냐의 차이로 기억한다.

  얼핏 찾아본 결과 input과 readline역시 전처리? 후처리? 가 있느냐 없느냐의 차이로 보인다.
  
  [간단한 차이점](https://www.geeksforgeeks.org/difference-between-input-and-sys-stdin-readline/)

  [누가누가 더 빠른가? 질의 응답](https://stackoverflow.com/questions/22623528/sys-stdin-readline-and-input-which-one-is-faster-when-reading-lines-of-inpu)
  

- 힙 부분은 구현하는것 외에는 딱히 문제를 풀게 안보인다.
 
  우선순위큐를 이용해야하는 문제들이 있긴한데... ㅎㅎ 오늘은 다른 유형의 문제를 풀어봤다.
---
- 새로운 조원과 세로운 방식의 스터디? 라고부르고 집단지성을 이용한 큐 구현을 해보았다.

  나는 뭐.. 내 상식선에서 아는것들 뿐이지만, 아무말않고 구현에 대한 내 나름의 구현"법"만 알려주고

  실제 로직은 그 가이드를 통한 남은 조원들이 하는 방식으로 진행하였다.

  뭐... 결과는 아직 모르겠다만.. 스터디아닌 스터디 이후 조원들의 평가는 나름 만족스러워서 다행이라 여겨진다.

  **오랜만에 객체지향적** 교과서적인 생각을 리마인드 해본 하루다. [구현물](https://github.com/HongSeumgMin/HangHae99_Chapter2/blob/main/queue.py)
- 