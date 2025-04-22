# class complexnum:
#     def number():
#      x = complex(5,7)
#      print(x)

# hello=complexnum
# hello.number ()




# class complexnum:
#     def add():
#         x = complex(3,5)
#         y = complex(6,9)
#         sum=x+y
#         print(sum)
# hello=complexnum
# hello.add ()




# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __str__(self):
#         # String representation
#         return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

#     def __add__(self, other):
#         # (a + bi) + (c + di) = (a+c) + (b+d)i
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)

#     def __sub__(self, other):
#         # (a + bi) - (c + di) = (a-c) + (b-d)i
#         return ComplexNumber(self.real - other.real, self.imag - other.imag)

#     def __mul__(self, other):
#         # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
#         real = self.real * other.real - self.imag * other.imag
#         imag = self.real * other.imag + self.imag * other.real
#         return ComplexNumber(real, imag)

#     def __truediv__(self, other):
#         # (a + bi) / (c + di) = [(ac + bd) + (bc - ad)i] / (c^2 + d^2)
#         denominator = other.real**2 + other.imag**2
#         if denominator == 0:
#             raise ZeroDivisionError("Cannot divide by zero-valued complex number")
#         real = (self.real * other.real + self.imag * other.imag) / denominator
#         imag = (self.imag * other.real - self.real * other.imag) / denominator
#         return ComplexNumber(real, imag)


# # Example usage
# if __name__ == "__main__":
#     c1 = ComplexNumber(4, 5)
#     c2 = ComplexNumber(2, -3)

#     print(f"First Complex Number: {c1}")
#     print(f"Second Complex Number: {c2}")

#     print(f"Addition: {c1 + c2}")
#     print(f"Subtraction: {c1 - c2}")
#     print(f"Multiplication: {c1 * c2}")
#     print(f"Division: {c1 / c2}")







# class Matrix3x3:
#     def __init__(self, data):
#         if len(data) != 3 or any(len(row) != 3 for row in data):
#             raise ValueError("Matrix must be 3x3.")
#         self.data = data

#     def __str__(self):
#         return "\n".join(["\t".join(map(str, row)) for row in self.data])

#     def __add__(self, other):
#         result = [
#             [self.data[i][j] + other.data[i][j] for j in range(3)]
#             for i in range(3)
#         ]
#         return Matrix3x3(result)

#     def __mul__(self, other):
#         result = [
#             [sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)]
#             for i in range(3)
#         ]
#         return Matrix3x3(result)

#     def transpose(self):
#         result = [
#             [self.data[j][i] for j in range(3)] for i in range(3)
#         ]
#         return Matrix3x3(result)


# # Example usage
# if __name__ == "__main__":
#     mat1 = Matrix3x3([
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ])

#     mat2 = Matrix3x3([
#         [9, 8, 7],
#         [6, 5, 4],
#         [3, 2, 1]
#     ])

#     print("Matrix 1:")
#     print(mat1)
#     print("\nMatrix 2:")
#     print(mat2)

#     print("\nMatrix Addition:")
#     print(mat1 + mat2)

#     print("\nMatrix Multiplication:")
#     print(mat1 * mat2)

#     print("\nTranspose of Matrix 1:")
#     print(mat1.transpose())






# import math

# class Solid:
#     def surface_area(self):
#         raise NotImplementedError("Subclass must implement this method")

#     def volume(self):
#         raise NotImplementedError("Subclass must implement this method")


# class Sphere(Solid):
#     def __init__(self, radius):
#         self.radius = radius

#     def surface_area(self):
#         return 4 * math.pi * self.radius ** 2

#     def volume(self):
#         return (4/3) * math.pi * self.radius ** 3


# class Cube(Solid):
#     def __init__(self, side):
#         self.side = side

#     def surface_area(self):
#         return 6 * self.side ** 2

#     def volume(self):
#         return self.side ** 3


# class Cylinder(Solid):
#     def __init__(self, radius, height):
#         self.radius = radius
#         self.height = height

#     def surface_area(self):
#         return 2 * math.pi * self.radius * (self.radius + self.height)

#     def volume(self):
#         return math.pi * self.radius ** 2 * self.height


# # Example usage
# if __name__ == "__main__":
#     # Create objects
#     sphere = Sphere(radius=5)
#     cube = Cube(side=3)
#     cylinder = Cylinder(radius=4, height=7)

#     print("Sphere:")
#     print(f"Surface Area: {sphere.surface_area():.2f}")
#     print(f"Volume: {sphere.volume():.2f}\n")

#     print("Cube:")
#     print(f"Surface Area: {cube.surface_area():.2f}")
#     print(f"Volume: {cube.volume():.2f}\n")

#     print("Cylinder:")
#     print(f"Surface Area: {cylinder.surface_area():.2f}")
#     print(f"Volume: {cylinder.volume():.2f}")







# import math

# # Base class
# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclasses must implement this method.")

#     def perimeter(self):
#         raise NotImplementedError("Subclasses must implement this method.")


