#https://www.acmicpc.net/problem/16234
import sys
from collections import deque
sys.stdin = open('in.txt', 'r')

N, L, R = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def calcTotalPeople(list):
  t = 0
  for x, y in list:
    t += b[x][y]
  return t

def modPeople(list, num):
  for x, y in list:
    b[x][y] = num

#while 인구이동 끝날때 까지,
#매 회차때 마다 
#bfs로?
#모든 나라보드 돌면서 
#주변 다 보고 연합할 조건 충족하는애 있으면
#그 애랑 나를 tmp로 연합에 채워넣음. 그리고 bfs큐에 삽입
isFin = False
count = 0

while isFin == False:
  isFin = True
  t = [[0] * N for _ in range(N)] #lookup한적 있냐 체크
  for x in range(N):
    for y in range(N):
      tmp = [] #연합
      que = deque()
      if t[x][y] == 0: #lookup 한적 없으면
        tmp.append((x, y)) #나는 일단 연합에 넣고 나랑 할사람 찾는거임.
        que.append((x, y)) #연합에 담을 bfs돌리기 위한 큐
      while que:
      #네방향 보면서, 인덱스 이내이고, 조건에 맞으면, lookup체크하고 큐에넣고
        currX, currY = que.popleft()
        t[currX][currY] = 1 #lookup체크해주고
        for i in range(4):
          tx = currX + dx[i]
          ty = currY + dy[i]
          #인덱스 이내이고, lookup한적이 없고, 나랑 쟤랑 인구수가 다르고, 인구차가 범위 이내이면
          if 0<=tx<N and 0<=ty<N and t[tx][ty] == 0 and L<=abs(b[currX][currY] - b[tx][ty])<=R:
            t[tx][ty] = 1 #lookup 체크
            tmp.append((tx, ty)) #연합에 삽입.
            que.append((tx,ty)) #큐에 삽입.
      #이까지 왔으면, bfs싹다돌면서 x,y와 연합을 맺은거임, 
      #그리고 tmp에 연합 들어가있음. x,y도 들어가있음.
      #그럼 이제 연합에 있는애들 싹다 인구 합쳐서 len(tmp)로 나눠서 싹다수정.
      if len(tmp) >= 2:
        #연합에 둘 이상있다? 
        modPeople(tmp, calcTotalPeople(tmp) // len(tmp)) #인구이동.
        isFin = False #인구이동을 했다는 뜻. 다음 인구이동도 수행.
        
        
      #연합에 혼자있으면 아무것도 안함.
  #while 회차 끝, 회차 count +
  if isFin == False:
    count += 1


print(count)

# ?? 시간초과나는데?
# 크게 줄일만한곳이 없어보이는데?;;
#딱 80퍼에서 시간초과난다..
# pypy로 돌리니까 통과.
#그래 더 줄일곳이 ㄹㅇ 없었는데 휴