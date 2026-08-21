#=========================================================================================================================#
###1 WAP that asks user enter : full name, email address , password 

# name = input("Enter your name: ").strip()
# email = input("Enter your email-id: ")
# password = input("Enter your password: ")
# flag = True

# if('' not in name):
#     flag = False
#     print("Invalid Full Name")

# if('@' not in email or not(email.endswith(".com"))):
#     flag = False
#     print("Invalid Email Address")

# if(len(password)<6 or password.count(' ')>0):
#     flag = False
#     print("Invalid Password")

# if(flag):
#     print("Form is sucessfully submitted")

## OR ##

# name = input("Enter your name: ").strip()
# email = input("Enter your email-id: ")
# password = input("Enter your password: ")

# using while loop

#=======================================================================================================================#
###2 WAP , u r given a no.of subjects for students. assume one classroom is required for 1 subject. how many classroom needed by all students

# subjects = set(["python","java","C++","python","javascript","java","python","java","C++","C"])
# print(subjects)
# print(len(subjects))

#=======================================================================================================================#
###3 WAP to accept a list from student and find average of marks and use sets for no repeated name

# n = int(input("Enter number of students: "))
# studentList = []
# names = []
# marks = []
# for i in range(n):
#     name = input("Enter the name: ")
#     mark = input("Enter the marks: ")
#     tup = (name,mark)
#     studentList.append(tup)

# studentList = [("alice",85),("Bob",80),("alice",82)]
# names = set()
# for student in studentList:
#     names.add(student[0])
# print(names)

# result =set()

# total=0
# count=0
# for name in names:
#     for student in studentList:
#         if student[0] == name:
#             total += student[1]
#             count += 1


#     average = total / count
#     result.add((name,average))
# print(result)

## doubtful ##
#     names.append(name)
#     marks.append(mark)

# for i in range(n):
#     for j in range(1,n):
#       if name[i] == name[j]:
#         marks = sum(marks[i]+marks[j])/
#     else:
#         print(name[i])

#=======================================================================================================================#
###4 WAP to find a way to store 9 and 9.0 as seperate value in a set

# set1 = set()
# var1 = int(9)
# var2 = float(9.0)
# set1.add((var1,var2))
# print(set1)

#=======================================================================================================================#
###5 WAF to print a length of a list. factorial 

# def length(l):
#     return len(l)

# p = ["Ram", 28, 2.8]
# print(length(p))

#=======================================================================================================================#
###6 WAF to print elements of a list in a single line 

# def list1(arr):
#     for i in arr:
#         print(i,end=" ")
# arr = [22,25,27]
# list1(arr)

#=======================================================================================================================#
###7 WAF for factorial

# def factorial(n):
#     fact = 1
#     for i in range(1,n):
#         fact*=i
#     return fact

# n=4
# print(f"Factorial of {n} = {factorial(n)}")


#=======================================================================================================================#
###8 WAF to convert USD to INR , 1 USD = 96 Rs

# def convert(Usd):
#     inr = usd * 96
#     return inr

# usd = float(input("Enter USD amount: "))
# print(f"Conversion ${usd} = Rs. {convert(usd) } ")

#=========================================================================================================================#
###9 WAF to give user to choice to do permutation and combination by 1 and 2 

# def permutation(n,r):
#     num = 1
#     denom = 1
#     for i in range(1,n+1):
#         num= num*i
#     for i in range(1,(n-r)+1):
#         denom= denom*i
#     return num/denom

# def combination(n,r):
#     num = 1
#     denom = 1
#     for i in range(1,n+1):
#         num=num*i
#     for i in range(1,(n-r)*r):
#         denom=denom*i
#     return num/denom

# n = int(input("Enter n for solving: "))
# r = int(input("Enter r for solving: "))
# input = int(input("Enter 1 for Permutation and 2 for Combination: "))

# if input == 1:
#         print(f"Permutation = {permutation(n,r)}")
# elif input == 2:
#      print(f"Permutation = {combination(n,r)}")
# else:
#      print("Invalid choice, enter 1 or 2")

## OR ## 

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact

# n = int(input("Enter n of permutation or combination: "))
# r = int(input("Enter r of permutation or combination "))

# choice = int(input("Enter 1 for permutation and combination: "))
# if choice ==1:
#     print("Permutation of given n and r is as follows: ")
#     num = factorial(n)
#     denom = factorial(n-r)
#     print( num / denom )
# elif choice==2:
#   print("Combination of given n and r is as follows: ")
#   num = factorial(n)
#   down = factorial(n-r)* factorial(r)
#   print(num/down)
# else:
#     print("Enter number 1 or 2")

#=======================================================================================================================#
###10 WARF to print 1 to n , ## check again

# def numbers(i,n):
#     if(i == n+1):
#         return
#     print(i)
#     numbers(i+1,n)


# print("Code Starts!")
# numbers(1,5)
# print("Success")







 