print("welcome to the pattern generator and Number Analyzer!")

while True:
    
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. exit")

    choice = input("Enter your choice")

    match choice:
             
        case "1":
            
            print("1. Right-angle Triangle:")
            print("2. pyramid")
            print("3. Left-angled Triangle")
            
            pattern_choice = input("select patteern type: ")
            
            rows = int(input("enter the number of rows fpr pattern: "))

            match pattern_choice:
                
                case "1":
                    
                    for i in range(1,rows +1):
                         print("*"*i)

                case "2":
                    
                    for i in range(1,rows +1):
                         spaces = rows - i
                         star = 2*i-1
                         print(" "* spaces + "*" * star)
                
                case "3":
                    
                    for i in range(1,rows +1):
                         print(" "*(rows-i),"*" *i+1)
                         
                case __:
                         print("invalid number")

        case "2":
           start_range = int(input("enter the start of the range: "))
           end_range = int(input("enter the end of the range: "))
           if(start_range%2==0):
               print(f"number {start_range} is even")

           else:
               print(f"number {end_range} is odd")
        case "3":
            break
        case __:
            print("invalid number")
