#=========================================================================================================================#
###1 WAP, Input 2 names, Enter the total number of vowels in boht names print good match if total is even else print average match

# name1 = input("Enter name of first person: ")
# name2 = input("Enter name of second person: ")
# name3 = name1 + name2

# a = name3.count.lowercase("a")
# b = name3.count.lowercase("e")
# c = name3.count.lowercase("i")
# d = name3.count.lowercase("o")
# e = name3.count.lowercase("u")

# count = a+b+c+d+e
# print(count)

# if count%2==0:
#     print("Good match")
# else:
#     print("Average match")


#=========================================================================================================================#
###2 WAP to ask user to enter 3 names of their fav movie and store them in a list 

# movie1 = input("Enter fav movie 1: ")
# movie2 = input("Enter fav movie 2: ")
# movie3 = input("Enter fav movie 3: ")
# movie_list = [movie1,movie2,movie3]
# print(movie_list)

## OR ##
# movie_list = list(map(str, input("Enter 3 favourite movies that u like: ").split()))

## OR ##
# movie_list = []
# movie_list.append(movie1)
# movie_list.append(movie1)
# movie_list.append(movie1)

# Theory: map is a high order function,takes 2 parameters

#=========================================================================================================================#
###3 WAP to print Name,Age,Branch from tuple and normally 

# student = ("Alice",20,"Computer Science")
# print("Name: ", student[0])
# print("Age: ", student[1])
# print("Branch: ", student[2])

## OR ##
# Take input for name,age and branch and use f string

#=========================================================================================================================#
###4 WAP to count number of students with "A" grade in following tuple ("C,"D","A","B","B","A")

# tup1 = ("C","D","A","B","B","A")
# list = list(tup1)
# list.sort()
# print(tuple(list))

#=========================================================================================================================#
###5 WAP to print values from 1 to 100 and 100 to 1 , multiplication of number n

# for i in range(1,101):
#     print(i , end=" ")

# for i in range(100,0,-1):
#     print(i ,end=" ")

# number = int(input("Enter a number to multiply: "))
# for i in range(1,11):
#     print(f"{number} x {i} = {number * i}")

#=========================================================================================================================#
###6 WAP to print elements of list in a loop

# n = int(input("Enter a num: "))
# list1 =[]
# for i in range(1,n+1):
#     list1.append(i**2)
# print(list1)

# find = int(input("Enter the number u want to find: "))

# for i in range(len(list1)):
#     if find == list1[i]:
#         print(f"Found the element at index {list1.index(find)}")
#         break
# else:
#     print("Element not Found")

#=========================================================================================================================#
###7 WAP to find sum of n natural numbers

# n = int(input("Enter the number to find sum of n natural numbers: "))
# sum = 0
# i=0
# while i<=n:
#     sum = sum + i 
#     i+=1
# print(sum)

#=========================================================================================================================#
###8 WAP to find factorial of first n natrural numbers

# n = int(input("Enter the number to find factorial of number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"Factorial of {n} is {fact}")

#=========================================================================================================================#
###9 WAP to find permutation

# n = int(input("Enter n for permutation: "))
# r = int(input("Enter r for permutation: "))

# num = n
# denom = n - r

# num=1
# denom=1
# for i in range(1,n+1):
#     num=num*i
# print(num)

# for i in range(1,n-r+1):
#     denom=denom*i
# print(denom)

# permutation = num/denom
# print(permutation)

#=========================================================================================================================#
###10 WAP for combination

# n = int(input("Enter n for combination: "))
# r = int(input("Enter r for combination: "))

# num = n 
# denom = r*(n-r)

# num=1
# denom=1

# for i in range(1,n+1):
#     num=num*i
# print(num)

# for i in range(1,r*(n-r)+1):
#    denom=denom*i
# print(denom)

# combination = num/denom
# print(combination)

#===============================================================================================================================================================================#

# Theory : Data structure vs data type

#=========================================================================================================================#
###11 WAP to store following word meanings in a pyhton dictionary

# dictionary = {'table': ("a piece of furniture","list of facts and figures") , 'cat': "a small animal"}

# for i in dictionary.items():
#     print(i)

# print(dictionary.items())

#=========================================================================================================================#
###12 WAP to enter marks with 3 subjects from user and store them in a dict. start with an empty dict and add one by one.sub name as key and marks as value

# dictionary = {}
# for i in range(1,4):
#     key = input(f"Enter name of Subject-{i}: ")
#     value = int(input(f"Enter marks of {key}: "))
#     print()
#     dictionary.update({key:value})
#     print(dictionary)

#=======================================================================================================================#
###1 WAP to create a frequency calculator

# arr = []
# n = int(input("Enter the number of elements in an array: "))
# for i in range(n):
#     arr.append(int(input(f"Enter the element {i+1}: ")))
# print(arr)

# dict = {}
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if arr[i]==arr[j]:
#             count+=1
#     if arr[i] not in arr[:i]:
#         print(arr[i], "=" , count)


# for i in arr:
#     dict[i] = arr.count(i)
# print(dict)

#=======================================================================================================================#
###


















