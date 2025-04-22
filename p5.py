# import random
# odd_numbers = random.sample(range(1, 100, 2), 5)
# print("Original list of 5 odd integers:", odd_numbers)
# even_numbers = random.sample(range(2, 100, 2), 4)
# print("List of 4 even integers:", even_numbers)
# odd_numbers[2] = even_numbers
# print("List after replacing third element with even integers:", odd_numbers)
# flattened_list = []
# for item in odd_numbers:
#     if isinstance(item, list):
#         flattened_list.extend(item)
#     else:
#         flattened_list.append(item)
# print("Flattened list:", flattened_list)
# flattened_list.sort()
# print("Sorted flattened list:", flattened_list)




# import random
# random_numbers = [random.randint(1, 50) for _ in range(20)]
# print("Generated list of random numbers:", random_numbers)
# user_input = int(input("Enter a number to find its positions: "))
# positions = [index for index, value in enumerate(random_numbers) if value == user_input]
# if positions:
#     print(f"The number {user_input} is found at positions: {positions}")
# else:
#     print(f"The number {user_input} is not found in the list.")




# import random
# random_numbers = [random.randint(1, 30) for _ in range(50)]
# print("Original list with duplicates:", random_numbers)
# unique_numbers = list(set(random_numbers))
# print("List after removing duplicates:", unique_numbers)





# import random
# random_numbers = [random.randint(-50, 50) for _ in range(30)]
# print("Original list of random numbers:", random_numbers)
# positive_numbers = [num for num in random_numbers if num > 0]
# negative_numbers = [num for num in random_numbers if num < 0]
# print("List of positive numbers:", positive_numbers)
# print("List of negative numbers:", negative_numbers)






# string_list = ["hello", "world", "python", "programming", "code"]
# print("Original list:", string_list)
# uppercase_list = [s.upper() for s in string_list]
# print("List with uppercase strings:", uppercase_list)






# fahrenheit_temps = [32, 50, 77, 104, 212]
# print("Temperatures in Fahrenheit:", fahrenheit_temps)
# celsius_temps = [(temp - 32) * 5/9 for temp in fahrenheit_temps]
# print("Equivalent temperatures in Celsius:", celsius_temps)






# stack = []
# def push():
#     element = input("Enter the element to push: ")
#     stack.append(element)
#     print(f"{element} pushed onto the stack.")
# def pop():
#     if not stack:
#         print("Stack is empty! Nothing to pop.")
#     else:
#         popped_element = stack.pop()
#         print(f"Popped element: {popped_element}")
# def display():
#     if not stack:
#         print("Stack is empty!")
#     else:
#         print("Stack elements (top to bottom):")
#         for i in reversed(stack):
#             print(i)
# while True:
#     print("\nStack Operations Menu:")
#     print("1. Push")
#     print("2. Pop")
#     print("3. Display")
#     print("4. Exit")
#     choice = input("Enter your choice (1-4): ")
#     if choice == '1':
#         push()
#     elif choice == '2':
#         pop()
#     elif choice == '3':
#         display()
#     elif choice == '4':
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice! Please enter a valid option.")







# queue = []
# def enqueue():
#     element = input("Enter the element to enqueue: ")
#     queue.append(element)
#     print(f"{element} added to the queue.")
# def dequeue():
#     if not queue:
#         print("Queue is empty! Nothing to dequeue.")
#     else:
#         removed_element = queue.pop(0)
#         print(f"Dequeued element: {removed_element}")
# def display():
#     if not queue:
#         print("Queue is empty!")
#     else:
#         print("Queue elements (front to rear):", queue)
# while True:
#     print("\nQueue Operations Menu:")
#     print("1. Enqueue")
#     print("2. Dequeue")
#     print("3. Display")
#     print("4. Exit")
#     choice = input("Enter your choice (1-4): ")
#     if choice == '1':
#         enqueue()
#     elif choice == '2':
#         dequeue()
#     elif choice == '3':
#         display()
#     elif choice == '4':
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice! Please enter a valid option.")







# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [3, 5, 7, 9]
# print("First list:", list1)
# print("Second list:", list2)
# difference_list = [num for num in list1 if num not in list2]
# print("Numbers in first list but not in second list:", difference_list)