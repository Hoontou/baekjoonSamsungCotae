#https://www.acmicpc.net/problem/14501

import sys
sys.stdin = open('in.txt', 'r')

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
#print(li)
#li[index][0] -> 상담에 걸리는 일수
#li[index][1] -> 상담 비용

maxSum = -1

def dfs(start, sum):
  global maxSum
  if start >= n:
    maxSum = max(maxSum, sum)
    return
  
  #지금 수행할 상담 안하고 다음날로
  dfs(start+1, sum)
  
  #지금 수행할 상담이 퇴사일 이후에 끝나면 안함
  if start + li[start][0] > n:
    return
  #상담해도 퇴사일 안쪽이면 함.
  dfs(start + li[start][0], sum + li[start][1])
    
dfs(0, 0)
print(maxSum)