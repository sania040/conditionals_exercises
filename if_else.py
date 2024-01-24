# Subject of the python script: Practice Questions for if conditional 
# Authored by: Sania Shakeel
# Where to contact: shakeelsania040@gmail.com   and   https://github.com/sania040


'''# Question 1: Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
# 1.1: Write a program that asks user to enter a city name and it should tell which country the city belongs to
city = input("Enter the name of city:  ")
if city in india:
    print("India")
elif city in pakistan:
    print("Pakistan")
elif city in bangladesh:
    print("Bangladesh")
else:
    print("SOrry!!")
# 1.2: Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
city1 = input("Enter first city: ")
city2 = input("Enter second city name: ")
if city1 in india and city2 in india:
    print("They both belong to india...")
elif city2 in pakistan and city1 in pakistan: 
    print("They both belong to pakistan...")
elif city1 in bangladesh and city2 in bangladesh:
    print("They both belong to bangladesh")
else:
    print("They both dont belong to same country...")
    
# Question 2: Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#Ask user to enter his fasting sugar level
suger_level = int(input("Enter suger level: "))
#If it is below 80 to 100 range then print that sugar is low
if suger_level in range(80,100):
    print("Low")
#If it is above 100 then print that it is high otherwise print that it is normal
elif suger_level > 100:
    print("High")
else:
    print("normal")
    '''
import math
# Question 3: Write a program that takes three sides of a triangle as input and prints whether it is a right-angled triangle or not.
def handle_sqrt_for_input():
    user_input = input("Enter sqrt for squareroot or numberical value for side: ")
    if user_input.lower() == 'sqrt':
        return math.sqrt(int(user_input))
    else:
        return int(user_input)
side1 = handle_sqrt_for_input()
side2 = handle_sqrt_for_input()
side3 = handle_sqrt_for_input()    
is_right_triangle= side3**2 == (side2**2 + side1**2) or side2**2 == (side1**2 + side3**2) or side1**2 == (side2**2 + side3**2)
if is_right_triangle:
    print("Right Triangle...")
else:
    print("Not a right triangle...")
    
'''# Question 4: Write a program that takes an integer as input and prints whether it is positive, negative, or zero.
integer = int(input("Enter integer: "))
if integer < 0:
    print("Negative...")
elif integer > 0: 
    print("Positive...")
else:
    print("zero")'''
'''
# Question 5: Create a program that checks whether a given year is a leap year or not. A leap year is divisible by 4, but not by 100 unless it is divisible by 400.
year = int(input("ENter the year: "))
if year % 400 == 0:
    if year % 4 == 0 and year % 100 == 0:
        print("Leap year....")
else:
    if year % 4 == 0 and year % 100 != 0:
        print("leap year...")
    else:
        print("Not a leap year...")
        '''
'''# Question 6: Write a program that asks the user to enter their age and then prints whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or a senior (60 years and above).
age = int(input("Enter your age: "))
if  age in range(0,13):
    print("Child....")
elif age in range(13,20):
    print("Teenager...")
elif age in range(20,60):
    print("Adult")
else:
    print("Senior...")'''

'''### Question 7: Create a program that takes three numbers as input and prints the largest one.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number:"))
number3 = int(input("Enter number three: "))
max = 0
if number1 > number2 and number1 > number3:
    max = number1
elif number2 > number1 and number2 > number3:
    max = number2
else: 
    max = number3
print('max is', max)
'''
'''### Question 8:Write a program that checks whether a given string is a palindrome (reads the same backward as forward) or not.
word = input("Enter word:")
if word == word[::-1]:
    print("Palindrome...")
else:
    print("not a pakindrome...")
### Question 9:Create a program that asks the user to input a day of the week and then prints whether it's a weekday or a weekend.
day = input("Enter day:")
if day == 'saturday' or day == 'sunday':
    print("Weekand:)")
else:
    print("weekday:(")
    '''
'''### Question 10:Write a program that takes a temperature in Celsius as input and prints whether it is freezing (below 0°C), normal (0-25°C), warm (26-35°C), or hot (above 35°C).
temprature = int(input("Enter temprature:"))
if temprature < 0: 
    print("freezing...:0")
elif temprature in range(0,26):
    print("Normal...:)")
elif temprature in range(26, 36):
    print("Warm... :|")
else:
    print("Hot..... :(")    '''
    
'''### Question 11:Create a program that checks if a given number is even or odd.
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even....")
else:
    print("Odd....")'''
'''### Question 12:Write a program that takes a letter as input and prints whether it is a vowel or a consonant.
letter = input("Enter the letter:")
vowel = ['a', 'e', 'i', 'o', 'u']
if  letter in vowel:
    print("Vowel.....")
else: 
    print("Consonent...")'''
    
'''### Question 13:Create a program that asks the user to enter three sides of a triangle and prints whether it is an equilateral, isosceles, or scalene triangle.
side_1 = int(input("Enter first side: "))
side_2 = int(input("Enter second side: "))
side_3 = int(input("Enter third side: "))

if side_1 != side_2 and side_1 != side_3 and side_2 != side_3: 
    print("Scalene")
elif side_1 == side_2 and side_1 != side_3 or side_3 == side_2 and side_3 != side_1 or side_3 == side_1 and side_3 != side_2:
    print("Isoscelese")
elif side_2 == side_1 and side_1 == side_3:
    print("equilateral")'''