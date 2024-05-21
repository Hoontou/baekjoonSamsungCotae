a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
plus = [3,0,1,6,4,2,7,8,5]

for i in range(9):
  print(a[i], end='')
  if i == 2 or i == 5 or i == 8:
    print()

tmp = a[::]
for i in range(9):
  a[i] = tmp[plus[i]]
  
for i in range(9):
  print(a[i], end='')
  if i == 2 or i == 5 or i == 8:
    print()