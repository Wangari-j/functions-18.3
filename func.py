#built in func

name = "Judy"
print("My name is" + name)

#higher order functions
def allNames(func, x, y):
    return func(x,y)

def add (a,b):
    return a + b

result = allNames(add, 4,9)

print(result)

