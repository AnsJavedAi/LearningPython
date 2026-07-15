password=input("Enter your password: ")
point_digit=0
point_special_character=0
point_lower=0
point_upper=0
point_lenght=0
for char in password:
    if char.isupper():
        point_upper=1
    elif char.islower():
        point_lower=1
    elif char.isdigit():
        point_digit=1
    elif not char.isalpha():
        point_special_character=1
total_points=point_digit+point_lower+point_special_character+point_upper
if len(password)>=8:
    point_lenght=1
    total_points+=point_lenght
    if total_points==5:
        print("Strong Password")
    elif total_points>=3:
        print("Medium Password")
    else:
        print("Weak Password")
else:
    print("Weak Password! Lenght should be 8 or more")
    
    


    
    
    
