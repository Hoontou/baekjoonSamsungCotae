#https://www.acmicpc.net/problem/3190

from collections import deque

#n 격자판 갯수, m 사과갯수
n = int(input())
m = int(input())

#보드
b = [[0]*n for _ in range(n)]
#사과의 위치를 2로 초기화
for _ in range(m):
  x, y = map(int, input().split())
  b[x-1][y-1] = 2
  
#d 머리회전 계획, 큐로 관리, popleft쓸거임.
rotateCount = int(input())
#d[0]은 몇초가 끝나면 머리돌릴건지. d[1]은 어디로 돌릴건지, changeD함수의 인자로 줄거임.
d = deque()
for _ in range(rotateCount):
  x, y = input().split()
  d.append((int(x), y))

#몸뚱아리 큐로 관리. 이동했으면 append하고, 꼬리 한칸줄어들면 popleft
body = deque()
#처음스타트 1로, 몸뚱아리에 추가
body.append((0, 0))
b[0][0] = 1
head = [0, 0]

#머리회전, 이동에 관해 정의
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
moveD = 0
def changeD(str):
  global moveD
  if str == 'D':
    moveD = (moveD + 1) % 4
  else:
    moveD = (moveD + 3) % 4

sec = 0

while True: #사과가 남아있는 동안. 인줄 알았는데 다먹어도 안끝남. 
  sec += 1

  #머리이동
  head[0] += move[moveD][0]
  head[1] += move[moveD][1]
  
  if not(0<=head[0]<=n-1 and 0<=head[1]<=n-1) or b[head[0]][head[1]] == 1:
    #머리위치가 b 밖이거나 몸통이랑 박았으면
    break
  elif b[head[0]][head[1]] == 2:
    #머리위치가 사과라면, 사과 없애고, 머리이동
    m -= 1
  else:
    #사과없으면 꼬리 한칸 없앤다.
    tail = body.popleft()
    b[tail[0]][tail[1]] = 0
  
  #머리 이동한 칸 1로 하고, body에 추가.
  b[head[0]][head[1]] = 1
  body.append((head[0], head[1]))
  
  #머리 회전해야하면,
  if d and d[0][0] == sec:
    #함수호출하고 pop한다.
    changeD(d[0][1])
    d.popleft()
  
print(sec)
