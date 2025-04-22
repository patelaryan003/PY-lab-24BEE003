# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict3 = {'e': 5, 'f': 6}
# concatenated_dict = {**dict1, **dict2, **dict3}
# print("Concatenated Dictionary:", concatenated_dict)






# dictionary = {'a':1, 'b':2}
# if not dictionary:
#     print("The dictionary is empty.")
# else:
#     print("The dictionary is not empty.")



# from collections import defaultdict
# employees = [
#     {'dept_no': 101, 'roll_no': 1, 'salary': 50000},
#     {'dept_no': 101, 'roll_no': 2, 'salary': 60000},
#     {'dept_no': 102, 'roll_no': 3, 'salary': 70000},
#     {'dept_no': 102, 'roll_no': 4, 'salary': 80000},
#     {'dept_no': 103, 'roll_no': 5, 'salary': 55000},
#     {'dept_no': 103, 'roll_no': 6, 'salary': 75000}
# ]
# dept_salaries = defaultdict(list)
# for emp in employees:
#     dept_salaries[emp['dept_no']].append(emp['salary'])
# for dept, salaries in dept_salaries.items():
#     print(f"Department {dept}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")







# input_string = input("Enter a string: ")
# char_frequency = {}
# for char in input_string:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# print("Character Frequency:", char_frequency)





# grocery_prices = {
#     'apple': 2.5,
#     'banana': 1.2,
#     'milk': 3.0,
#     'bread': 2.0,
#     'eggs': 5.0
# }
# grocery_quantity = {
#     'apple': 4,
#     'banana': 6,
#     'milk': 2,
#     'bread': 1,
#     'eggs': 1
# }
# total_bill = sum(grocery_prices[item] * grocery_quantity[item] for item in grocery_prices if item in grocery_quantity)
# print("Total Bill:", total_bill)
