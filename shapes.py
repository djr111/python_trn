import math
# circle area 
r = input("Please enter the radius of the circle  ")

circle = math.pi * float(r)**2

print(f"The circle area with radius : {r} = {circle:.2f}")

#trinagle area 
b = input("Please enter the base of the triangle  ")
h = input("Please enter the height of the triangle  ")

triangle = (float(b) * float(h)) / 2

print(f"The triangle area with base {b} and height {h}  = {triangle:.2f}")

#rectangle area

l = input("Please enter the lenght of the rectangle  ")
w = input("Please enter the width of the rectangle  ")

rectangle = float(l) * float(w)

print(f"The rectangle area with lenght {l} and width {w}  = {rectangle:.2f}")