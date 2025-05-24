# class rectangle:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         a = self.length * self.breadth
#         return a
        
#     def perameter(self):
#         b = 2*(self.length + self.breadth)
#         return b
        
    
# rect1 = rectangle(10,5)
# rect2 = rectangle(34,6)

# print("Rctangle 1")

# print(f"area,{rect1.area()}")
# print(f"perameter,{rect1.perameter()}")

# print("rectangle 2")

# print(f"area,{rect2.area()}")
# print(f"perameter, {rect2.perameter}")

# if rect1.area() > rect2.area():
#     print("rectangle 1 os bigger")
# else:
#     print("rectangle 2 is bigger")




# class bank:
#     def __init__(self,name,balance):
#         self.name = name 
#         self.balance = balance

#     def deposit (self,amount):
#         self.balance = self.balance + amount
#         print(f"deposited: {amount}, your current balance {self.balance}")

#     def withdraw(self,amount):
#      if amount <= self.balance:
#         self.balance -= amount
#         print(f"withdrawal !: {amount}, current balance: {self.balance}")
#      else:
#         print("insufficient balance!!")

#     def showbalance(self):
#         print(f"account holder name: {self.name}, your new balance {self.balance} ")

          
# ac1 = bank("rajesh",28900)   

# ac1.showbalance()
# ac1.deposit(20000)
# ac1.withdraw(6000)
# ac1.withdraw(8990)


# class movie:
#     def __init__(self,name,rating,year):
#         self.name = name
#         self.rating = rating
#         self.year = year

#     def set_rating(self,new_rating):
#         self.rating = new_rating
       

#     def is_hit(self):
#         if self.rating >= 7:
#             print(f"{self.name} is hit! ")
#         else:
#             print(f"{self.name} is flop")

# review = movie("sultan",8, 9)

# review.is_hit()

# class counter:
#     def __init__(self):
#         self.count = 0

#     def incriment(self):
#         self.count +=1
#         print(f"your incriment: {self.count}")
    

# l1 = counter()

# l1.incriment()
# l1.incriment()
# l1.incriment()
# l1.incriment()
# l1.incriment()
# l1.incriment()


# class car():
#     def __init__(self,model,name,number):
#         self.model = model
#         self.name = name
#         self.number = number

#     def show(self):
#         print(f"your car model : {self.model} && car name: {self.name}")

#     def __del__(self):
#         print(f"car is {self.name} is destroyed")

#     def l2(self):
        
#         if self.number <= 4:
#             print(f"your car is rubbish")
#         else:
#             print("sexy car")
    
#     def l3():
#         pass


# c1 = car(2022,"bmw",9)
# c1 = car(2021,"aud",3)

# c1.show()
# c1.l2()



# class animal:
#     def __init__(self,name):
#         self.name = name
    
#     def display(self):
#         print("your animal nameis:",self.name)


# a1 = animal("lion")

# a1.display()


# class rectangle:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth

#     def areaa(self):
#         area = self.length * self.breadth
#         print(f"your area is:  {area}")


# a1 = rectangle(3,5)
# a1.areaa()


# class employee ():
#     def __init__(self,name):
#         self.name = name

#     def __del__(self):
#         print(f"thanks your from bottom of my eart your {self.name}")
#         print("thank you everone for making my farewell great , good bye!!")

# c1 = employee("rajesh")

# c1.name()



# class book ():
#     def __init__(self):
#         self.title = ""
#         self.author = ""

#     def set(self,title,author):
#         self.title = title
#         self.author = author

#     def get(self):
#         print(f"the title {self.title} is awesome by {self.author} ")

# c1 = book()

# c1.set("summer vacation","rajesh")

# c1.get()


# class bank():
#     def __init__(self):
      
#         self.balance = 1

#     def depositt(self,amount):
#         self.balance += amount

#         print(f"deposited {amount} current balance {self.balance}")

#     def withdraw(self,amount):
#         if self.balance <= amount:
#             self.balance =- amount
#             print(f"your withdraw: {amount} now fund : {self.balance}")
#         else:
#             print("you dont have fund ")

#     def show_balance(self):
#         print(f"Your current balance is: ₹{self.balance}")

# c1 = bank()

# c1.depositt(50000)
# c1.withdraw(40000)
# c1.show_balance()
    
# uses getter and setter to validate the age of a person 
# class validate():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = 0
#         self.age = age 

#     def age(self):
#         return self._age
    
