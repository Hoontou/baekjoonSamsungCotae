#https://www.acmicpc.net/problem/12100

n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]

result = set() #dfs 끝칸의 최댓값들이 모인다.

def move(i, tmpB):
  global n
  if i == 0: #우
    for x in range(n):
      for p in range(1, n):
        for q in range(p):
          #맨 오른쪽-1 칸 부터 보면서,
          if tmpB[x][q] == 0:
            #내 오른쪽 칸이 비었으면, 서로 바꿔치기
            tmpB[x][q], tmpB[x][p] = tmpB[x][p], 0
  if i == 1: #좌
    for x in range(n):
      for p in range(n-2, -1, -1):
        for q in range(n-1, p, -1):
          if tmpB[x][q] == 0:
            tmpB[x][q], tmpB[x][p] = tmpB[x][p], 0
  if i == 2: #상
    for x in range(n):
      for p in range(1, n):
        for q in range(p):
          if tmpB[q][x] == 0:
            tmpB[q][x], tmpB[p][x] = tmpB[p][x], 0
  if i == 3: #하
    for x in range(n):
      for p in range(n-2, -1, -1):
        for q in range(n-1, p, -1):
          if tmpB[q][x] == 0:
            tmpB[q][x], tmpB[p][x] = tmpB[p][x], 0

def add(i, tmpB):
  global n
  if i == 0: #우
    for x in range(n):
      for p in range(1, n):
        #맨 오른쪽칸-1 부터 보면서,
        if tmpB[x][p-1] == tmpB[x][p]:
          #내 오른쪽 칸이랑 내가 똑같으면 더하고 0으로만든다
          tmpB[x][p-1], tmpB[x][p] = tmpB[x][p]*2, 0
  if i == 1: #좌
    for x in range(n):
      for p in range(n-2, -1, -1):
        if tmpB[x][p+1] == tmpB[x][p]:
          tmpB[x][p+1], tmpB[x][p] = tmpB[x][p]*2, 0
  if i == 2: #상
    for x in range(n):
      for p in range(1, n):
        if tmpB[p-1][x] == tmpB[p][x]:
          tmpB[p-1][x], tmpB[p][x] = tmpB[p][x]*2, 0
  if i == 3: #하
    for x in range(n):
      for p in range(n-2, -1, -1):
        if tmpB[p+1][x] == tmpB[p][x]:
          tmpB[p+1][x], tmpB[p][x] = tmpB[p][x]*2, 0

def dfs(deep, tmpB):
  if deep == 5:
    a = 0
    for i in tmpB:
      a = max(max(i), a)
      result.add(a)
    return
  
  else:
    for i in range(4):
      #매회마다 복사본 생성
      tmp = [t[:] for t in tmpB]
      #복사본을 수정해서
      move(i, tmp) #한쪽으로 밀고
      add(i, tmp) #같은수 합치고
      move(i, tmp) #또 한쪽으로 민다.
      #넘긴다
      dfs(deep+1, tmp)

dfs(0, b)
print(max(result))