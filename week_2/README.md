# HangHae99_Chapter2
## 항해99 챕터2 자료구조/알고리즘

### 2주차 : **그래프/트리**

<details>
<summary>1일차 (그래프/트리)</summary>
<div markdown="1">

   - 과제 (문자열 조작 / 배열)
     - [전화번호 문자 조합](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
     - [순열](https://leetcode.com/problems/permutations/)
     - [조합](https://leetcode.com/problems/combinations)
   - 추가 과제
     - [단지번호붙이기](https://www.acmicpc.net/problem/2667)
     - [바이러스](https://www.acmicpc.net/problem/2606)
</div>
</details>
<details>
<summary>2일차 (BFS)</summary>
<div markdown="1">

  - 과제
    - [부분 집합](https://leetcode.com/problems/subsets/)
    - [일정 재구성](https://leetcode.com/problems/reconstruct-itinerary/)
    - [코스 스케줄](https://leetcode.com/problems/course-schedule/)
  - 추가 과제
    - [단지번호붙이기](https://www.acmicpc.net/problem/2667)
    - [바이러스](https://www.acmicpc.net/problem/2606)
</div>
</details>
<details>
<summary>3일차 (백트래킹)</summary>
<div markdown="1">

  - 과제
    - [1,2,3 더하기](https://www.acmicpc.net/problem/9095)
  - 심화 과제
    - [암호 만들기](https://www.acmicpc.net/problem/1759)
</div>
</details>
<details>
<summary>4일차 (이진 트리)</summary>
<div markdown="1">

  - 과제
    - [이진 트리의 직경](https://leetcode.com/problems/diameter-of-binary-tree/)
    - [가장 긴 동일 값의 경로](https://leetcode.com/problems/longest-univalue-path/)
    - [이진 트리 반전](https://leetcode.com/problems/invert-binary-tree/)
  - 추가 과제
    - [트리의 부모 찾기](https://www.acmicpc.net/problem/11725)
</div>
</details>
<details>
<summary>5일차 (이진 트리)
</summary>
<div markdown="1">

  - 과제
    - [이진 트리 직렬화 & 역직렬화](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
    - [균형 이진 트리](https://leetcode.com/problems/balanced-binary-tree/)
    - [최소 높이 트리](https://leetcode.com/problems/minimum-height-trees/)
  - 추가 과제
    - [트리](https://www.acmicpc.net/problem/1068)
</div>
</details>

---
## 2주차 회고
#### 최대한 "팀"을 활용하고, 내가 잘못 판단한게 아닌가? 내 자신을 의심하고 고쳐나가자.
- dfs/bfs 등 트리에 대해 공부했던 한 주 였다.

  여러탐색에 대해 개념적인 부분은 알고 있었지만, 그것을 어떻게 구현해볼지는 고민한적이 없었는데,
  
  마침 이번 주에 학습할 기회가 생겨 구현을 위해 노력을 해보았다.
  
  크게 두가지 방법으로 **재귀적인 방법, 반복적인 방법**이 있고,
  
  재귀적인 방법이 흐름에 따라 구현하면 되어 직관적이고 쉬웠다.
  
  다만, 재귀는 오버헤드가 n에 비례하게 발생하는것이 보이고, 실제로도 데이터가 조금만 늘어도 쉽게 오버플로가 나타났다.
  
  그 이후 되도록 반복적인 방법으로 구현을 해보려 많은 시도를 하였지만,
  
  반복을 하기위한 **특별한 장치가 필요하다는 것이 나의 결론**이 되었고,
  
  나는 **그 장치가 없어도 돌아가는** 반복적인 탐색을 여러번 시도 했으나 모두 실패하였다.
  
  이후, 반복하기 위한 별도의 장치를 가지고 구현은 성공했으나.. 뭔가 모를 패배감에 기쁘지는 않았다.
  
  결국엔 나의 한계를 인정하고, **모범답안, 탐색을 반복문으로 구현하는법**등을 여러 코드로 조사해보았고,
  
  의아하게도 **내가 생각했던게 나름 최선**이였다는걸 깨달았다...
  
  이때.. 느꼈던 생각은..
  
  - 내가 생각하지 못했던 최선의 방법이 물론 존재하겠지만,
  
     내가 생각했던것도 최선일 수 있다는 것이 발견되었다. 즉, 내 생각을 의심하는것도 좋지만 받아들이는것도 중요하다는걸 배웠다.
  - 두번째로는 나는 지금 시간이 부족하다는걸 매번 느낀다. 그런데 계속 나는 한가지 문제에 대해 스스로 해결하고자 욕심을 부리고 있다는 것이다.

    되돌아 생각해보면.. 이부분은 예전 내 후배직원에게도 조언했던 부분이다. 혼자서 고민하는것도 좋지만, 무엇이던 그 **정도**가 있고,
    
    시간이 부족하다면, 고민하는 시간을 적게 잡고. 해결이 안된다면 주변 직원에게 도움을 요청하라고 조언을 해 주었었다.
    
    나는 남에게 저렇게 말하면서도 나 자신은 그러지 않고 있었다. 도움을 받는것이 패배하는 것이라 느꼈기 때문이다.
    
    하지만, 결국은 도움을 받았고, 별다른 패배감은 못느꼇다. 단지.. 도움받은 내용이 경이로울 뿐이다.(와!? 이렇게 되네?)
     
  고로... 군대에서 느꼇던.. 나의 성격의 단점.
  
  내성적, 귀찮음, **개인적, 분석적**.. 이런것들을 버리고 버리려 노력했지만,
  
  아직도 나의 내면에 들어있다는것이 느껴졌다. 팀이 있다면 팀을 이용하고,
  
  이용할 수 있을때 이용하며 최대한의 이익을 서로서로 받을 수 있는 그런 환경을 만들고 이용해야겠다는걸 다시금 생각해보았다.
  
## 최대한 "팀"을 활용하고, 내가 잘못 판단한게 아닌가? 내 자신을 의심하고 고쳐나가자.