#lambda arguments:expressions

add10 = lambda x: x+10
print(add10(10))

def addResult10(x):
    return x+10

# result = addResult10(50)
result = lambda x: x+10
print(result(50))

multiply = lambda x, y : x*y
print(multiply(5, 10))

# map(func, seq)
a = [2, 4, 6, 8, 10]
# res = map(lambda x: x*2, a)
res = [x*2 for x in a]
print(list(res))