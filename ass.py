# KINDLY NOTE THAT ALL PROGRAMS ARE WRITTEN IN ONE FILE PLEASE MARK OTHER PROGRAMS AS COMMENT BEFORE RUNNING ONE
# OR COPY ONE PROGRAM AND RUN ONE AT A TIME

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)




from datetime import datetime
# datetime object containing current date and time
now = datetime.now() 
print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)


nnum1 = input("First Number:")
num2 = input("Second Number:")
# Add two numbers
sum = float(num1) + float(num2)
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))   


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
