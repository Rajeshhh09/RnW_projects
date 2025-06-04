def create():
    filename = input("Enter file name to create (with .txt): ")
    try:
       
        with open(filename, "r"):
            print("File already exists.")
    except FileNotFoundError:
        
        with open(filename, "w") as f:
            f.write("File created!\n")
        print(f"{filename} created successfully.")
    return filename

def write_file(filename):
    text = input("Enter text to write: ")
    with open(filename, "w") as f:
        f.write(text + "\n")
    print("Content written successfully.\n")

def append_file(filename):
    while True:
        text = input("Enter text to append (or type 'exit' to stop): ")
        if text.lower() == 'exit':
            print("Stopped appending.\n")
            break
        with open(filename, "a") as f:
            f.write(text + "\n")
        print("Text appended.\n")

def read(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print("\n File Content:\n" + "-"*30)
            print(content)
            print("-"*30)
    except FileNotFoundError:
        print("File not found. Cannot read.")


# file = create()


# while True:
#     print("\nWhat do you want to do?")
#     print("1. Write to file")
#     print("2. Append to file")
#     print("3. read")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         write_file(file)
#     elif choice == '2':
#         append_file(file)
#     elif choice == '3':
#         read(file)
#     else:
#         print("Invalid choice. Try again.")
