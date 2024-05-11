#https://www.acmicpc.net/problem/14503
import sys
sys.stdin = open('in.txt', 'r')

n, m = map(int, input().split())
row, col, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
#북, 동, 남, 서
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

#1은 벽, 2는 청소 완, 0은 청소 안됨
def check0ExistAroundHere(row, col):
  for i in range(4):
    if a[row+dRow[i]][col+dCol[i]] == 0:
      return True
  return False

count = 0

while True:
  if a[row][col] == 0:
    a[row][col] = 2
    count += 1
  
  if check0ExistAroundHere(row, col) == False:
    #후진가능?
    tmpD = (d + 2) % 4
    tr = row + dRow[tmpD]
    tc = col + dCol[tmpD]
    #범위 내고, 뒤로갈 수 있으면 뒤로감
    if (0<=tr<n) and (0<=tc<m) and a[tr][tc] != 1:
      row = tr
      col = tc
      continue
    else:
      break
  
  else:
    #주변 빈칸에 청소안된곳이 있다.

    #회전
    #d = 3 - d
    #아니 여기서 1번으로 돌아간다가 3-1로 돌아간다는거냐 1로 돌아가라는거냐
    for i in range(4):
      #회전
      d = (d + 3) % 4
      
      tr = row + dRow[d]
      tc = col + dCol[d]
      #보는곳이 청소 안됐어?
      if a[tr][tc] == 0:
        #전진
        row = tr
        col = tc
        break
  
print(count)
