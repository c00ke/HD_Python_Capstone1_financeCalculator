# Finance Calculators

import math

print("Choose either the 'investment' or 'bond' calculator from the menu below to proceed:")

print("\ninvestment   - to calculate the amount of interest you'll earn on investment")
print("bond         - to calculate the amount you you'll have to pay on a home loan")

choice = (input("\nBond or Investment: ").lower())                                                      # Using lower() function to ensure input is always lowercase so that capitals don't affect selection

# Use if statement to ensure input is correct, else an error message will be displayed
# Writing the conditional statement to choose between investment or bond calculator

if choice == "investment":                                    
    print("\nYou have chosen the investment calculator")
    
    amount = float(input("\nHow much money will you be investing: R "))                                 # Using \n to move sentence to new line & the float function as it is currency we are working with, there will be decimals involved
    interest = float(input("What is the interest rate: "))                                              # Casting input str to float() as the input will be a number with decimals 
    years_inv = int(input("How many years will you be investing for: "))                                # Casting input str to int() as the input  will be a whole number
    type_int = input("Would you like simple or compound interest? (Simple or Compound): ").lower()      # Using lower() function to ensure input is always lowercase so that capitals don' affect selections

    if type_int == "simple":                                                                            # Nesting another if function to differ between simple or compound interest
        total = amount * (1 + (interest/100) * years_inv)
        print("\nWith simple interest, your investment will be equal to: " + str(total))                # Using str() to cast the int to a string so that I can concatenate the sentence

    elif type_int == "compound":
        total = amount * math.pow((1 + (interest/100)), years_inv)
        print("\nWith compound interest, your investment will be equal to: " + str(round((total), 2)))  # Using round() function to round off to two decimal places, str() to cast int to a string for concatenation

    else:
        print("Error: please only select compound or simple interest")                                  # Error message if neither compound nor simple interest is selected
    
elif choice == "bond":
    print("\nYou have chosen the bond calculator")

    house_val = float(input("\nWhat is the present value of the house: R "))                            # Casting input str to float() as the input will be a number with decimals
    interest = float(input("What is the interest rate: "))
    time = int(input("How many months will you take to repay the bond: "))                              # Casting input str to int() as the input  will be a whole number
    i = (interest/12) / 100                                                                             # Working out the monthly interest rate percentage

    total = (i * house_val) / (1 - (1 + i)**(-time))
    print("Your monthly bond repayment will be R " + str(round(total,2)))                                # str() to cast int to a string for concatenation, using Round() to round off to 2 decimal

else:
    print("Error: please only select the investment or the bond calculator.")

# End of program

    
