age_str = input("Enter Your Age: ")
age = int(age_str)
if age <= 6:
    print("Bus is Free")
elif age <=12:
    print("Bus fare is 450 won")
elif age <=18:
    print("Bus fare is 720 won")
elif age<=64:
    print("Bus fare is 1200 won")
else:
    print("Bus is Free")
    
