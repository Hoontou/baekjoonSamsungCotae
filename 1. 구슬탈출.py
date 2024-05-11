#https://www.acmicpc.net/problem/13460

#n 행, m열
n, m = map(int, input().split())
b = [list(input()) for _ in range(n)]

# 탈출구, R, B의 좌표담는 해시
hash = {}
for x in range(n):
  for y in range(m):
    if b[x][y] not in '#.':
      hash[b[x][y]] = (x,y)
      
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = []

def dfs(xyR, xyB, time):
  global n, m
  if time == 11:
    return
  else:
    for i in range(4):
      
      #기울인다.
      tR, tB = moveBall(xyR[0], xyR[1], xyB[0], xyB[1], i)
      
      #기울였는데 움직임이 없으면 패스
      if xyR == tR and xyB == tB:
        continue
      
      #이제 한방향으로 움직였고, 종료조건 체크
      #B가 O좌표면 현재 방향 탐색은 실패, 이 조건이 위에 와야함
      #B가 탈출했거나, RB가 동시에 탈출하는거 모두 걸러질듯?
      
      if tB == hash['O']:
        continue
      
      
      #R가 O좌표면 result에 현재 time 기록
      if tR == hash['O']:
        result.append(time)
        return
        #이 이후로  dfs를 호출하는건 의미가 없을듯, 
        #최소 time을 찾는거니까 바로 return
      
      #R, B가 한번 움직였는데도 여전히 탈출못했다면 dfs호출
      dfs(tR, tB, time+1)
      

def moveBall(txR, tyR, txB, tyB, i):
  moveCountR = 0
  moveCountB = 0
  #벽이 아니면 앞으로 가고, 탈출구 나왔으면 break
  while b[txR + dx[i]][tyR + dy[i]] != '#':
    txR += dx[i]
    tyR += dy[i]
    moveCountR += 1
    if b[txR][tyR] == 'O': 
      break
  while b[txB + dx[i]][tyB + dy[i]] != '#':
    txB += dx[i]
    tyB += dy[i]
    moveCountB += 1
    if b[txB][tyB] == 'O':
      break
  
  if (txR, tyR) == (txB, tyB) and b[txR][tyR] != 'O':
    #좌표가 겹치는 이유가 구멍이 아니라면
    #늦게도착한 애를 한칸뒤로 보냄
    if moveCountR > moveCountB:
      txR -= dx[i]
      tyR -= dy[i]
    else:
      txB -= dx[i]
      tyB -= dy[i]
  return (txR, tyR), (txB, tyB)
    
  
dfs(hash['R'], hash['B'], 1)

print(-1 if len(result) == 0 else min(result))