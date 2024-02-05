class text:    
  BOLD_START='\033[1m'
  BOLD_END='\033[0m'
  RED='\033[0;31m'

print(text.BOLD_START+"Welcome I'm your bot CAM!"+text.BOLD_END+'\033[0;31m')
print()
print("*Do you have a list of items you want sorted?*")
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

prime_numbers = [number1,number2,number3,number4,number5]
prime_numbers.sort()
print("Sorted list")
print(prime_numbers)

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
    number1=int(number1)
    number2=int(number2)
    number3=int(number3)
    number4=int(number4)
    number5=int(number5)
    print()
    prime_numbers = [number1,number2,number3,number4,number5]
    prime_numbers.sort()
    print("Sorted list")
    print(prime_numbers)
    
