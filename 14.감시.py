#https://www.acmicpc.net/problem/15683

import sys
import copy

sys.stdin = open('in.txt', 'r')

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

cctv1 = [[0], [1], [2], [3]]
cctv2 = [[0, 2], [1, 3]]
cctv3 = [[0, 1], [1, 2], [2, 3], [3, 0]]
cctv4 = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
cctv5 = [[0, 1, 2, 3]]
cctvs = [[], cctv1, cctv2, cctv3, cctv4, cctv5]

dx = [0, 1 ,0 ,-1]
dy = [1, 0 ,-1, 0]


def getCctvLocation(arr):
  location = []
  for (indexX, i) in enumerate(arr):
    for (indexY, j) in enumerate(i):
      if 0 < j < 6:
        location.append((indexX, indexY, j))
  return location

def getCannotWatchZoneNum(arr):
  count = 0
  for (indexX, i) in enumerate(arr):
    for (indexY, j) in enumerate(i):
      if j == 0:
        count += 1
  return count

def watchRoom(arr, x, y, direct):
  tx = x+dx[direct]
  ty = y+dy[direct]
  while 0<=tx<n and 0<=ty<m :
    if arr[tx][ty] == 6:
      break
    
    if arr[tx][ty] == 0:
      arr[tx][ty] = "#"
    tx = tx+dx[direct]
    ty = ty+dy[direct]
  return
  
#(x, y, cctv타입)[]
location = getCctvLocation(a)
#cctv의 방향
cctvState = [0] * len(location)

minBlackZone = 2147000000
def dfs(deps):
  global minBlackZone
  if deps == len(location):
    #state돌면서 watch처리
    tmp = copy.deepcopy(a)
    for (index, i) in enumerate(cctvState):
      #location에 들어있는 index번째의 cctv는 i방향을 보고있음.
      #location을 보고 index번째의 cctv타입과 위치를 가져와서
      #watchRoom 함수로 watch처리.
      x, y, type = location[index]
      for j in cctvs[type][i]:
        #j는 cctv가 보고있는 방향에서 감시할수 있는 방향들
        watchRoom(tmp, x, y, j)
        #cctv가 감시할수 있는 방향을 싹다 '#'으로 바꿈
    minBlackZone = min(minBlackZone, getCannotWatchZoneNum(tmp))
    return
  
  targetCctvType = location[deps][2]
  #cctvState에 cctc가 어딜 보고있는지 체크할거임.
  for i in range(len(cctvs[targetCctvType])):
    cctvState[deps] = i
    dfs(deps+1)

dfs(0)
print(minBlackZone)



