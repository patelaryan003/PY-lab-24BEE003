#a=int(input("plz enter 1 number:"))
#if(a>0):
#    print("the given number is posi")
#else:
#    print("the given number is negi")




# a=int(input("plz enter number:"))
# b=a%2
# if(b==0):
#     print("the number is even")
# else:
#     print("the number is odd")




# def find_largest_and_smallest(num1, num2):
#     largest = max(num1, num2)
#     smallest = min(num1, num2)
#     print(f"The largest number is: {largest}")
#     print(f"The smallest number is: {smallest}")
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     find_largest_and_smallest(num1, num2)
# except ValueError:
#     print("Please enter valid numbers.")



  

# def find_largest_and_smallest(num1, num2, num3):
#     largest = max(num1, num2, num3)
#     smallest = min(num1, num2, num3)
#     print(f"The largest number is: {largest}")
#     print(f"The smallest number is: {smallest}")
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     num3 = float(input("Enter the third number: "))
#     find_largest_and_smallest(num1, num2, num3)
# except ValueError:
#     print("Please enter valid numbers.")


# def is_divisible_by_10(number):
#     if number % 10 == 0:
#         print(f"{number} is divisible by 10.")
#     else:
#         print(f"{number} is not divisible by 10.")
# try:
#     number = int(input("Enter a number: "))
#     is_divisible_by_10(number)
# except ValueError:
#     print("Please enter a valid integer.")


# def check_age_category(age):
#     if age < 18:
#         print("You are a Minor.")
#     else:
#         print("You are a Major.")
# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         print("Age cannot be negative.")
#     else:
#         check_age_category(age)
# except ValueError:
#     print("Please enter a valid integer for age.")


# def count_digits(number):
#     num_digits = len(str(abs(number))) 
#     print(f"The number of digits in {number} is: {num_digits}")
# try:
#     number = int(input("Enter a number: "))
#     count_digits(number)
# except ValueError:
#     print("Please enter a valid integer.")


# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a Leap Year.")
#     else:
#         print(f"{year} is not a Leap Year.")
# try:
#     year = int(input("Enter a year: "))
#     if year < 0:
#         print("Please enter a valid positive year.")
#     else:
#         is_leap_year(year)
# except ValueError:
#     print("Please enter a valid integer for the year.")



# def is_triangle_valid(angle1, angle2, angle3):
#     if angle1 + angle2 + angle3 == 180:
#         print("The triangle is valid.")
#     else:
#         print("The triangle is not valid.")
# try:
#     angle1 = float(input("Enter the first angle: "))
#     angle2 = float(input("Enter the second angle: "))
#     angle3 = float(input("Enter the third angle: "))

#     if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
#         print("Angles must be positive values.")
#     else:
#         is_triangle_valid(angle1, angle2, angle3)
# except ValueError:
#     print("Please enter valid numbers for the angles.")


# def print_absolute_value(number):
#     absolute_value = abs(number)  
#     print(f"The absolute value of {number} is: {absolute_value}")
# try:
#     number = float(input("Enter a number: "))
#     print_absolute_value(number)
# except ValueError:
#     print("Please enter a valid number.")



# def compare_area_and_perimeter(length, breadth):
#     area = length * breadth
#     perimeter = 2 * (length + breadth)

#     print(f"Area of the rectangle: {area}")
#     print(f"Perimeter of the rectangle: {perimeter}")

#     if area > perimeter:
#         print("The area of the rectangle is greater than its perimeter.")
#     else:
#         print("The area of the rectangle is not greater than its perimeter.")
# try:
#     length = float(input("Enter the length of the rectangle: "))
#     breadth = float(input("Enter the breadth of the rectangle: "))

#     if length <= 0 or breadth <= 0:
#         print("Length and breadth must be positive numbers.")
#     else:
#         compare_area_and_perimeter(length, breadth)
# except ValueError:
#     print("Please enter valid numbers for length and breadth.")
    


# def are_points_collinear(x1, y1, x2, y2, x3, y3):
#     if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
#         print("The three points lie on the same straight line.")
#     else:
#         print("The three points do not lie on the same straight line.")
# try:
#     x1 = float(input("Enter x1: "))
#     y1 = float(input("Enter y1: "))
#     x2 = float(input("Enter x2: "))
#     y2 = float(input("Enter y2: "))
#     x3 = float(input("Enter x3: "))
#     y3 = float(input("Enter y3: "))

#     are_points_collinear(x1, y1, x2, y2, x3, y3)
# except ValueError:
#     print("Please enter valid numerical values for the coordinates.")


# import math
# def check_point_position(x_center, y_center, radius, x_point, y_point):
#     distance = math.sqrt(pow(x_point - x_center, 2) + pow(y_point - y_center, 2))
#     if distance < radius:
#         print("The point lies inside the circle.")
#     elif distance == radius:
#         print("The point lies on the circle.")
#     else:
#         print("The point lies outside the circle.")
# try:
#     x_center = float(input("Enter the x-coordinate of the center of the circle: "))
#     y_center = float(input("Enter the y-coordinate of the center of the circle: "))
#     radius = float(input("Enter the radius of the circle: "))
#     x_point = float(input("Enter the x-coordinate of the point: "))
#     y_point = float(input("Enter the y-coordinate of the point: "))
#     check_point_position(x_center, y_center, radius, x_point, y_point)
# except ValueError:
#     print("Please enter valid numerical values.")



# def number_to_words(number):
#     words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
#              "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
#              "eighteen", "nineteen"]
#     if 0 <= number <= 19:
#         print(f"The number {number} in words is: {words[number]}")
#     else:
#         print("Please enter a number between 0 and 19.")
# try:
#     number = int(input("Enter a number between 0 and 19: "))
#     number_to_words(number)
# except ValueError:
#     print("Please enter a valid integer.")



# def get_grade(marks):
#     if marks == "NA":
#         return "NA"
#     elif 0 <= marks <= 39:
#         return "F"
#     elif 40 <= marks <= 44:
#         return "P"
#     elif 45 <= marks <= 49:
#         return "C"
#     elif 50 <= marks <= 54:
#         return "B"
#     elif 55 <= marks <= 59:
#         return "B+"
#     elif 60 <= marks <= 69:
#         return "A"
#     elif 70 <= marks <= 79:
#         return "A+"
#     elif 80 <= marks <= 100:
#         return "O"
#     else:
#         return "Invalid Marks"
# def calculate_results(subject1, subject2, subject3):
#     if subject1 <= 39 or subject2 <= 39 or subject3 <= 39:
#         result = "Fail"
#     else:
#         result = "Pass"
#     total = subject1 + subject2 + subject3
#     average = total / 3
#     print(f"Total Marks: {total}")
#     print(f"Average Marks: {average:.2f}")
#     print(f"Result: {result}")
#     print(f"Grade for Subject 1: {get_grade(subject1)}")
#     print(f"Grade for Subject 2: {get_grade(subject2)}")
#     print(f"Grade for Subject 3: {get_grade(subject3)}")
# try:
#     subject1 = int(input("Enter marks for Subject 1: "))
#     subject2 = int(input("Enter marks for Subject 2: "))
#     subject3 = int(input("Enter marks for Subject 3: "))
#     calculate_results(subject1, subject2, subject3)
# except ValueError:
#     print("Please enter valid integers for marks.")

