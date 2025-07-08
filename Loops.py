# for i in range(0,10):
#     print(i)

# secret=33
# gotAnswer=False

# while not gotAnswer:
#     inp=int(input("Guess the number Clue(0-100): "))
#     if(secret==inp):
#         print("You won!")
#         gotAnswer=True
#     else:
#         print("Try again")

# marks=float(input("Enter Your Mark"))
# if 90<= marks <=100:
#     print("Grade O")
# elif 80<= marks <90:
#     print("Grade A+")
# elif 70<= marks <80:
#     print("Grade A")
# elif 60<= marks <70:
#     print("Grade B+")
# elif 50<= marks <60:
#     print("Grade B")
# elif 0<= marks <50:
#     print("Fail")
# else:
#     print("Invalid Input")


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:" , bmi) 

if bmi < 18.5:
    print("You are Underweight")
elif 18.5 <= bmi < 25:
    print("You are Normal weight")
elif 25 <= bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")