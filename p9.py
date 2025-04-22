# def prime_factors(n, divisor=2):
#     if n == 1:
#         return []
#     if n % divisor == 0:
#         return [divisor] + prime_factors(n // divisor, divisor)
#     else:
#         return prime_factors(n, divisor + 1)
# number = int(input("Enter a positive integer: "))
# if number > 1:
#     factors = prime_factors(number)
#     print(f"The prime factors of {number} are: {factors}")
# else:
#     print("Please enter a positive integer greater than 1.")





# def to_binary(n):
#     if n == 0:
#         return ''
#     else:
#         return to_binary(n // 2) + str(n % 2)
# number = int(input("Enter a positive integer: "))
# if number > 0:
#     binary_representation = to_binary(number)
#     if binary_representation == '':
#         binary_representation = '0'
#     print(f"The binary equivalent of {number} is: {binary_representation}")
# else:
#     print("Please enter a positive integer greater than 0.")





# def count_vowels(s):
#     if len(s) == 0:
#         return 0
#     vowels = 'aeiouAEIOU'
#     if s[0] in vowels:
#         return 1 + count_vowels(s[1:]) 
#     else:
#         return count_vowels(s[1:])
# input_string = input("Enter a string: ")
# vowel_count = count_vowels(input_string)
# print(f"The number of vowels in the string is: {vowel_count}")




# def reverse_list(lst):
#     if len(lst) == 0:
#         return lst
#     else:
#         return reverse_list(lst[1:]) + [lst[0]]
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# reversed_numbers = reverse_list(numbers)
# print(f"The reversed list is: {reversed_numbers}")




# def power(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * power(a, b - 1)
# a = int(input("Enter the base (a): "))
# b = int(input("Enter the exponent (b): "))
# result = power(a, b)
# print(f"{a} raised to the power of {b} is: {result}")





# def sanitize_list(lst):

#     if len(lst) == 0:
#         return []
#     if lst[0] < 0:
#         return [0] + sanitize_list(lst[1:]) 
#     else:
#         return [lst[0]] + sanitize_list(lst[1:]) 
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# sanitized_numbers = sanitize_list(numbers)
# print(f"The sanitized list is: {sanitized_numbers}")






# def compute_sum_and_count(lst):
#     if len(lst) == 0:
#         return 0, 0
#     current_sum, current_count = compute_sum_and_count(lst[1:])
#     return lst[0] + current_sum, 1 + current_count
# def average(lst):
#     total_sum, total_count = compute_sum_and_count(lst)
#     if total_count == 0:
#         return 0
#     else:
#         return total_sum / total_count
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# avg = average(numbers)
# print(f"The average of the numbers is: {avg}")








# def string_length(s):
#     if s == "":
#         return 0
#     else:
#         return 1 + string_length(s[1:])
# input_string = input("Enter a string: ")
# length = string_length(input_string)
# print(f"The length of the string is: {length}")