#     def age(self,value):
#         if value >=0:
#             self._age = value
#         else:
#             print("value cannot be negative")


#     def setter (self):
#         if(self.age>=18):
#             print(f"{self.name} you can vote !!")
#         else:
#             print(self.name," you are not elidgible for vote be 18 then come")
        
#     def getter (self):
#         print(f"{self.name} be 18 year old yrr!!")
   
# b1 = validate("rajesh",-1)
# b1.setter()
# b1.age()
# b1.getter()


# class student():
#     def __init__(self,division,grade):
#         self.devision = division
#         self.name = ""
#         self.marks = ""
#         self.grade = grade

#     def n_m(self):
#         self.name 
#         self.marks

#         return self.name,self.marks
    
#     def avg(self):
#         avj = sum(self.marks)/len(self.marks)
#         print(f"the average marks is {avj}")
        
#     def grd(self):
#         if self.mark <= value:
#             value = self.grade
#             print
#         if sel
    

# class addition():
#     def __init__(self,num1,num2,txt1,txt2):
#         self.num1 = num1
#         self.num2 = num2
#         self.txt1 = txt1
#         self.txt2 = txt2
    
#     def add(self):
        
#         return self.num1 + self.num2

#     def concatinate(self):
#         return self.txt1 + self.txt2  
        
#     def prnt(self):
#         result = self.add()
#         result2 = self.concatinate()
#         print(f"your answer is {result}")
#         print(f"your answer is {result2}")

# c2 = addition(22,33,"raj","esh")

# c2.prnt()



#perfect example of ploymorphism

# def adder(a,b):
#     return a+b

# print(f"your anser is {adder(1,2)}")
# print(f"your anser is {adder("r", "ajesh")}")


# class parents:
#     def display(self):
#         print("hello")

# class child(parents):
#     pass

# c = child()

# c.display()



# class teacher():
#     def teach(self):
#         print("teaching students ")

# class adminstrator():
#     def manage(self):
#         print("managing school ")

# class headmaster(teacher,adminstrator):
#     def lead(self):
#         print("leading the school ")

# hm = headmaster()

# hm.teach()
# hm.lead()
# hm.manage()


# class a:
#     def show(self):
#         print("this is a")
#         print("this is id of a : ",id(self))
#         print("this is type of a: ",type(self))

# class b(a):
#     def show(self):
#         print("this b")
#         print("this is id of b : ",id(self))
#         print("this is type of b: ",type(self))
        

# class c(a):
#     def show(self):
#         print("this is c")
#         print("this is id of c : ",id(self))
#         print("this is type of c: ",type(self))

# class d(a):
#     def show(self):
#         print("this is d")
#         print("this is id of d : ",id(self))
#         print("this is type of d: ",type(self))

# class e(a):
#     def show(self):
#         print("this is e")
#         print("this is id of e : ",id(self))
#         print("this is type of e: ",type(self))

# class f(a):
#     def show(self):
#         print("this f")

# class g(b, c, d, e, f):
#     def show(self):
#         print("this is id of e : ",id(self))
#         print("this is type of e: ",type(self))
#         print("-"*40)
#         a().show()
#         print("-"*40)
#         b().show()
#         print("-"*40)
#         c().show()
#         print("-"*40)
#         d().show()
#         print("-"*40)
#         e().show()
#         print("-"*40)
#         f().show()
#         print("-"*40)
#         print("this is multiple inheritance")

# obj = g()
# print(isinstance(obj,d))
# help(a)
# obj.show(a)



# class calculation():
#     def square(self,a):
#         b = a *a
#         print("square of a is ",b)

#         def cube():
#             self.a = a
#             b = a*a*a
#             print("cube of a is ",b)

#         cube()
        
# obj = calculation()
# obj.square(4)



# dic = []
# class calc:
#     def take_input(self):
#         self.a = str(input("enter a row of strings: "))

#         def prnt():
#              print(f"length of the string is{len(self.a)}")
#              word = self.a.split()
#              print(f"total numner of elemsnts in this (words): {len(word)}")

#              dic.append(self.a)

#         prnt()

# c1 = calc()
# c1.take_input()
# print(dic)


class clac:
    def area(self,a,l,b):
        self.a = a
        self.b = b
        self.c = l*b
        print(f"here is the rectangle of {self.c}")

        def area_aquare(self):
            self.d = self.a * self.a
            print(f"here is the square of {self.d}")

        area_aquare()

m = clac()
m.area(3,4,4)