print("Welcome to the NumPy Analyzer!")
print("This tool will help you analyze and manipulate NumPy arrays.")
import numpy as np

class array_tool:
    def __init__(self):
        self.arr = None

    def create_array(self):
        try:
            r = int(input("enter a array: "))
            elements = input(f"Enter {r} numbers separated by spaces: ").split()
            elements = [int(x) for x in elements ]
            self.arr = np.array(elements)
            print("="*20)
            print("Array created successfully!")
            print(self.arr)
            print("="*20)
        except:
            print("Enter array in space format use space in this")
            

    def d2_array(self):
            try:
                a = int(input("enter row number: "))
                b = int(input("enter column number: "))
                total = a*b

                elements = input(f"enter elements in {total} format: ").split()
                elements = [int(x) for x in elements]

                if len(elements)!=total:
                    print("enter proper elements")
                else:

                    arr = np.array(elements).reshape(a,b)
                    print("="*20)
                    print("your 2d array:")
                    print(arr)
                    print("="*20)
            except ValueError:
                print("Please enter valid number!!")

    def d3_array(self):
        try:
            a = int(input("Enter box number to store array: "))
            b = int(input("Enter row number: "))
            c = int(input("enter column number: "))
            total = a*b*c
            elements = input(f"Enter {total} elements in space separate: ").split()
            elements = [int(i) for i in elements]

            if len(elements)!=total:
                print(f"Enter total {total}!!")
            else:
                arr = np.array(elements).reshape(a,b,c)
            
            print("="*20)
            print(f"Your 3D array: ")
            print(f"{arr}")
            print("="*20)
        except ValueError:
                print("Please enter valid number!!")

    def arr1(self):
        try:
            x = int(input("Enter rows for the first array: "))
            y = int(input("Enter columns for the first array: "))
            total = x * y

            elements = input(f"Enter {total} numbers separated by space: ").split()

            if len(elements) != total:
                print(f"Please enter exactly {total} numbers!")
                return None

            # Try to convert each element to int and catch any conversion errors
            try:
                elements = [int(i) for i in elements]
            except ValueError:
                print("Enter numbers only! No letters or special characters allowed.")
                return None

            arr = np.array(elements).reshape(x, y)
            print("Original array:")
            print(arr)
            return arr

        except ValueError:
            print("Enter valid numeric values for rows and columns!")
            return None

            

    def arr2(self):
        try:    
            a = int(input("enter rows for second array: "))
            b = int(input("enteer columns for second array: "))
            suree = a*b

            elementss = input(f"Enter {suree} numbers: ").split()
            elementss = [int(j) for j in elementss]

            if len(elementss)!=suree:
                print("enter in proper format in",{suree})
            
            arrr = np.array(elementss).reshape(a,b)
            print("Second array: ")
            print(arrr)
            return arrr
        except:
            print("please enter valid numbers!!")
            return None
        

tool = array_tool()

