print("\nwelcome to the pattern generator and Number Analyzer!\n")

while True:
    
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. exit")

    choice = input("\nEnter your choice: ")

    match choice:
             
        case "1":
            
            print("1. Right-angle Triangle:")
            print("2. pyramid")
            print("3. Left-angled Triangle")
            
            pattern_choice = input("\nselect patteern type: ")
            
            rows = int(input("\nEnter the number of rows for pattern: "))

            match pattern_choice:
                
                case "1":

                    print("-"*40)
                    print("Pattern")
                    for i in range(1,rows +1):
                         print("*"*i)
                    print("-"*40)

                case "2":

                    print("-"*40)
                    print("Pattern")
                    for i in range(1,rows +1):
                         spaces = rows - i
                         star = 2*i-1
                         print(" "* spaces + "*" * star)
                    print("-"*40)

                case "3":

                    print("-"*40)
                    print("Pattern")
                    for i in range(1,rows +1):
                         print(" "*(rows-i),"*" *i)
                    print("-"*40)   

                case __:
                         print("invalid number")

        case "2":
           
           start_range = int(input("enter the start of the range: "))
           end_range = int(input("enter the end of the range: "))
           print("\n")
           sum = 0
           for i in range(start_range,end_range):
                if(i %2 == 0):
                     print(f"Number {i} is even ")
                else:
                    print(f"Number {i} is odd ") 

                    sum = sum+i
           print(f"\nSum of all numbers from 10 to 15 is: {sum}")
            
            
        case "3":
            print("Exiting the program. Goodbye!")
            break
        case __:
            print("invalid number")