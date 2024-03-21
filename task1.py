#fibonacci generator

def fibonacci(n):
    a , b =0,1
    result = [ ] 
    for i in range(n):
        result.append(a)
        a, b =b, a+b
    return result
# generating the frist twenty numbers in the fibonacci series 
print(fibonacci(20))