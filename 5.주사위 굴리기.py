#https://www.acmicpc.net/problem/14499

n, m, x, y, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
moveList = map(int, input().split())
#front, behind, up, down, left, right
dice = {'f': 0, 'b': 0, 'u': 0, 'd': 0, 'l': 0, 'r': 0}

def roll(i):
  if i == 1:
    #동
    dice['u'], dice['d'], dice['l'], dice['r'] = dice['l'], dice['r'], dice['d'], dice['u']
  if i == 2:
    #서
    dice['u'], dice['d'], dice['l'], dice['r'] = dice['r'], dice['l'], dice['u'], dice['d']
  if i == 3:
    #남
    dice['f'], dice['b'], dice['u'], dice['d'] = dice['d'], dice['u'], dice['f'], dice['b']
  if i == 4:
    #북
    dice['f'], dice['b'], dice['u'], dice['d'] = dice['u'], dice['d'], dice['b'], dice['f']
    
def move(x, y, i):
  global n, m
  if i == 1:
    tx = x
    ty = y + 1
  if i == 2:
    tx = x
    ty = y - 1
  if i == 3:
    tx = x - 1
    ty = y
  if i == 4:
    tx = x + 1
    ty = y
    
  if not (0<=tx<=n-1 and 0<=ty<=m-1):
    #범위초과면 원본 리턴
    return x, y
  
  return tx, ty

for i in moveList:
  tx, ty = move(x, y, i)
  if tx == x and ty == y:
    #움직일수 없다면,
    continue #패스
  
  #움직일 수 있다면,
  roll(i) #굴린다.
  x, y = tx, ty #움직인다.
    
  if b[x][y] == 0:
    #움직인칸 비었으면
    b[x][y] = dice['d']
  else:
    #칸에 뭐 차있으면
    dice['d'] = b[x][y]
    ## +++추가, 칸에 쓰여있는 수는 0이 된다.
    b[x][y] = 0
    

  print(dice['u'])