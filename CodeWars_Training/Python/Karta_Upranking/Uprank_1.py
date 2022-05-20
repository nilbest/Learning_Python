import math

def square_digits(num):
    x = [int(a) for a in str(num)]
    for i in range(0, len(x)):
        x[i]=x[i]*x[i]
    y=[str(integer) for integer in x]
    a_string= "".join(y)
    num=int(a_string)
    return num

print(square_digits(258))
print("Test")