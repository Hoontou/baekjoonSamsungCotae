#https://www.acmicpc.net/problem/14890
import sys
sys.stdin = open('in.txt', 'r')

n, L =  map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

count = 0

#한 라인 쭉 밀면서
def func(road):
  global count
  hill = [0]*n
  current = 0

#while 현재 칸 < n
  while current != n-1:
#맨 첫칸에 섰다.
    currentH = road[current]
#다음칸을 바라본다.
    nxt = current + 1
    nextH = road[nxt]
#1. 층이 같애. 갈수있어. 그럼가.
    if currentH == nextH:
      current += 1
      continue

#3. 칸 차이가 2칸이상이야. 못가.
    if abs(currentH - nextH) >= 2:
      break
    
#2. 층이 달라. 못가. 근데 차이가 한칸이야. 경사로가 필요해.
#앞에 놓인 L의 길이 만큼의 칸이 내 칸의 높이 +-1인지.
    if abs(currentH - nextH) == 1:
      
      #내가높은거야? 앞이 높은거야?
      if currentH > nextH:
        for j in range(1,L):
          #경사로 놓을려고 체크하는데 인덱스 초과나면 break
          if nxt+j >= n:
            break

          #거기 경사로 있어?
          if hill[nxt+j] == 1:
            break

          tmpH = road[nxt+j]
          #경사로 놓을려고 체크하는 와중에 높이가 달라지면 break
          if nextH != tmpH:
            break
        else:
        #경사로를 제대로 놓을 수 있어?
        #그럼 경사로 놓고 L만큼 전진해.
          for k in range(L):
            hill[nxt+k] = 1
          current += L
          continue
              
      else:
        #내칸에 경사로 있어?
        if hill[current] == 1:
          break

        #내 뒤가 L길이 만큼 나랑 같은지 체크해.
        for q in range(1,L):
          before = current - q
          #인덱스 오버 체크해
          if before < 0:
            break

          #거기 경사로 있어?
          if hill[before] == 1:
            break

          tmpH = road[before]
          if currentH != tmpH:
            break
        else:
        #뒤에경사로를 제대로 놓을 수 있어?
        #그럼 경사로 놓고 한칸 전진해.
          for k in range(L):
            hill[current-k] = 1
          current += 1
          continue

      #경사로를 제대로 못놓아. 
      #놓을 수 있으면 continue로 빠져나가게했어. 이까지 못와.
      break
    else:
      break
  else:
  #무사히 마지막 까지 건너왔어.
    #print(road)
    count += 1

#횡으로 확인하고 종으로도 확인하고
for i in range(n):
  func(a[i])

for i in range(n):
  func([a[j][i] for j in range(n)])

print(count)

#더러운 탐색. 다시풀고싶지 않은 문제.
#경사로를 겹쳐서 놓으면 안된다고 해서,
#당연하게 가로세로 겹치면 안된다고 생각하고 구현중이었는데
#도저히 결과 안나와서 찾아보니깐 같은방향으로만 안겹치면 됨.
#애초에 설명글 부터 뒤지게 안읽힘. 그냥 문제가 더럽다.
#탐색이 더러우니까 변수화 할 수 있는건 변수화 해서 써라.
#i+1같이 쓰면 눈 핑핑 돌아감.