import shapes
import math

def calculate_factorial():
    try:
        fact = int(input("Enter a number: "))
        print(f"The Factorial of {fact} is: {math.factorial(fact)}")
        math.factorial(fact)
    except ValueError:
        print("enter onlu number!!")

def compund_in(principal,rate,time):
    try:
        amount = principal *math.pow((1+rate/(100)),time)
        a  = amount - principal
        return a
    except ValueError:
        print("enter only number!!")

def trigonometric():
    try:
        degree = float(input("Enter angle in degrees: "))
        angle_degree_to_radians = math.radians(degree)

        sin = math.sin(angle_degree_to_radians)
        cos = math.cos(angle_degree_to_radians)
        tan = math.tan(angle_degree_to_radians)
        
        print(f"sin({degree}) = {sin:.4f}")
        print(f"cos({degree}) = {cos:.4f}")
        print(f"tan({degree}) = {tan:.4f}")
    except ValueError:
        print("enter degrees in number between 0 to 360!!")

# while True:
#     print("""
# 1. calaculate factorial
# 2. Solve Compound Intrest
# 3. Trigonometric Calculations
# 4. Area of Geometric Shapes
# 5. Back to Main Menu""")
    
#     choice = input("Enter your Choice: ")

#     match choice:
#         case '1':
#             calculate_factorial()
#             print("="*30)
#         case '2':
            
#             p = float(input("Enter principle amount: "))  
#             r = float(input("Enter rate of intres (in%): "))  
#             t = float(input("Enter time (in years): "))
#             a = compund_in(p,r,t)
#             print(f"Compound Interest = {a:.2f}")
#             print("="*30)

#         case '3':
#             trigonometric()
#             print("="*30)

#         case '4':
#             print("""
# Choose shape:
# 1. Square
# 2. Rectangle
# 3. Triangle
# 4. Circle
# """)
#             shape_choice = input("Enter shape number: ")

#             match shape_choice:
#                 case '1':
#                     side = float(input("Enter side of square for area of circle: "))
#                     print("Area:", shapes.square(side))

#                 case '2':
#                     l = float(input("Enter length: "))
#                     b = float(input("Enter breadth: "))
#                     print("Area:", shapes.rectangle(l, b))

#                 case '3':
#                     l = float(input("Enter base: "))
#                     w = float(input("Enter height: "))
#                     print("Area:", shapes.triangle(l, w))

#                 case '4':
#                     r = float(input("Enter radius: "))
#                     print("Area:", shapes.circle(r))
                    
#             print("="*30)

#         case '5':
#             print("going to the main program..")
#             break


            


        
