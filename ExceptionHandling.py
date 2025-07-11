
try:
    number=int(input("Enter the Number: "))
    print(f"Answer: {10/number}")
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Dont put zero")
finally:
    print("Process Complete!")
    



print("Step 1")
print("Step 2")
print("Step 3")
print("Step 4")