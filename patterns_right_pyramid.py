nrows=int(input("enter a number: "))

for row in range(1, nrows+1) :
  for col in range(1, row) :
    print('*', end = '')
  print(" ")

for row in range(nrows-1, 0, -1):
  for col in range(1, row):
    print('*', end='')
  print()
