print("\nWelcone to the Data Analyzer and Transformer Program \n")

#here we created a empty list to store data
data = []

#user define is declared here because we cannot decalre function inside the code
 
def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)
    

#taking options
  
while True:
    print("\n1. Input Data")
    print("2. Display Data Summary (Built-in Function)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Value)")
    print("7. Exit Program\n")

    choice = (input("Please enter your choice: "))

    match choice:

        case "1":
            data_input = input("\nEnter data for a 1D array (separated by spaces):")

            #map function converting the list into string

            data = list(map(int, data_input.split()))
            print("\nData has been stored successfully !")
            print(f"your data {data}")

        case "2":
            if not data:
                print("\nno data found! please input data first")
            else:    
                print("\nData summary:")
                print(f"Total element: {len(data)}")      
                print(f"Minimum value: {min(data)}") 
                print(f"Maximum value: {max(data)}")
                
                sum = 0
                for i in data:
                    sum = sum+i

                print("Sum of all numbers: ",sum)  

                average = sum/len(data)
                print("Avergae value: ",average )

        case "3":

             number = int(input("Enter a number to calculate its factorial: ")) 

             result = factorial(number)
             print(f"Factorial of {number} is: {result}\n")

        case "4":
                value = int(input("Enter a threshold value to filter out data above this value: ")) 
                filtered_data = list(filter(lambda x: x >= value,data))
                print(f"Filtered Data(Values >= {value}): {filtered_data}\n")

        case "5":

                print("choose sorting option")

                while True:

                    print("1. Ascending order")
                    print("2. descending order")
                    option = input("Enter your choice: ")

                    match option:
                        case "1":
                            if not data:
                              print("no data found , please insert the data!!")
                            else:
                              a = list(sorted(data))
                              print(f"sorted data in ascendind order:{a}: ")

                        case "2":
                              d = list(sorted(data, reverse = True))
                              print(f"sorted data in descending order:{d}: ")
                              break

        case "6":
              
              print("Dataset Statistics\n")

                #if some enter option 6 without inputing the data so this line will run
              if not data:
                  print("no data found please enter the data!!")
              else:
                minn = (min(data))
                print(f"Minimum value: {minn}")

                maxi = (max(data))
                print(f"Maximum value: {maxi}")

                total = 0

                for i in data:
                    total +=i  

                print("Sum of all values: ",total)   

                avg = total/len(data)

                print(f"Average value: {avg}")       

                              

        case "7":
            print(" \n thank you for using the data analyzer and transformer program. goodbye!")
            break