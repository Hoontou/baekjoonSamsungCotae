#https://www.acmicpc.net/problem/15685
import sys

sys.stdin = open('in.txt', 'r')

#이게 뭔 패턴이 있나 싶지만... 패턴이 있으니까 문제로 넣어놨겠지?
#3회차 까지 손으로 따라 그려보고 고민해보면 패턴이 보인다
#3회차를 그릴려면, 3회차 첫번째 획을, 2회차 마지막거를 90도 돌리고 방향 반대.
#3회차 둘째획을, 2회차 마지막 -1거를 90도돌리고 방향 반대.
#3회자 셋째 획을, 2회차 마지막 -2거를 90도 돌리고 방향 반대.
#첫회차를 0세대라 하는 이유도 2의 0승이 1 이라서 한획이라는 뜻인듯.

#오른쪽 이동을 90도 돌린 결과가 위로 이동이라는게 이상했는데,
#그냥 시작점이랑 끝점을 검지와 엄지로 짚고 끝점을 고정하고 시작점을
#시계방향으로 90도 돌려보니까 뭔말인지 이해했음.

#좀 쉽게 수정해 보면,
#회차당 그려야 하는 갯수는 이전회차의 2의 이전회차 승 만큼 이고,
#이전회차를 역순으로 올라가면서 북서남동 순으로 추가하면 된다.
#ex) 2회자 까지의 드래곤커브는, 2의 2승으로 4개고, 동북서북 임.
# 3회차에는 2의 이전회차 승인 4개를 더 그려야 함.
#2회차를 역순으로 가면서, 반시계의 순서로 다음걸 그리면 됨.
#2회차를 역순으로 하면 북서북동이고, 1번인 북 반시계는 서,
#2번인 서 반시계는 남, 3번인 북 다음은 서, 4번인 동 다음은 북.
#그래서 3회차는 서남서북임. 3회차 그리고 나면 최종 커브는
#동북서북 + 서남서북

#요약 이전회차를 역순으로 돌면서, 반시계로 방향으로 바꿔서 리스트에 붙이면 됨.

#아래 d에 맞춰 동북서남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())

#curves[i][0], [1] 은 시작점 x, y
#curves[i][2] 는 시작 방향, 0은 동 1은 북 2는 서 3은 남.
#? 시작방향에 힌트가 있는데?
#curves[i][3]는 세대.
curves = [list(map(int, input().split())) for _ in range(n)]

b = [[0] * 101 for _ in range(101)]
count = 0

#어느방향들로 가야하는지 리스트
def makeCurve(startD, g):
  result = []

  result.append(startD)

  for _ in range(g):
    tmp = []
    #result역순으로 순회
    for d in result[::-1]:
      tmp.append(next(d))
    #다담았으면 result에 붙여넣고 다음회차로
    result = result + tmp
    
  return result
    
def next(num):
  return (num+1)%4

def draw(which):
  x, y, d, g = curves[which]
  directions = makeCurve(d, g)
  #만들어진 curve대로 dx dy 이용해서 체크처리
  #맨처음 시작점 체크처리
  b[x][y] = 1
  for direction in directions:
    x += dx[direction]
    y += dy[direction]
    b[x][y] = 1
    
for i in range(n):
  draw(i)

for x in range(100):
    for y in range(100):
        if b[x][y] and b[x+1][y] and b[x][y+1] and b[x+1][y+1]:
          count += 1
print(count)
