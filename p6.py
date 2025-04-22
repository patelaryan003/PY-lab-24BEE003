# def count_boys_girls(names_list):
#     boys_count = sum(1 for name in names_list if isinstance(name, tuple))
#     girls_count = sum(1 for name in names_list if isinstance(name, str))
#     return boys_count, girls_count
# names = [("aryan",), "princy", ("deep",), "hatvi", ("dev",), "diya"]
# boys, girls = count_boys_girls(names)
# print(f"Number of boys: {boys}")
# print(f"Number of girls: {girls}")



# def separate_student_data(students):
#     roll_nos = [student[0] for student in students]
#     names = [student[1] for student in students]
#     ages = [student[2] for student in students]
#     return roll_nos, names, ages
# students = [(101, "aryan", 20), (102, "dev", 22), (103, "deep", 21)]
# roll_numbers, names, ages = separate_student_data(students)
# print("Roll Numbers:", roll_numbers)
# print("Names:", names)
# print("Ages:", ages)




# from datetime import date
# def days_between_dates(date1, date2):
#     d1 = date(date1[2], date1[1], date1[0]) 
#     d2 = date(date2[2], date2[1], date2[0])  
#     return abs((d2 - d1).days) 
# date1 = (10, 2, 2025)  
# date2 = (25, 2, 2025) 
# difference = days_between_dates(date1, date2)
# print(f"Number of days between {date1} and {date2}: {difference}")





# food_items = [("dal", 150), ("paneer", 300), ("butter milk", 200), ("rice", 100), ("roti", 80)]
# food_items.sort(key=lambda item: item[1], reverse=True)
# print("Sorted food items (by price):")
# for item in food_items:
#     print(item)
# removed_item = food_items.pop(0)  
# print("\nAfter removing the most expensive item:")
# for item in food_items:
#     print(item)




# def remove_empty_tuples(tuples_list):
#     return [tup for tup in tuples_list if tup]  
# tuples_list = [(1, 2), (), (3, 4, 5), (), ("Hello",), ()]
# filtered_list = remove_empty_tuples(tuples_list)
# print("Original list:", tuples_list)
# print("List after removing empty tuples:", filtered_list)




# def modify_tuple(tup, index, new_value):
#     temp_list = list(tup) 
#     temp_list[index] = new_value  
#     return tuple(temp_list)  
# my_tuple = (10, 20, 30, 40)
# modified_tuple = modify_tuple(my_tuple, 2, 99)
# print("Original Tuple:", my_tuple)
# print("Modified Tuple:", modified_tuple)




# def delete_tuple_element(tup, index):
#     temp_list = list(tup)  
#     del temp_list[index]   
#     return tuple(temp_list) 
# my_tuple = (10, 20, 30, 40, 50)
# modified_tuple = delete_tuple_element(my_tuple, 2)
# print("Original Tuple:", my_tuple)
# print("Modified Tuple:", modified_tuple)
