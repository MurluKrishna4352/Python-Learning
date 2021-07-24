# break and continue function
for i in range(1 , 20):
     if(i == 15):
          break
     elif (i % 2 == 0):
          continue 
     print(i)
     
# same program using while
i = 0
while i <= 20:
     i += 1
     if(i ==15):
          break
     elif (i % 2 == 0):
          continue 
     print(i)
     
     
