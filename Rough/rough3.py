y = "x^2"
y = y.replace('x', "(1)")
print(y, type(y), (1)^2)
q = eval(y)
print(eval(y), eval("(1)^2"), float(2)^2)
print(q)

