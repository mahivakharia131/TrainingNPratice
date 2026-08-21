#=======================================================================================================================#
###1 WARF to print factorial 

# def factorial(n):
#     if(n == 0 or n ==1):
#         return 1
#     else:
#        return n*factorial(n-1)
# print(factorial(3))

#=======================================================================================================================#
###2 WARF to print sum of n natural numbers

# def add(n):
#     if(n==0):
#         return 0
#     else:
#         return n+add(n-1)

# print(add(3))

#=======================================================================================================================#
###3 WARF to print all elements in a list

# def ele(list1 , index):
#     if index == len(list1):
#         return
#     print(list1[index])
#     ele(list1,index+1)


# list1 = ["ram", 23 , 24.6,"priya"]
# ele(list1 , 0)

#=======================================================================================================================#
###4 WARF for backtracking in a maze

# def maze(i,j,n,m):
#     if i==n or j==m:
#         return 0
#     elif i==n-1 and j==m-1:
#         return 1
#     r = maze(i,j+1,n,m)
#     d = maze(i+1,j,n,m)
#     return r+d
# print(maze(0,0,11,11))

#=======================================================================================================================#
###5 WARF Spiral matrix


# def spiral(matrix,top,left,bottom,right):
# # base case
#     if (top>bottom or left>right):
#        return

#     for i in range(left,right+1):
#         print(matrix[top][i])
#     for i in range(top+1,bottom+1):
#         print(matrix[i][right])
#     for i in range(right-1,left-1,-1):
#         print(matrix[bottom][i])
#     for i in range(bottom-1,top,-1):
#         print(matrix[i][left])
    
#     spiral(matrix,top+1,left+1,bottom-1,right-1)

# matrix = [
#     [1,2,3,4],
#     [12,13,14,5],
#     [11,16,15,6],
#     [10,9,8,7]
# ]

# top=0
# bottom=3
# left=0
# right=3

# spiral(matrix,top,left,bottom,right)


#======================================================================================================================#
###6 WAP 2 numbers as input and perform division. use exception handling to manage potential 

# try:
#     a = int(input("Enter num1:"))
#     b = int(input("Enter num2:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Invalid denominator value, it should be greater than zero")
# except ValueError:
#     print("Invalid Input/Data type")
