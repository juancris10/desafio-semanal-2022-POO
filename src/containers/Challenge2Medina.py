

def fnfibo(num):
    a= 0
    b= 1
    for i in range(num):
        c= a+b 
        a= b
        b = c
    return b

for i in range(50):
    print(fnfibo(i))
