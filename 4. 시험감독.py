#https://www.acmicpc.net/problem/13458

n = int(input())
b = list(map(int, input().split()))
main, sub = map(int, input().split())

result = 0

#한번 싹 돌면서 정감독관만큼 다뺌
result += len(b)
b = list(map(lambda x : x - main, b))
#뺐는데 음수나오면 0으로.
#b = list(map(lambda x : x if x >= 0 else 0, b))

for i in b:
  #0 or 음수면 패스
  if i <= 0:
    continue
  #나누고도 남는학생 있으면 +1
  if i % sub > 0:
    result += 1
  #몫을 더함
  result += i // sub

print(result)
