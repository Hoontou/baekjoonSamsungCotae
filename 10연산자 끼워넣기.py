#https://www.acmicpc.net/problem/14888
import sys
sys.stdin = open('in.txt', 'r')

n = int(input())

#수열 a
a = list(map(int, input().split()))
#연산자 갯수 b
b = list(map(int, input().split()))
# 0: +, 1: -, 2: *, 3: //

mx = -2147000000
mn = 2147000000

def calc(num1, num2, type):
  if type == 0:
    return num1 + num2
  if type == 1:
    return num1 - num2
  if type == 2:
    return num1 * num2
  if type == 3:
    if num1 < 0:
      return -(abs(num1) // num2)
    else:
      return num1 // num2

def dfs(result, deps = 0):
  global mx, mn

  #식의 끝에 도달
  if deps == n:
    mx = max(mx, result)
    mn = min(mn, result)
    return
  
  #연산자 dfs로 순회
  for i in range(4):
    if b[i] == 0:
      #연산자가 남은게 없으면 패스
      continue

    #첫회차면 그냥 첫숫자 넘김
    if deps == 0:
      dfs(a[deps], deps+1)
      continue
    #연산자 남은게 있으면 하나 씀
    b[i] -= 1
    dfs(calc(result, a[deps], i), deps+1)
    b[i] += 1

    #해당 for회차 나갈때 되돌려놓고 나감
    
    
dfs(0)

print(mx)
print(mn)
