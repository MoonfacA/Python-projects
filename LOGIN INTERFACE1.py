import hashlib#Used to hash data into cryptic bytes
def Signup():#Defining the sign up function
 Email=input("Enter email address:")
 Password=input("Enter password:")
 Confirm_password=input("Confirm password:")
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