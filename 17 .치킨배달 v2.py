#https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations
sys.stdin = open('in.txt', 'r')

n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
minDis = 2147000000
chickens = []
home = []

#1은 집, 2는 치킨
for i in range(n):
  for j in range(n):
    if b[i][j] == 1:
      home.append((i, j))
    if b[i][j] == 2:
      chickens.append((i, j))

#살리기로 결정한 치킨집들로 도시의 치킨거리를 구해서 리턴
def calcDis(list):
  result = 0
  
  #모든 집을 돌면서
  for x, y in home:
    tmp = 2147000000
    for tx, ty in list: #i는 치킨집 인덱스
      #모든 치킨집을 돌면서 
      #치킨집 i과의 최소거리를 구해 도시의 치킨거리에 더함
      tmp = min(tmp, (abs(x-tx) + abs(y-ty)))
    result += tmp
  
  return result

combi = list(combinations(chickens, m))
for i in combi:
  minDis = min(minDis, calcDis(i))
  
print(minDis)

#그냥 조합을 대충 구해서 시간오류났음
#그냥 이터툴 써서 하니까 바로통과.