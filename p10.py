# import csv
# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 30, 'New York'],
#     ['Bob', 25, 'Los Angeles'],
#     ['Charlie', 35, 'Chicago'],
#     ['David', 40, 'San Francisco']
# ]
# with open('output.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
# print("CSV file 'output.csv' created successfully!")




# import csv
# with open('students.csv', mode='r') as file:
#     reader = csv.reader(file)    
#     header = next(reader)    
#     students_data = []
#     for row in reader:
#         student_dict = {
#             'Roll No': row[0],          
#             'Name': row[1],              
#             'Subject 1': int(row[2]),   
#             'Subject 2': int(row[3]),    
#             'Subject 3': int(row[4]),     
#             'Total': int(row[2]) + int(row[3]) + int(row[4])  
#         }
#         students_data.append(student_dict)
# for student in students_data:
#     print(student)





# def create_vcard():
#     name = input("Enter the full name: ")
#     phone = input("Enter the phone number: ")
#     email = input("Enter the email address: ")
#     address = input("Enter the address: ")    
#     vcard_data = f"""BEGIN:VCARD
# VERSION:3.0
# FN:{name}
# TEL:{phone}
# EMAIL:{email}
# ADR:{address}
# END:VCARD"""    
#     file_name = name.replace(" ", "_") + "_contact.vcf" 
#     with open(file_name, "w") as file:
#         file.write(vcard_data)
#     print(f"vCard created successfully! You can store this contact in your mobile as '{file_name}'.")
# create_vcard()





# import os
# import shutil
# def create_subdirectory_and_copy_file():
#     source_file = 'path/to/source/subdirectory/filename.txt'
#     destination_dir = 'path/to/new/subdirectory' 




# def copy_and_convert_to_uppercase(source_file, destination_file):
#     try:
#         with open(source_file, 'r') as source:
#             content = source.read()
#         content_upper = content.upper()
#         with open(destination_file, 'w') as destination:
#             destination.write(content_upper)
#         print(f"Contents copied and converted to uppercase successfully from '{source_file}' to '{destination_file}'.")
#     except FileNotFoundError:
#         print(f"Error: The source file '{source_file}' was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# source_file = 'source.txt' 
# destination_file = 'destination.txt'  
# copy_and_convert_to_uppercase(source_file, destination_file)





# def merge_lines_alternatively(file1, file2, output_file):
#     try:
#         with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as output:
#             lines1 = f1.readlines()
#             lines2 = f2.readlines()
#             i, j = 0, 0
#             while i < len(lines1) or j < len(lines2):
#                 if i < len(lines1):
#                     output.write(lines1[i])
#                     i += 1
#                 if j < len(lines2):
#                     output.write(lines2[j])  
#                     j += 1
#         print(f"Lines merged successfully into '{output_file}'.")
#     except FileNotFoundError as e:
#         print(f"Error: {e.filename} not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# file1 = 'file1.txt' 
# file2 = 'file2.txt' 
# output_file = 'merged_output.txt'
# merge_lines_alternatively(file1, file2, output_file)






# import pickle
# from datetime import datetime
# class Employee:
#     def __init__(self, empcode, empname, date_of_joining, salary):
#         self.empcode = empcode
#         self.empname = empname
#         self.date_of_joining = date_of_joining
#         self.salary = salary

#     def __str__(self):
#         return f"Employee Code: {self.empcode}, Name: {self.empname}, Date of Joining: {self.date_of_joining}, Salary: {self.salary}"
# def serialize_employee(employee, filename):
#     with open(filename, 'wb') as file:
#         pickle.dump(employee, file) 
#     print(f"Employee object")






# import re
# def remove_specific_words(input_file, output_file):
#     words_to_remove = ['a', 'the', 'an']
#     try:
#         with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
#             content = infile.read()
#             for word in words_to_remove:
#                 content = re.sub(rf'\b{word}\b', ' ', content, flags=re.IGNORECASE)
#             outfile.write(content)
#         print(f"Modified content saved to '{output_file}'.")
#     except FileNotFoundError:
#         print(f"Error: The file '{input_file}' was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# input_file = 'input.txt' 
# output_file = 'output.txt' 
# remove_specific_words(input_file, output_file)