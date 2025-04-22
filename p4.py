
# num = int(input("Enter a positive integer: "))
# if num < 0:
#     print("Please enter a positive integer.")
# else:
#     total = 0
#     for i in range(1, num + 1):
#         total += i
#     print(f"The sum of the first {num} natural numbers is: {total}")


# n=5
# fact=1
# while n:
#     fact=fact*n
#     n=n-1
#     print(fact)



# num = int(input("Enter a number: "))
# print(f"Multiplication Table for {num}:")
# for i in range(1, 11): 
#     print(f"{num} x {i} = {num * i}")




# text = input("Enter a string: ")
# alphabet_count = 0
# digit_count = 0
# for char in text:
#     if char.isalpha():
#         alphabet_count += 1
#     elif char.isdigit():
#         digit_count += 1
# print(f"Number of Alphabets: {alphabet_count}")
# print(f"Number of Digits: {digit_count}")




# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a Prime number.")
# else:
#     print(f"{num} is NOT a Prime number.")




# def is_perfect(n):
#     if n < 1:
#         return False
#     sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
#     return sum_of_divisors == n
# num = int(input("Enter a number: "))
# if is_perfect(num):
#     print(f"{num} is a Perfect number.")
# else:
#     print(f"{num} is NOT a Perfect number.")




# def is_armstrong(n):
#     num_str = str(n)
#     num_digits = len(num_str)
#     sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
#     return sum_of_powers == n
# num = int(input("Enter a number: "))
# if is_armstrong(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is NOT an Armstrong number.")





# def is_palindrome(n):
#     return str(n) == str(n)[::-1] 
# num = int(input("Enter a number: "))
# if is_palindrome(num):
#     print(f"{num} is a Palindrome number.")
# else:
#     print(f"{num} is NOT a Palindrome number.")





# def is_automorphic(n):
#     squared = n ** 2 
#     return str(squared).endswith(str(n)) 
# num = int(input("Enter a number: "))
# if is_automorphic(num):
#     print(f"{num} is an Automorphic number.")
# else:
#     print(f"{num} is NOT an Automorphic number.")




# def find_pythagorean_triplets(limit):
#     triplets = []
#     for a in range(1, limit + 1):
#         for b in range(a, limit + 1):  
#             c = (a*2 + b*2) ** 0.5 
#             if c.is_integer() and c <= limit:  
#                 triplets.append((a, b, int(c)))  
#     return triplets
# limit = 30
# triplets = find_pythagorean_triplets(limit)
# print("Pythagorean Triplets (a, b, c) with side length ≤ 30:")
# for triplet in triplets:
#     print(triplet)







# def print_24_hours():
#     for hour in range(24):
#         if hour == 0:
#             print(f"{hour:02d}:00 - Midnight")
#         elif hour == 12:
#             print(f"{hour:02d}:00 - Noon")
#         elif hour < 12:
#             print(f"{hour:02d}:00 - {hour} AM")
#         else:
#             print(f"{hour:02d}:00 - {hour - 12} PM")
# print_24_hours()





# import math  
# def combination(n, r):
#     return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
# n = int(input("Enter value of n: "))
# r = int(input("Enter value of r: "))
# if r > n or n < 0 or r < 0:
#     print("Invalid input! r should be ≤ n and both should be non-negative.")
# else:
#     print(f"{n}C{r} (Combination) = {combination(n, r)}")





# import math  
# def permutation(n, r):
#     return math.factorial(n) // math.factorial(n - r)
# n = int(input("Enter value of n: "))
# r = int(input("Enter value of r: "))
# if r > n or n < 0 or r < 0:
#     print("Invalid input! r should be ≤ n and both should be non-negative.")
# else:
#     print(f"{n}P{r} (Permutation) = {permutation(n, r)}")




# import math  
# def factorial(n):
#     return math.factorial(n)
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers!")
# else:
#     print(f"Factorial of {num} is {factorial(num)}")






# def print_reverse_natural_numbers(n):
#     for i in range(n, 0, -1):
#         print(i, end=" ")
# N = int(input("Enter a number (N): "))
# if N <= 0:
#     print("Please enter a positive natural number!")
# else:
#     print(f"Natural numbers from {N} to 1 in reverse order:")
#     print_reverse_natural_numbers(N)





# def fibonacci(n):
#     fib_series = [0, 1]  
#     for i in range(2, n):
#         next_term = fib_series[-1] + fib_series[-2]
#         fib_series.append(next_term)
#     return fib_series[:n] 
# N = int(input("Enter the number of terms (N): "))
# if N <= 0:
#     print("Please enter a positive integer!")
# else:
#     print(f"First {N} numbers of the Fibonacci series:")
#     print(fibonacci(N))




# import math 
# def sin_taylor_series(x, terms=10):
#     sin_x = 0  # 
#     for n in range(terms):
#         term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
#         sin_x += term
#     return sin_x
# degrees = float(input("Enter the angle in degrees: "))
# radians = degrees * (math.pi / 180) 
# sin_value = sin_taylor_series(radians, terms=10)
# print(f"sin({degrees}°) ≈ {sin_value}")


