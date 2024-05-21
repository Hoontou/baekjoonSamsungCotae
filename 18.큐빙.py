#https://www.acmicpc.net/problem/5373
import sys
sys.stdin = open('in.txt', 'r')

#일단 6면 정의부터
cube = {
  'U': [['w'] * 9],
  'D': [['y'] * 9],
  'F': [['r'] * 9],
  'B': [['o'] * 9],
  'L': [['g'] * 9],
  'R': [['b'] * 9]
}

n = int(input())
case = []
for _ in range(n):
  useless = input()
  tmp = list(input().split())
  case.append(tmp)

#돌리는건, 알파벳을 방향을 본 후, +면 시계, -는 반시계.
#딱보니, 한 면을 90도로 돌리는 함수랑
#영향받는 라인 싹다 고치는 함수면 되겠는데
#근데 더럽겠구만 딱봐도
#걍 하드코딩 파바바박하면 뚝딱되긴 할듯

#012 301 125
#345 642 048
#678 785 367
#원래, +, -
plus = [3,0,1,6,4,2,7,8,5]
minus = [1,2,5,0,4,8,3,6,7]

#바라보고 있는 면 돌리는 함수.
def rotWatching(string): #string ex) U+
  watching = cube[string[0]] #돌릴 면
  tmp = watching[::] #원상태
  d = plus if string[1] == '+' else minus
  
  for i in range(9):
    watching[i] = tmp[d[i]]
  return
  
#다른면 돌리는 함수
def rotOther(string):
  #하 ㅋㅋㅋㅋㅋ 암만생각해도 하드코딩밖에 없는데??
  #6면 * 수정해야하는 면 4개 * 2방향 -> ??
  #더럽다 그냥
  return