print("=" * 30)
print("Choose an Option")
while True:
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or split Arrays")
    print("4. Search, sort, or Filter Arrays")
    print("5. Copute Aggregates and Statistics")
    print("6. Exit")
    choice = input("Enter Your Choice: ")
    match choice:
        case '1':
           print("Select the type of array to create")
           while True:
               print("1. 1d array")
               print("2. 2d array")
               print("3. 3d array")
               print("4. exit")
               choice2 = input("Enter your coice: ")
               match choice2:
                    case '1':
                        tool.create_array()
                    case '2':
                       tool.d2_array()
                    case '3':
                       tool.d3_array()
                    case '4':
                       print("Going back to the main menu!")
                       break
                    case _:
                       print("Invalid choice bhai sahi choice dal!!")

        case '2':
            while True:
                print("1. Addition")  
                print("2. Subtraction") 
                print("3. multiplication") 
                print("4 . division")  
                print("5. Back to te main menu") 

                c = input("Enter your choice: ")  
                match c:
                    case '1':
                    
                        print("Addition of two arrays")
                        t = f"{tool.arr1()+tool.arr2()}"
                        print("="*30)
                        print("Addition: ")
                        print(t)
                        print("="*30)
                    
                    
                    case '2':
                        print("Subtration of two arrays")
                        s = f"{tool.arr1()-tool.arr2()}"
                        print("="*30)
                        print("Subtraction: ")
                        print(s)
                        print("="*30)
            
                    case '3':
                        print("Multiplication of two arrays")
                        
                        k = f"{tool.arr1()*tool.arr2()}"
                        print("="*30)
                        print("Multiplication: ")
                        print(k)
                        print("="*30)

                    case '4':
                        print("Division of two arrays")
                        arr1 = tool.arr1()
                        arr2 = tool.arr2()
                        if arr1 is not None and arr2 is not None:
                            if np.any(arr2 == 0):
                                print("Error: Division by zero detected in the second array!")
                            else:
                                result = arr1 / arr2
                                print("="*30)
                                print("Division:")
                                print(result)
                                print("="*30)
                        else:
                            print("Array creation failed.")
                    
                    case '5':
                        print("going back to the main menu")
                        break
                    case _:
                        print("invalid case!")

        case '3':
            print("Choose an option")
            while True:
                print("1. Combine array")
                print("2. Split Array")
                print("3. back to the main menu")
                d = input("Enter choice:")
                match d:
                    case '1':
                        print("Combining array...")
                        v = np.concatenate([tool.arr1(),tool.arr2()]) 
                        print("="*30)
                        print("Combined array: ")
                        print(v)
                        print("="*30)

                    case '2':
                        print("Choose option")
                        while True:
                            print("1. Verticle split")
                            print("2. Horizontal split")
                            d = input("Select the option")
                            match d:
                                case '1':
                                    # print("ENTER ")
                                    a = tool.arr1()
                                    cols = a.shape[1]
                                    if cols % 2 == 0:
                                        j = np.vsplit(a,2)
                                        print("="*30)
                                        print("Splitted array into vertically: ")
                                        for part in j:
                                            print(part)
                                        print("="*30)
                                    else:
                                        print(f"Cannot split into 2 equal parts. Columns = {cols}")

                                case '2':
                                    b = tool.arr1()
                                    try:
                                        rows = b.shape[1]
                                        if rows%2 == 0:
                                            result = np.hsplit(b,2)
                                            print("="*30)
                                            print("Splitted array into horizontaly")
                                            for k in result:
                                                print(k)
                                        else:
                                            print(f"Cannot split into 2 equal parts. Rows = {rows}")
                                            print("="*30)
                                    except ValueError:
                                        print("Please enter in proper format")
                                case _:
                                    print("invalid case!")
                    case '3':
                        print("Going back to the main menu...")
                        break
                    case _:
                        print("invalid case!")
        case '4':
            print("Choose an opton")
            while True:
                print("1. Search a value")
                print("2. Sort the array")
                print("3. Filter values")
                print("4. Exit")

                j = input("Enter your choice: ")
                match j:
                    case '1':
                        a = tool.arr1()
                        search = int(input("Enter a value to search: "))
                        if search in a:
                            print("="*30)
                            print("yess we found it!!")
                            print(search)
                            print("="*30)
                        else:
                            print("Not found!")
                            print("="*30)

                    case '2':
                        print("Select the type of sorting")
                        while True:
                            print("1. Ascending order")
                            print("2. descending order")
                            print("3. Exit")
                            d = input("Enter your choice: ")
                            match d:
                                case '1':
                                    a = tool.arr1()
                                    if a is not None:
                                        try:
                                            b = np.sort(a, axis=1)  # Sort each row in ascending order
                                            print("=" * 20)
                                            print("Your sorted array in ascending order:")
                                            print(b)
                                            print("=" * 20)
                                        except Exception as e:
                                            print("Sorting failed:", e)
                                    else:
                                        print("Array creation failed.")

                                case '2':
                                    a = tool.arr1()
                                    if a is not None:
                                        try:
                                            b = -np.sort(-a,axis=1)
                                            print("Your sorted array in descending order:")
                                            print(b)
                                            print("=" * 20)
                                        except Exception as e:
                                            print("Sorting failed:", e)
                                    else:
                                        print("Array creation failed")
                                case '3':
                                    print("Returning to the previous menu...")
                                    break

                                case _:
                                    print("Invalid choice! Please enter 1, 2, or 3.")

                    case '3':
                        a = tool.arr1()
                        try:
                            b = int(input("Enter number to filter (if you enter four then the value you will get will be greater than): "))
                            filtered = a[a>b]
                            print("="*30)
                            print(f"Filtered values greater than {b}: ")
                            print(filtered)
                            print("="*30)
                        except ValueError:
                            print("filtering programme failed")
                    case _:
                        print("Invalid choice")

        case '5':
            print("Choose an Aggregate/statistical opertaion")
            while True:
                print("1. Sum")
                print("2. Mean")
                print("3. Median")
                print("4. Standard Deviation")
                print("5. Variance")
                print("6. Exit")

                k=input("Enter your choice: ")
                match k:
                    case '1':
                        print("Sum of all numbers")
                        s = tool.arr1()
                        try:
                            total = np.sum(s)
                            print("="*17)
                            print("Your Sum Value: ")
                            print(f"Overall mean: {total}")
                            print("="*17)
                        except ValueError:
                            print("programme filed due to ",ValueError)
                            
                    case '2':
                        a = tool.arr1()
                        try:
                            meann = np.mean(a)

                            print("="*20)
                            print("Your Mean Value: ")
                            print(f"Overall mean: {np.mean(meann)}")
                            print("="*20) 
                        except ValueError:
                            print("Programme failed",ValueError)

                    case '3':
                        a = tool.arr1()
                        try:
                            media = np.median(a)

                            print("="*20)
                            print("Your Median Value: ")
                            print(f"Overall median: {np.mean(media)}")
                            print("="*20) 
                        except ValueError:
                            print("Programme failed",ValueError)

                    case '4':
                        a = tool.arr1()
                        try:
                            stad = np.std(a)
                            print("="*20)
                            print("Your Standar deviation Value: ")
                            print(f"Overall median: {stad}")
                            print("="*20) 
                        except ValueError:
                            print("Programme failed",ValueError)

                    case '5':
                        a = tool.arr1()
                        try:
                            varience = np.var(a)
                            print("="*20)
                            print("Your variance Value: ")
                            print(f"Overall varience: {varience}")
                            print("="*20) 
                        except ValueError:
                            print("Programme failed",ValueError)

                    case '6':
                        print("exit..")
                        break
                    case _:
                        print("Invalid choice")

        case '6':
            print("Thank You for using the NumPy Analyzer! Good bye!!")
            break

        case '7':
            print("Invalid choice (choose between from 1 to 6)")
            