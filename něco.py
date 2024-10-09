def f1(a,b,c=0):
    return a+b*c

result = f1(10,4,5)
result2 = f1(10,4)
result3 = f1(b=4,a=10)
print(result,result2,result3)