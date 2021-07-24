#string slicing
var = "HELLO WORLD ! "
print(len(var))
print(var.strip())
print(var.title())
print(var.upper())
print(var.lower())
# very very case sensitive 
print(var.replace("HELLO","HI"))
print(var.find("o"))

#to find a word in a string
# it takes the var in boolean
# it is also case sensitive

x = "WORLD" in var
print(x)

#if i print world instead of WORLD it would show error
y = "world" in var
print(y)
