#==========================================================================================================================#
###1 WAP to define a func of negative number error, write check_positive func tht raises exception for negative number passed

# Inheritance from class by using except exception as e where we raised class in try block or only if-else statement
# finally to check u reached end of the code

# class NegativeNumberError(Exception):
#     pass

# try:
#     n = int(input("Enter a num: "))

#     if(n<0):
#         raise NegativeNumberError("Number is Negative!!")
#     print(f"Number: {n}")
# except Exception as e:
#     print(f"Error={e}")
# finally:
#     print("Code Completed")

## do later just to chk##
# try:
#     print(1)
#     if(-4):
#         raise NegativeNumberError
#         print(2)
# print(3)
# except:
#   print("Error")
#   print(4)


#==========================================================================================================================#
###2 WAP to map into a list to multiply by 2
# map returns address so convert it again while printing, return objects only
# s*2 doubles the number of elements but since called by map 1-1 value goes in the func and operations r performed

# def mulby2(x):
#     return x*2

# s = [2,8,3,4]
# result = list(map(mulby2,s))
# print(result)

#==========================================================================================================================#
###3 WAP to filter is negative number
# for loop and if else is required here if not filter

# def is_negative(num):
#     return num<0
# num = [1,-2,-4,7,-5]
# negative_num = list(filter(is_negative,num))
# print(negative_num)

#==========================================================================================================================#
###4 WAP to reduce add and average and multiplication

# from functools import reduce 
# def add(x,y):
#     return x+y
# a = [1,2,3,4,5]
# res = reduce(add,a)
# print(res)

# from functools import reduce
# def sum(x,y):
#     return x+y
# a = [1,2,3,4,5]
# res = reduce(sum,a)
# print(res/len(a))

# from functools import reduce
# def fact(x,y):
#     return x*y
# a = [1,5,10,4,2]
# res = reduce(fact,a)
# print(res)

#==========================================================================================================================#
###5 WAP Circle class to create a circle with radius r using the constructor

# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius**2
#     def perimeter(self):
#         return 2*math.pi*self.radius
# r = float(input("Enter radius: "))
# c1 = Circle(r)
# print(f"Area of Circle with radius {r} is: {c1.area():.2f}")
# print(f"Perimeter of circle: {c1.perimeter():.2f}")

#==========================================================================================================================#
###6 WAP student name , with 3 subject marks and average of it

# class Student:
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3

#     def average(self):
#         return (self.sub1 + self.sub2 + self.sub3)/3 
#    
# n = input("Enter Student name: ")
# print()

# for i in range(1,4):
#     n = list(map((input(f"Enter name of subject {i}: "))))
#     m = list(map((int(input(f"Enter marks of subject {i}: ")))))
#     print()

# student = Student(n,m[0],m[1],m[2])
# print(f"Average marks of {n} : {student.average():.3f}")

#=====================================================================================================================#
###7 WAP same as above but dynamic

# class Student:
#     def __init__(self,name,sub:list):
#         self.name = name
#         self.sub = sub

#     def average(self,marks,subjects):
#         a = sum(marks)/subjects
#         return a

# name= input("Enter Student name: ")
# subjects= int(input("Enter number of subjects: "))
# print()
# sub =[]
# marks=[]
# for i in range(subjects):
#     sub.append(input(f"Enter name of subject{i+1}: "))
#     marks.append(int(input(f"Enter marks of {sub[i]} : ")))
#     print()
# student = Student(name,sub)
# print(student.average(marks,subjects))






        
        