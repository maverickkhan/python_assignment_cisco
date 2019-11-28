## ASSINGMENT 2 ##
# FIRST PROGRAM
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")

# SECOND PROGRAM
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# THIRD PROGRAM
n = len([10, 20, 30]) 
print("The length of list is: ", n) 

#4TH PROGRAM
total = 0
list1 = [11, 5, 17, 18, 23]  
for ele in range(0, len(list1)): 
    total = total + list1[ele] 
  
#5TH PROGRAM
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))

#6TH PROGRAM
def elements_lessthan_five(l):
    l1=[]
    for i in l:
        if i<5:
            l1.append(i)
            
    return(l1)
    
# print(elements_lessthan_five([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))

# 3rd ASSIGNMENT #
# first program 2nd assignment #
def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")

# 3rd Program Assignment 3 #
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

# assignment 3 question 4 #
def returnSum(dict): 
      
     sum = 0
     for i in dict.values(): 
           sum = sum + i 
       
     return sum
  
dict = {'a': 300, 'b':400, 'c':200} 
print("Sum :", returnSum(dict))

# Assignment 3 question 5
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
list1 = [10, 21, 30, 20, 21, 30, 40,  
         50, -20, 60, 60, -10, -10] 
print (Repeat(list1))

## assignment 3 question 4#
def checkKey(dict, key): 
      
    if key in dict.keys(): 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 
  
dict = {'a': 100, 'b':200, 'c':300} 
  
key = 'b'
checkKey(dict, key) 
  
key = 'w'
checkKey(dict, key) 