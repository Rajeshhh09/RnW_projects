import random
import string

def generate():
    try:
        length = int(input("Enter password lngth: "))
        if length < 4:
            print("Password length should be at least more than 4!")
            return
        character = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(character, k=length))
        print("Generated password:", password)
    
    except ValueError:
        print(" ")

def otp_generator():
    r = random.randint(1000,9999)
    return r
    


# while True:
#     print("""
# 1. Generate Random Number
# 2. Generate Random List
# 3. Create Random Password
# 4. Generate Random OTP
# 5. Back to Main Menu          """)
    
#     choice = input("Enter Choice: ")

#     match choice:
#         case '1':
#             print("="*30)
#             ra = random.randint(1,9)
#             print(f"Here is your random number: {ra}")
#             print("="*30)
#         case '2':
#             print("="*30)
#             ru = [random.randint(1,99) for _ in range(9)]
#             print("Random Integer List:", ru)
#             print("="*30)

#         case '3':
#             print("="*30)
#             generate()
#             print("="*30)

#         case '4':
#             print("="*30)
#             print("Your OTP (Dont Share With Anyone!):",otp_generator())
#             print("="*30)

#         case '5':
#             print("Exitig...")
#             break
#         case _:
            # print("Invalid option!")