# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# dict3 = {"e": 5, "f": 6}
# dict4 = {**dict1, **dict2, **dict3}
# print("Concatenated Dictionary:", dict4)
# 1




# my_dict = {}
# if not my_dict:
#     print("The dictionary is empty.")
# else:
#     print("The dictionary is not empty.")
# 2







# employees = [
#     {"Dept_No": 101, "Emp_Roll_No": 1, "Salary": 50000},
#     {"Dept_No": 102, "Emp_Roll_No": 2, "Salary": 60000},
#     {"Dept_No": 101, "Emp_Roll_No": 3, "Salary": 55000},
#     {"Dept_No": 103, "Emp_Roll_No": 4, "Salary": 45000},
#     {"Dept_No": 102, "Emp_Roll_No": 5, "Salary": 70000},
#     {"Dept_No": 103, "Emp_Roll_No": 6, "Salary": 48000},
#     {"Dept_No": 101, "Emp_Roll_No": 7, "Salary": 52000},
# ]
# dept_salaries = {}
# for emp in employees:
#     dept = emp["Dept_No"]
#     salary = emp["Salary"]
    
#     if dept not in dept_salaries:
#         dept_salaries[dept] = {"min": salary, "max": salary}
#     else:
#         dept_salaries[dept]["min"] = min(dept_salaries[dept]["min"], salary)
#         dept_salaries[dept]["max"] = max(dept_salaries[dept]["max"], salary)
# print("Department-wise Salary Range:")
# for dept, salaries in dept_salaries.items():
#     print(f"Dept {dept}: Min Salary = {salaries['min']}, Max Salary = {salaries['max']}")
# 3




# input_string = input("Enter a string: ")
# char_frequency = {}
# for char in input_string:
#     char_frequency[char] = char_frequency.get(char, 0) + 1
# print("Character Frequency Dictionary:", char_frequency)                                                                                                                                                                                                                                                                 









# grocery_prices = {
#     "apple": 2.5,
#     "banana": 1.2,
#     "milk": 3.0,
#     "bread": 2.0,
#     "eggs": 5.0
# }
# grocery_quantity = {
#     "apple": 4,
#     "banana": 6,
#     "milk": 2,
#     "bread": 1,
#     "eggs": 1
# }
# total_bill = 0
# for item in grocery_quantity:
#     if item in grocery_prices:
#         total_bill += grocery_quantity[item] * grocery_prices[item]
# print("Total Bill Amount: $", round(total_bill, 2))
# 5









