x="first number"
x=(int)
y="second number"
y=(int)
operator=("+,-,*,/,^,%")
def calculate(x,y,operator):

    if operator=="+":
        return x+y
    elif operator=="-":
        return x-y
    elif operator=="*":
        return x*y
    elif operator=="/":
        if y!=0:
                return x/y
        else:
                return"cannot divide by zero"
    elif operator=="^":
        return x**y
    elif operator=="%":
        if y==0:
            return"denominator can not be zero"
        return (x/y)*100
    elif x<5:
        return"Duh calculation too easy!"
class text:    
  BOLD_START='\033[1m'
  BOLD_END='\033[0m'
  GREEN='\033[92m'

print(text.BOLD_START+"Welcome to our Pythornny calculator!"+text.BOLD_END+'\033[92m')
print()
print("*Do you have some calculations in mind?*")
print()

x=float(input('enter first number:'))
operator=input('enter operator(+,-,*,/,^,%):')
y=float(input('enter second number:'))

print(x,operator,y)
result=calculate(x,y,operator)
print('=',result)
    
continue_calculating= (True)

while continue_calculating is True:
    x=float(input('enter first number:'))
    operator=input('enter operator(+,-,*,/,^,%):')
    y=float(input('enter second number:'))

    print(x,operator,y)
    result=calculate(x,y,operator)
    print('=',result)    

