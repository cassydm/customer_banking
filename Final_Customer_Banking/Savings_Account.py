#import account class from account.py
from AccountClass import Account
# Create an instance of the `Account` class and pass in the balance and interest parameters.
def create_savings_account(balance,interest,months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    #creating the instance of Account
    my_account=Account(balance,interest)
    #printing intitial balance information
    print(f"Your Savings account details:")
    print("-"*42)
    print(f"Starting balance: ${my_account.balance:,.2f}")
    print(f"APR: {interest:.2f}%")
    print(f"Months: {months}")
    print("-"*42)
    #performing calculations and storing as variables
    earned_interest = balance * (interest / 100 * months / 12)
    updated_balance = balance+earned_interest
    #using the Account class functions to update the balance and interest earned.
    my_account.set_interest(earned_interest)
    my_account.set_balance(updated_balance)
    #printing the information for the user
    print(f"Earned interest on ${balance:,.2f} after {months} months: ${my_account.interest:,.2f}")
    print(f"Your new balance is ${my_account.balance:,.2f}")
    print("~"*42)
    #returning account instance for input function
    return my_account