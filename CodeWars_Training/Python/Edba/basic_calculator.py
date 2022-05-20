def calculator(num1, operator, num2):
    output = None
    if num2 != 0 or operator != "/":
        output=eval(f"{num1} {operator} {num2}")
        return int(output)
    else:
        return "Can't divide by 0!"
     
     
#def calculator(num1, operator, num2):
#    output = None
#    if num2 != 0 or operator != "/":
#       input="{}{}{}".format(num1,operator,num2)
#        output=eval(input)
#        return output
#    else:
#        return "Can't divide by 0!"

 
def test(testnum,num):
    print(f"Test Nummer:{testnum} = {num}")
    

def main():
    test(calculator(2, '/', 2),1)
    test(calculator(10, '-', 7),3)    
    test(calculator(2, '*', 16),32)    
    test(calculator(2, '-', 2),0)   
    test(calculator(15, '+', 26),41)   
    test(calculator(2, "/", 0), "Can't divide by 0!")
    
if __name__ == "__main__":
    main()