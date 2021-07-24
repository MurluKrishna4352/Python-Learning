# set

set_0 = {5 , "apple" , 10 , "mango" , "orange"}

for i in set_0:
    print("i   :      " , i)

print("apple" in set_0) # one argument
print("1" in set_0) # one argument

set_1 = {"apple" , "mango" , 1 , 2 , 3}
set_0.update(set_1)
print(set_0)

set_0.add(1132)
print(set_0)
print(len(set_0))

set_0.remove("apple")
print(set_0)

set_0.pop()
print("pop :    " , set_0)

set_0.discard(1)
print("discard :    " , set_0)
