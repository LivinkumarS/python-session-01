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

marks=float(input("Enter Your Mark"))
if 90<= marks <=100:
    print("Grade O")
elif 80<= marks <90:
    print("Grade A+")
elif 70<= marks <80:
    print("Grade A")
elif 60<= marks <70:
    print("Grade B+")
elif 50<= marks <60:
    print("Grade B")
elif 0<= marks <50:
    print("Fail")
else:
    print("Invalid Input")