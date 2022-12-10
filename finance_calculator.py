# Here we are creating a finance calculator
# One calculator is a investment calculator
# One is a home loan repayment calculator
"""
The user simply picks if they want an investment or a bond calculator. From here
they will be asked certain questions depending on which choice they make.
These questions will gather all vital information and calculate the answer.
"""

import math

# Asking user to choose between 2 choices
investment_or_bond = input("""
Choose either 'investment' or 'bond' from the menu below to proceed:      

investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on your home loan
                                                      """).lower()

interest_types = ("simple", "compound")


# Asking the user to input info if they picked investment
if investment_or_bond == "investment":

    # Asking how much they want to deposit
    deposit = int(input("How much are you depositing: "))

    # Rate should be divided by 100
    rate = int(input("What is your interest rate: "))
    rate = rate / 100

    # Asking how many years they want to invest for
    years = int(input("How many years do you plan on investing: "))

    # Asking user to pick simple or compound
    investment_interest = input("Do you want 'simple' or 'compound' interest: ")

# If user picked simple
    if investment_interest == "simple":

        # Calculating simple interest
        simple_interest = deposit * (1 + rate * years)

        # Printing compound interest along with the terms
        print(f"You will get back ${simple_interest} after {years} at {investment_interest}% "
              f" interest")

    # If user picked simple
    elif investment_interest == "compound":

        # Calculating compound interest
        compound_interest = deposit * math.pow((1 + rate), years)

        # Printing compound interest along with the terms
        print(f"You will get back ${round(compound_interest)} after {years} at {investment_interest}% "
              f" interest")

# Asking the user to input info if they picked investment
if investment_or_bond == "bond":

    # Asking for hte value of their house
    house_value = int(input("What is the value of the house: "))

    # This needs to be divided by 12 to obtain the monthly amount, as the amount is yearly
    house_interest = int(input("What is your interest rate: ")) / 12
    # Divide by 100 for percentage
    house_interest = house_interest / 100

    # Asking to give how many months they want to repay the bond
    bond_months = int(input("How many months do you plan to take to repy the bond: "))

    # Bond repayment formula
    bond_repayment = (house_interest * house_value) / (1 - (1 + house_interest)
                                                   ** (- bond_months))
    # Printing bond repayment each month
    print(f"You will have to pay ${round(bond_repayment)} each month")

else:
    print("Invalid input!!!!")

