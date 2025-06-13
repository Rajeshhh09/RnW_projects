class array_tool:
    def __init__(self):
        self.arr = None

    def create_array(self):
        r = int(input("enter a array"))
        elements = input(f"Enter {r} numbers separated by spaces: ").split()
        elements = [int(x) for x in elements ]
        self.arr = np.array(elements)
        print("Array created successfully:")
        print(self.arr)

tool = array_tool()

print("=" * 30)
print("Choose an Option")
while True:
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or split Arrays")
    print("Search, sort, or Filter Arrays")
    print("Copute Aggregates and Statistics")
    print("Exit")
    choice = input("Enter Your Choice: ")
    match choice:
        case '1':
           tool.create_array()