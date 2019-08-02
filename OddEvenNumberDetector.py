number = int(input(print("Enter a new number: ")))
mod = number%2
mult = number%4
if mod == 1:
    print("The number you entered is an odd number.")
elif mult == 0:
    print("The number entered is a multiple of 4.")
elif mod == 0:
    print("The number you entered is an even number.")

else:
    print("Thanks for playing this game.")
