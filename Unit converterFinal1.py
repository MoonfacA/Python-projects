print("Unit conversion")
#variables setting
print("Which category would you like to convert?..enter option")
Category=input("(1)length: \n(2)Weight:\n")
print()
if Category==("1"):
    unit1=input("Which unit would you like to convert from?\n[mm, cm, m, km]:")
    unit2=input("Which unit would you like to conver to?\n[mm, cm, m, km]:")
    number=input("Enter your value:")
    #calculations1
    if unit1=="mm" and unit2=="cm":
     ans=float(number)/10
     print(ans, "cm")
    elif unit1=="cm" and unit2=="m":
     ans=float(number)/100
     print(ans, "m")
    elif unit1=="m" and unit2=="km":
     ans=float(number)/1000
     print(ans, "km")
    
    elif unit1=="km" and unit2=="m":
     ans=float(number)*1000
     print(ans, "m")
    elif unit1=="m" and unit2=="cm":
     ans=float(number)*100
     print(ans, "cm")
    elif unit1=="cm" and unit2=="mm":
     ans=float(number)*10
     print(ans, "mm")
    
elif Category==("2"):
    unit1=input("Which unit would you like to convert from?\n[mg, g, kg, pound]:")
    unit2=input("Which unit would you like to conver to?\n[mg, g, kg, pound]:")
    number=input("Enter your value:")
    #calculations2
    if unit1=="mg" and unit2=="g":
     ans=float(number)/1000
     print(ans, "g")
    elif unit1=="g" and unit2=="kg":
     ans=float(number)/1000
     print(ans, "kg")
    elif unit1=="kg" and unit2=="pound":
     ans=float(number)/2.20462
     print(ans, "pounds")
    
    elif unit1=="pounds" and unit2=="kg":
     ans=float(number)*2.20462
     print(ans, "kg")
    elif unit1=="kg" and unit2=="g":
     ans=float(number)*1000
     print(ans, "g")
    elif unit1=="g" and unit2=="mg":
     ans=float(number)*1000
     print(ans, "mg")
    
        