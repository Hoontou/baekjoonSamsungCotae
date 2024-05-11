#https://www.acmicpc.net/problem/14502

from collections import deque
from itertools import combinations

n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

#b의 정보 저장
pointOf0 = []
pointOf2 = []
for row in range(n):
  for col in range(m):
    if b[row][col] == 0:
      pointOf0.append((row, col))
    elif b[row][col] == 2:
      pointOf2.append((row, col))

#세울수있는 벽은 세개
combiOf0 = list(combinations(pointOf0, 3))

#네방향 확인을 위한, 결과값을 저장할,
dRow = [1, 0, -1, 0]
dCol = [0, -1, 0, 1]
result = []

#시뮬레이션 시작
for xyList in combiOf0: 
  #xyList는 combination of poinfOf0임
  #xyList는 (x, y)의 집합, ((x,y), (x,y)...)
  tmpB = [t[:] for t in b] #딥카피
  que = deque(pointOf2)

  #xy = (row, col)
  for xy in xyList:
    #combination해서 나온 벽 위치에 벽세운다.
    tmpB[xy[0]][xy[1]] = 1
  
  #bfs수행
  while que:
    tmpPoint = que.popleft()

    #4방향 돌면서 빈공간이면 2로 수정
    for i in range(4):
      tx = tmpPoint[0] + dRow[i]
      ty = tmpPoint[1] + dCol[i]
      if not(0<=tx<=n-1 and 0<=ty<=m-1):
        #인덱스체크
        continue
      
      if tmpB[tx][ty] == 0:
        tmpB[tx][ty] = 2
        que.append((tx, ty))
  
  #이제 tmpB에 3개의 벽 세우고, 바이러스가 다 퍼진상황.
  #아직 0으로 남아있는 칸의 갯수를 result에 append한다.
  count = 0
  for i in tmpB:
    count += i.count(0)
  result.append(count)

print(max(result))