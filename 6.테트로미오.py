#https://www.acmicpc.net/problem/14500

import sys
sys.stdin=open("in.txt", "r")

row, col = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(row)]
check = [[0]*col for _ in range(row)]

dr = [0, 1 ,0, -1]
dc = [1, 0 ,-1, 0]

maxSum = 0

def isWithinIndex(r, c):
  global row, col
  if not(0<=r<row) or not(0<=c<col):
    return False
  return True

#현재 바라보는 row, col, 지금까지의 합계, 방금 지나온 방향, 깊이depth
def dfs(r, c, sum = 0, deps = 0):
  global maxSum

  if deps == 4:
    maxSum = max(sum, maxSum)
    return

  if not(isWithinIndex(r, c)):
    return

  #현재 칸이 왔던곳이면
  if check[r][c] == 1:
    return
  
  for i in range(4):
    tr = r + dr[i]
    tc = c + dc[i]

    #현재 칸 체크하고,  다음칸으로 현재까지의 합계를 넘김
    check[r][c] = 1
    dfs(tr, tc, sum + a[r][c], deps + 1)
    check[r][c] = 0

    
#ㅗ모양 계산
def func(r, c, base):
  global maxSum
  tmp = base
  
  for i in range(4):
    for j in range(4):
      #4방향중 한방향을 제외해서 바라봄
      if j == i:
        continue
      tr = r + dr[j]
      tc = c + dc[j]
      #바라볼 방향 = tr, tc
      #바라볼 방향이 인덱스범위 내인지 체크
      if not(isWithinIndex(tr, tc)):
        #인덱스 범위 밖이면 이 도형은 폐기, tmp값 초기화
        tmp = base
        break
      tmp += a[tr][tc]
    else:
      #루프 정상적으로 마쳤다면, max넣어주고, 결과값 초기화
      maxSum = max(tmp, maxSum)
      tmp = base



for i in range(row):
  for j in range(col):
    dfs(i, j)
    func(i, j, a[i][j])

print(maxSum)