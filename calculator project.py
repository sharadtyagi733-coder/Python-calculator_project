# functions for operations
# user input
# print result

# add
def add(num1,num2):
    return(num1+num2)
# subtreact
def sub(num1,num2):
    return(num1-num2)
# multiply
def mul(num1,num2):
    return(num1*num2)    
# divide    
def div(num1,num2):
    return(num1/num2) 
# avg 
def avg(num1,num2):
    return(num1+num2)/2    

 #   step 2  user input
print("please select a operation:\n" \
    "1.additon:\n"\
    "2.subtraction:\n"\
    "3.multiplication:\n"\
    "4.divison:\n"\
    "5.average:\n")   
select=int(input("select a operation from 1,2,3,4,5:"))

number1=int(input("enter first number:"))
number2=int(input("enter first number:"))

# step 3 print result
if select==1:
    print(number1, "+", number2, "=" , \
        add(number1,number2))
if select==2:
    print(number1, "-", number2, "=" , \
        sub(number1,number2))
if select==3:
    print(number1, "*", number2, "=" , \
        mul(number1,number2))        
if select==4:
    print(number1, "/", number2, "=" , \
        div(number1,number2)) 
if select==5:
    print("(",number1, "+", number2,")","/","2", "=" , \
        avg(number1,number2))  
else:
    print("invalid operatiin exit")              