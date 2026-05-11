name = input("Enter your Name: ")
s_name= input("Enter your Sir Name: ")
age = int(input("Enter your Current Age: "))
field= input("Which Learning Field you Belong: ")

print("----Your Detail-----")
print("Your First Name: ",name)
print("Your Sir Name: ",s_name)
print("Full Name: ", name + "" ,s_name)
print("Your Age: ",age)
print("Learning Field: ",field)


num1 = int(input("Enter value of number 1: "))
num2 = int(input("Enter value of number 2: "))
print("Addition:",num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division: ", num1 / num2)

print("Choose the Mathematical Operator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice= int(input("Enter your Choice: "))

num1 = int(input("Enter value of number 1: "))
num2 = int(input("Enter value of number 2: "))

if choice == 1:
    print("Addition:",num1 + num2)
elif choice == 2:
    print("Subtraction:", num1 - num2)
elif choice == 3:
    print("Multiplication:", num1 * num2)
elif choice == 4:
    if num2 == 0:
        print("Number is not Divisible By Zero")
    else:
        print("Division: ", num1 / num2)
else:
    print("Invalid Choice")

length= float(input("Enter value of Length: "))
breadth= float(input("Enter value of Breadth: "))
area = length * breadth
print("Area of Length: ",area)

side = float(input("Enter value of side: "))
area= side * side
print("Area of Square: ",area)


base= float(input("Enter value of Base: "))
height= float(input("Enter value of Height: "))
area= 0.5 * (base * height)
print("Area of Triangle: ",area)


num = int(input("Enter value of num:"))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

num = int(input("Enter value of num: "))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")