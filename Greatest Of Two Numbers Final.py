class text:    
  BOLD_START='\033[1m'
  BOLD_END='\033[0m'
  YELLOW='\033[1;33;40m'

print('\033[1;33;40m'+text.BOLD_START+"Welcome I'm your bot CAM!"+text.BOLD_END+'\033[1;33;40m')
print()
print("*Do you have a list of items you want sorted?*")
print()

a=int(input("Enter the first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a>b:
    if a>c:
        print("The greatest number is",a)
    else:
        print("The greates number is",c)
else:
    if b>c:
        print("The greatest number is",b)
    else:
        print("The greatest number is",c)
print()
print()

continue_comparing= (True)
while continue_comparing is True:
 a=int(input("Enter the first number:"))
 b=int(input("Enter second number:"))
 c=int(input("Enter third number:"))

if a>b:
    if a>c:
        print("The greatest number is",a)
    else:
        print("The greates number is",c)
else:
    if b>c:
        print("The greatest number is",b)
    else:
        print("The greatest number is",c)