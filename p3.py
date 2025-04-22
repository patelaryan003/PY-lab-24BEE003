
# def count_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in input_string:
#         if char in vowels:
#             count += 1
#     return count
# user_input = input("Enter a string: ")
# vowel_count = count_vowels(user_input)
# print(f"The number of vowels in the string is: {vowel_count}")



# def to_lowercase(input_string):
#     result = ""  
#     for char in input_string:
#         if 'A' <= char <= 'Z':
#             result += chr(ord(char) + 32)
#         else:
#             result += char
#     return result
# user_input = input("Enter a string: ")
# lowercase_string = to_lowercase(user_input)
# print("Lowercase string:", lowercase_string)



# def to_uppercase(input_string):
#     result = ""  
#     for char in input_string:
#         if 'a' <= char <= 'z':
#             result += chr(ord(char) - 32)
#         else:
#             result += char
#     return result
# user_input = input("Enter a string: ")
# uppercase_string = to_uppercase(user_input)
# print("Uppercase string:", uppercase_string)



# def to_togglecase(input_string):
#     result = "" 
#     for char in input_string:
#         if 'A' <= char <= 'Z':
#             result += chr(ord(char) + 32)
#         elif 'a' <= char <= 'z':
#             result += chr(ord(char) - 32)
#         else:
#             result += char
#     return result
# user_input = input("Enter a string: ")
# togglecase_string = to_togglecase(user_input)
# print("Toggle case string:", togglecase_string)




# def is_substring(string1, string2):
#     len1 = len(string1)
#     len2 = len(string2)
#     for i in range(len1 - len2 + 1):
#         match = True
#         for j in range(len2):
#             if string1[i + j] != string2[j]:
#                 match = False
#                 break
#         if match:
#             return True
#     return False
# main_string = input("Enter the main string: ")
# sub_string = input("Enter the substring to check: ")
# if is_substring(main_string, sub_string):
#     print(f'"{sub_string}" is present in "{main_string}".')
# else:
#     print(f'"{sub_string}" is not present in "{main_string}".')




# def remove_substring(main_string, sub_string):
#     result = ""  
#     i = 0
#     while i < len(main_string):
#         if main_string[i:i+len(sub_string)] == sub_string:
#             i += len(sub_string)
#         else:
#             result += main_string[i]
#             i += 1
#     return result
# main_string = input("Enter the main string: ")
# sub_string = input("Enter the string to remove: ")
# updated_string = remove_substring(main_string, sub_string)
# print("Updated string:", updated_string)




