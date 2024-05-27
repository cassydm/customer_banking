#import account class from account.py
from AccountClass import Account
def create_cd_account(balance, interest, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    #creating the instance of Account
    my_cd=Account(balance,interest)
    #printing intitial balance information
    print(f"Your CD account details:")
    print("-"*42)
    print(f"Starting balance: ${my_cd.balance:,.2f}")
    print(f"APR: {interest:.2f}%")
    print(f"Months: {months}")
    print("-"*42)
    #performing calculations and storing as variables
    earned_interest = balance * (interest / 100 * months / 12)
    updated_balance = balance+earned_interest
    #using the Account class functions to update the balance and interest earned.
    my_cd.set_interest(earned_interest)
    my_cd.set_balance(updated_balance)
    #printing the information for the user
    print(f"Earned interest on ${balance:,.2f} after {months} months: ${my_cd.interest:,.2f}")
    print(f"Your new balance is ${my_cd.balance:,.2f}")
    print("-"*42)
    #returning account instance for input function
    return my_cd