# # Circle class
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):  # circumference
#         return 2 * math.pi * self.radius


# # Square class
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

#     def perimeter(self):
#         return 4 * self.side


# # Equilateral Triangle class
# class EquilateralTriangle(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return (math.sqrt(3) / 4) * self.side ** 2

#     def perimeter(self):
#         return 3 * self.side


# # Example usage
# if __name__ == "__main__":
#     circle = Circle(radius=5)
#     square = Square(side=4)
#     triangle = EquilateralTriangle(side=6)

#     print("Circle:")
#     print(f"Perimeter (Circumference): {circle.perimeter():.2f}")
#     print(f"Area: {circle.area():.2f}\n")

#     print("Square:")
#     print(f"Perimeter: {square.perimeter():.2f}")
#     print(f"Area: {square.area():.2f}\n")

#     print("Equilateral Triangle:")
#     print(f"Perimeter: {triangle.perimeter():.2f}")
#     print(f"Area: {triangle.area():.2f}")








# class Time:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         # Normalize time automatically
#         total_seconds = hours * 3600 + minutes * 60 + seconds
#         self.hours = (total_seconds // 3600) % 24
#         self.minutes = (total_seconds % 3600) // 60
#         self.seconds = total_seconds % 60

#     def __str__(self):
#         return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

#     def to_seconds(self):
#         return self.hours * 3600 + self.minutes * 60 + self.seconds

#     @staticmethod
#     def from_seconds(total_seconds):
#         return Time(0, 0, total_seconds)

#     def __add__(self, other):
#         return Time.from_seconds(self.to_seconds() + other.to_seconds())

#     def __sub__(self, other):
#         diff_seconds = abs(self.to_seconds() - other.to_seconds())
#         return Time.from_seconds(diff_seconds)


# # Example usage
# if __name__ == "__main__":
#     t1 = Time(2, 45, 30)
#     t2 = Time(1, 20, 50)

#     print("Time 1:", t1)
#     print("Time 2:", t2)

#     print("\nAddition of Time 1 and Time 2:")
#     print(t1 + t2)

#     print("\nSubtraction of Time 1 and Time 2:")
#     print(t1 - t2)

#     print("\nTotal seconds in Time 1:", t1.to_seconds())
#     print("Total seconds in Time 2:", t2.to_seconds())

#     print("\nCreating Time from 5000 seconds:")
#     t3 = Time.from_seconds(5000)
#     print(t3)







# class Date:
#     def __init__(self, day, month, year):
#         self.date = [day, month, year]

#     def __str__(self):
#         return f"{self.date[0]:02d}/{self.date[1]:02d}/{self.date[2]}"

#     def __eq__(self, other):
#         return self.date == other.date


# # Example usage
# if __name__ == "__main__":
#     date1 = Date(22, 4, 2025)
#     date2 = Date(22, 4, 2025)
#     date3 = Date(1, 1, 2024)

#     print("Date 1:", date1)
#     print("Date 2:", date2)
#     print("Date 3:", date3)

#     print("\nIs Date 1 equal to Date 2?", date1 == date2)  # True
#     print("Is Date 1 equal to Date 3?", date1 == date3)    # False







# class Weather:
#     def __init__(self, parameters):
#         # Store weather parameters in a list
#         self.parameters = parameters

#     def __contains__(self, item):
#         # This method makes the 'in' operator work
#         return item in self.parameters

#     def __str__(self):
#         return f"Weather Parameters: {', '.join(self.parameters)}"


# # Example usage
# if __name__ == "__main__":
#     today_weather = Weather(["temperature", "humidity", "wind", "pressure", "visibility"])

#     print(today_weather)

#     print("\nChecking for parameters:")
#     print("Is 'temperature' in today's weather?", 'temperature' in today_weather)  # True
#     print("Is 'rainfall' in today's weather?", 'rainfall' in today_weather)        # False






# class MyString:
#     def __init__(self, text):
#         self.text = text

#     def __str__(self):
#         return self.text

#     # Overloaded += operator
#     def __iadd__(self, other):
#         if isinstance(other, MyString):
#             self.text += other.text
#         elif isinstance(other, str):
#             self.text += other
#         else:
#             raise TypeError("Can only concatenate MyString or str")
#         return self

#     # Convert to lowercase
#     def toLower(self):
#         self.text = self.text.lower()

#     # Convert to uppercase
#     def toUpper(self):
#         self.text = self.text.upper()


# # Example usage
# if __name__ == "__main__":
#     s1 = MyString("Hello")
#     s2 = MyString(" World")

#     print("Original Strings:")
#     print("s1:", s1)
#     print("s2:", s2)

#     s1 += s2
#     print("\nAfter Concatenation (s1 += s2):")
#     print("s1:", s1)

#     s1.toLower()
#     print("\nAfter toLower():")
#     print("s1:", s1)

#     s1.toUpper()
#     print("\nAfter toUpper():")
#     print("s1:", s1)
