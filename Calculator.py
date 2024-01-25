import time

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nInput the number only: "))
try: 
    if choice == 1:
        print('Addition')
        num1 = int(input("Input first number"))
        num2 = int(input("Input second number")) 
        final = num1 + num2
        print("Total " + str(int(final)))
except ValueError: 
    print("Enter a number")    

try: 
      if choice == 2: 
        print('Subtraction')
        num1 = int(input("Input first number"))
        num2 = int(input("Input second number")) 
        final = num1 - num2
        print("Total " + str(int(final)))
except ValueError: 
    print("Enter a number")    

try: 
      if choice == 3: 
        print('Multiplication')
        num1 = int(input("Input first number"))
        num2 = int(input("Input second number")) 
        final = num1 * num2
        print("Total " + str(int(final)))
except ValueError: 
    print("Enter a number")    

try: 
      if choice == 4: 
        print('Division')
        num1 = int(input("Input first number"))
        num2 = int(input("Input second number")) 
        final = num1 / num2
        print("Total " + str(int(final)))
except ValueError: 
    print("Enter a number")    

print()    
time.sleep(60)