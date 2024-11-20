#Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.
year = int(input("Enter year"))
if year%4==0 or year%400==0:
    print("Leap  Year")
elif year%100!=0:
    print("Not leap year")
else:
    print("Not leap year")