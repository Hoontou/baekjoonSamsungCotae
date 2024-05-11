#https://www.acmicpc.net/problem/14889
import sys
from itertools import combinations

sys.stdin = open('in.txt', 'r')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


#team1Entrys = list(combinations(range(1, n+1), n//2))
#연습삼아 순열만들기

combination = []
check = [0] * (n+1)
tmp = [0] * (n//2)

def dfs(deps, start):
  global n
  
  if deps == n//2 + 1:
    combination.append(tmp.copy())
    return

  for i in range(start, n+1):
    if check[i] == 1:
      continue
    check[i] = 1
    tmp[deps-1] = i
    dfs(deps+1, i+1)
    tmp[deps-1] = 0
    check[i] = 0

  
dfs(1, 1)
team1 = combination[:len(combination)//2]
team2 = combination[len(combination)//2:]
team2 = team2[::-1]

minDiff = 2147000000

#모든 엔트리 가능성을 돌면서
for i in range(len(team1)):
#i = 시너지 계산할 타겟 엔트리의 인덱스
#tmp = 해당회차의 시너지의 합
  tmp1 = 0
  tmp2 = 0

  #시너지 계산 시작
  for j in range(n//2): #j = 시너지 계산할 j번째 팀원
    #내 등번호
    myBackNum1 = team1[i][j]
    myBackNum2 = team2[i][j]
    for k in range(n//2):#k = 시너지 계산당할 나머지 팀원
      #시너지 계산당할 팀원의 등번호
      targetBackNum1 = team1[i][k]
      targetBackNum2 = team2[i][k]

      #시너지 리스트를 보고 등번호 -1에 해당하는,
      # 시너지 계산할 팀원과의 시너지를 더함
      tmp1 += a[myBackNum1-1][targetBackNum1-1]
      tmp2 += a[myBackNum2-1][targetBackNum2-1]
  #해당 타겟 엔트리의 시너지를 다 계산했음.
  #차이를 계산해서 최솟값에 넣음
  minDiff = min(minDiff, abs(tmp1-tmp2))

print(minDiff)

