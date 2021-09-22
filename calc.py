#returns sum of num1 and num2
def add(num1, num2):
	return num1 + num2
#returns subtraction of num1 and num2
def subtract(num1, num2):
	return num1 - num2
#returns multiplication of num1 and num2
def multiply(num1, num2):
	return num1 * num2
#returns division of num1 and num2
def divide(num1, num2):
	return num1 / num2
    
def main():
    operation = input("What do you want to do (+, -, *, /)?")
    if(operation != '+' and operation !='-' and operation !='*' and operation !='/'):
        #invalid operation
        print("You must enter a valid operator!")
    else:
        var1 = int(input("Enter num1: "))
        var2 = int(input("Enter num2: "))
        if(operation == '+'):
            print(add(var1, var2))
        elif(operation == '-'):
            print(subtract(var1, var2))
        elif(operation == '*'):
            print(multiply(var1, var2))
        elif(operation == '/'):
            print(divide(var1, var2))

main()