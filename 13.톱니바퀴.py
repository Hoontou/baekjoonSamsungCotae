#https://www.acmicpc.net/problem/14891

import sys
sys.stdin=open("in.txt", "r")

#1,2,3,4번 톱니, 0->N극, 1->S극
#index 2 -> 세시방향(오른쪽), index 6 -> 9시 방향(왼쪽)
a = [list(map(int, input())) for _ in range(4)]
n = int(input())
R = 2
L = 6
rotateplans = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
  rotateplans[i][0] = rotateplans[i][0] -1

#돌리기 전에, 해당 rotate수행 시 뭐가 어떻게 돌아가는지 체크

def calcSideEffect(rotatePlan):
  #돌렸을 때 돌아가는 톱니들
  effects = [rotatePlan]

  #타겟 톱니의 오른쪽, 왼쪽 극
  right = a[rotatePlan[0]][R]
  left = a[rotatePlan[0]][L]
  rotate = rotatePlan[1]
  #우측을 탐색
  for i in range(rotatePlan[0]+1, 4):
    #우측으로 계속 넘어가면서
    #맞물린게 같으면 effects에 더함
    if right == a[i][L]:
      break

    #맞물린게 다르면 effects에 더함
    effects.append([i, -rotate])
      
    #다음 톱니와 비교를 위해 변수 수정
    right = a[i][R]
    rotate = -rotate

  rotate = rotatePlan[1]
  
  for i in range(rotatePlan[0]-1, -1, -1):
    #우측으로 계속 넘어가면서
    #맞물린게 같으면 effects에 더함
    if left == a[i][R]:
      break

    #맞물린게 다르면 effects에 더함
    effects.append([i, -rotate])
      
    #다음 톱니와 비교를 위해 변수 수정
    left = a[i][L]
    rotate = -rotate
  
  return effects

for i in range(n):
  #돌렸을때 변화를 계산
  effects = calcSideEffect(rotateplans[i])

  #변화를 수행
  for j in effects:
    tmp = a[j[0]].copy()
    #j[0] = 돌릴 톱니
    #j[1] = 돌릴 방향
    if j[1] == 1: #시계, 마지막이 맨앞으로.
      tmp.insert(0, tmp.pop())
    else: #반시계, 맨앞이 맨뒤로
      tmp.append(tmp[0])
      tmp = tmp[1:]

    a[j[0]] = tmp


score = 0
for i in range(4):
    if a[i][0] == 1:
        score += 2**i
print(score)