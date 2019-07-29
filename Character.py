#ProgramThatAsksTheUserForTheirNameAndAgeAndCalculatesTheYearTheyWillBe100

print("Hello! ")
name = input("What is your name?" + " \n")
age = int(input("How old are you?" + " \n"))
print("Thank you. The information entered is being processed...")

year = str((2019 - age)+ 100)

print("You will be 100 years old in " + year + ".")
print("Thank you for using our service.")

#Version 2
number = int(input("Please enter a random number, " + name + ". \n"))
print(number * str(number))
