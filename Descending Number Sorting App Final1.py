class text:    
  BOLD_START='\033[1m'
  BOLD_END='\033[0m'
  white='\033[1;37;40m'

print('\033[1;37;40m'+text.BOLD_START+"WELCOME"+text.BOLD_END+'\033[1;37;40m')

print()
print('\033[1;37;40m'+text.BOLD_START+"I'm your bot R, here to assist you"+text.BOLD_END+'\033[1;37;40m')
print()
print("*Do you have a list of numbers you want sorted?*")
print()

number1=float(input('enter first number:'))
number2=float(input('enter second number:'))
number3=float(input('enter third number:'))
number4=float(input('enter forth number:'))
number5=float(input('enter fifth number:'))

print()
print(number1,number2,number3,number4,number5)
print()
number1=int(number1)
number2=int(number2)
number3=int(number3)
number4=int(number4)
number5=int(number5)
print()           
prime_number = [number1,number2,number3,number4,number5]
prime_number.sort()
prime_number.reverse()
print("Sorted descending list")
print(prime_number)


print()
continue_sorting= (True)
while continue_sorting is True:
    number1=float(input('enter first number:'))
    number2=float(input('enter second number:'))
    number3=float(input('enter third number:'))
    number4=float(input('enter forth number:'))
    number5=float(input('enter fifth number:'))

    print()
    print(number1,number2,number3,number4,number5)
    print()
    print()
    number1=int(number1)
    number2=int(number2)
    number3=int(number3)
    number4=int(number4)
    number5=int(number5)
    print()
        
    prime_number = [number1,number2,number3,number4,number5]
    prime_number.sort()
    prime_number.reverse()
    
    print("Sorted descending list")
    print(prime_number)
 

    

