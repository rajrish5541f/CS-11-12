def hcf(a,b):
    while b:
        a,b=b,a%b

    print(a)
hcf(14,35)
print(2%3)
print(3%2)