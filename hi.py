print("hello world")

name = input("whats your name ? ")
print(f"Nice to meet you {name}")

number1 = input("Enter first number please: ")
number2 = input("Enter second number please: ")

sum = int(number1) + int(number2)
difference = int(number1) - int(number2)
product = int(number1) * int(number2)
quotient = int(number1) / int(number2)

print(f"Summ of two numbers : {sum}")
print(f"         difference : {difference}")
print(f"             product: {product}")
print(f"            quotient: {quotient}")

age = input("what is you age ? ")
print(f"Oh next year you will be{int(age)+1} years old")