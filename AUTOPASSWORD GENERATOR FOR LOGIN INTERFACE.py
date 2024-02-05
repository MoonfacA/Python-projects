import hashlib#Used to hash data into cryptic bytes
import random#random imported to generate random characters expanded on below
import string#Has the following categories
#string.ascii_letters
#string.ascii_lowercase
#string.ascii_uppercase
#string.digits
#string.punctuation
def Signup():#Defining the sign up function
 Email=input("Enter email address:")
 Password=int(input("Enter length of your required password:"))
 length=Password
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
    print("Your password is:")
    print(Password)
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



 
 Confirm_password=input("Copy and confirm password:")
 if Password==Confirm_password:
    enc=Confirm_password.encode()#Encode function used to create a new document with the password
    hash1=hashlib.md5(enc).hexdigest()#Password is hashed into a cryptic form
    with open("credentials.txt","w") as f:#New document named and used to store data#email and hashed password under given conditions
        f.write(Email+"\n")
        f.write(hash1)
        f.close()
        print("You have successfully registered!")
 else:
     print("Password is not the same as above")
def Login():
    Email=input("Enter email:")
    Password=input("Enter password:")
    Authentication=Password.encode()
    Authentication_hash=hashlib.md5(Authentication).hexdigest()
    with open("credentials.txt","r") as f:
         stored_Email,stored_Password=f.read().split("\n")
         f.close()
         if Email==stored_Email:
          if Authentication_hash==stored_Password:
                 print("Logged in successfully")
         else:
             print ("login failled")
("\n")
while 1:
    print("**********Login System**********")
    print("1.signup")
    print("2.Login")
    print("3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        Signup()
    elif ch==2:
        Login()
    elif ch==3:
        break
    else:
        print("Wrong Choice")
