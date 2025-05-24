class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name: {self.name}, age: {self.age}")

class employee(person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.__emp_id = emp_id
        self.__salary = float(salary)

    def display(self):
        super().display()
        print(f"employee ID: {self.__emp_id} employee Salary: {self.__salary}")

    def get_salary(self):
        return self.__salary
    
    def get_emp_id(self):
        return self.__emp_id
    
    def __gt__(self,other):
        if self.__salary > other.get_salary():
            return True
        elif self.__salary == other.get_salary():
            return self.__emp_id > other.get_emp_id()
        else:
            return False
    
class manager(employee):
    def __init__(self, name, age, emp_id, salary,department):
        super().__init__(name, age, emp_id, salary)
        self.department = department
    
    def display(self):
        super().display()
        print(f"department: {self.department}")

people = []

print("---\nChoose an Operation---")
while True:

    print("\n=== Employee Management System ===")
    print("\n ---Choose another Operation---")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. show details")
    print("5. Compare Salaries")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            name = input("enter name: ")
            age = input("enter age: ")
            p = person(name,age)
            people.append(p)
            print(f"person created With name: {name} and age: {age}  ")

        case '2':
            name = input("enter name: ")
            age = input("enter age: ")
            emp_id = input("enter employee id: ")
            salary = input("enter salary: $ ")
            e = employee(name,age,emp_id,salary)
            people.append(e)
            print(f"Employee created with name: {name}, age: {age}, ID: {emp_id} and salary: ${salary} ")
        
        case '3':
            name = input("enter name: ")
            age = input("enter age: ")
            emp_id = input("enter employee id: ")
            salary = input("enter salary: $")
            department = input("enter department: ")
            m = manager(name,age,emp_id,salary,department)
            people.append(m)
            print(f"Manager created with name: {name}, age: {age}, ID: {emp_id} and salary: ${salary} and department: {department} ")


        case '4':

            while True:
                print("1. person")
                print("2. employee")
                print("3. manager")
                print("4. exit")

                choice2 = input("enter choice: ")

                match choice2:
                    case '1':
                        print("person details ")
                        print("-"*40)
                        for p in people:
                            if isinstance(p,person) and not isinstance(p,employee):
                                p.display()
                                print("-"*40)

                    case '2':
                        print("employee details")
                        print("-"*40)
                        for person in people:
                            if isinstance(person,employee) and not isinstance(person,(manager)):
                                person.display()
                                print("-"*40)

                    case '3':
                        print("Manager details")
                        print("-"*40)
                        for person in people:
                            if isinstance(person,manager):
                                person.display()
                                print("-"*40)
                    case '4':
                        print("Exiting...")
                        break

                    case __:
                        print("invalid option")
        case '5':



            emp_id1 = input("Enter the first employee's ID: ")
            emp_id2 = input("Enter the Secound Employee's ID: ")

            emp1 = None
            emp2 = None

            
            for p in people:
                if isinstance(p, employee):
                    if p.get_emp_id() == emp_id1:
                        emp1 = p
                    if p.get_emp_id() == emp_id2:
                        emp2 = p

            if emp1 is None or emp2 is None:
                print("Enter valid ID number!! ")
            else:
                if emp1.get_salary() < emp2.get_salary():
                    print(f"Employee {emp1.name}{(emp_id1)} has lower salary than Manager {emp2.name} {(emp_id2)}")
                elif emp1.get_salary() == emp2.get_salary():
                    print("Dono ki salary barabar hai.")
                else:
                    print(f"{emp2.name} have more salary than {emp1.name} .")
  
                
                    
            

        case '6':
            print("Exiting the System. All Rsources have been freed")
            print("Good Bye!")
            break

        case ___:
            print("invalid choice . try again")
                


