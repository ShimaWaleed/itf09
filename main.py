# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = add(num1, num2)
diff_result = sub(num1, num2)
prod_result = mul(num1, num2)
div_result = div(num1, num2)

print("Sum:", add(num1,num2))
print("sub:", sub(num1,num2))
print("mul:", mul(num1,num2))
print("div:", div(num1,num2))