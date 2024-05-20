#https://www.acmicpc.net/problem/15686
import sys
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

#dfs의 최대뎁스를 m으로 해서, 
def dfs(list, deps):
  global m, minDis

  #최대 뎁스에 왔고
  if deps == m: 
    #상태트리가 꽉 채워졌으면
    if len(list) == m:
      #계산돌리고 min이면 갱신.
      minDis = min(minDis, calcDis(list))
    return

  #dfs 상태트리 만들기
  #이렇게 대충 조합 구해서 시간오류나는듯;
  for i in range(deps, len(chickens)):
    dfs(list+[i], deps+1)
    dfs(list+[], deps+1)
    
#살리기로 결정한 치킨집들로 도시의 치킨거리를 구해서 리턴
def calcDis(list):
  result = 0
  
  #모든 집을 돌면서
  for x, y in home:
    tmp = 2147000000
    for i in list: #i는 치킨집 인덱스
      #모든 치킨집을 돌면서 
      tx, ty = chickens[i]
      #치킨집 i과의 최소거리를 구해 도시의 치킨거리에 더함
      tmp = min(tmp, (abs(x-tx) + abs(y-ty)))
    result += tmp
  
  return result

dfs([], 0)

print(minDis)