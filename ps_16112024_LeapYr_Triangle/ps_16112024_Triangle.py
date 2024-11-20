side1 = int(input("Enter side1 of the triangle"))
side2 = int(input("Enter side2 of the triangle"))
side3 = int(input("Enter side3 of the triangle"))

if(side1==side2 and side2==side3 and side1==side3):
    print("Equillateral")
elif(side1==side2 and side2!=side3 and side1!=side3):
    print("Isosceles ")
elif (side1 != side2 and side2 != side3 and side1!= side3):
    print("Scalen ")