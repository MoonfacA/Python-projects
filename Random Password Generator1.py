import random#random imported to generate random characters expanded on below

#ASCII code(Askee) is used, it is a system with english characters assigned numbers(0-127), has expanded version
#Order and characters used, ch(77) returns M, ord("M") returns 77
#ASCII uppercase characters range from 65-90, see cheat sheet for others
#These can all be grouped and subdivided under the string module
import string#Has the following categories
#string.ascii_letters
#string.ascii_lowercase
#string.ascii_uppercase
#string.digits
#string.punctuation
print("WELCOME TO OUR PASSWORD GENERATOR")
print()
length=int(input("Enter length of your required password:"))

#Data defination
lower= string.ascii_lowercase
upper= string.ascii_uppercase
numbers= string.digits
symbols= string.punctuation
#combining defined data
all=lower+upper+numbers+symbols
#Temporary variable used to store all function(combination of upper,lower, numbers and symbols)
temp=random.sample(all,length)
#sample function allows for random sampling from a defined data set with length specification

if length>4:
    print("Characters used:")
    print(temp)
    print()
#Create password by joining characters
    Password="".join(temp)
    print("Password:")
    
    print(Password)
elif length==0:
 print()
 print("Password can't have zero digits")
elif length<4:
    print()
    print("Password too short")


Password_GENERATED= (True)
while Password_GENERATED is True:
    print()
    length=int(input("Enter length of your required password:"))
#Data defination
    lower= string.ascii_lowercase
    upper= string.ascii_uppercase
    numbers= string.digits
    symbols= string.punctuation
#combining defined data
    all=lower+upper+numbers+symbols
#Temporary variable used to store all function(combination of upper,lower, numbers and symbols)
    temp=random.sample(all,length)
#sample function allows for random sampling from a defined data set with length specification
    if length>4:
     print("Characters used:")
     print(temp)
     print()
#Create password by joining characters
     Password="".join(temp)
     print("Password:")
    
     print(Password)
    elif length==0:
     print()
     print("Password can't have zero digits")
    elif length<4:
     print()
     print("Password too short")
