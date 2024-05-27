#importing functions
from Savings_Account import create_savings_account
from CD_Account import create_cd_account

#Defining a function that takes the user inputs for savings account calculation
def main():
    """Takes user inputs for savings and CD calculation and returns the created accounts.

    Prompts the user to enter the initial balance, interest rate, and number of months each
    for the Savings Account and CD.
    Calls the create_savings_account or create_cd_account function with the user inputs 
    to calculate savings account details.

    Returns:
        my_account: An instance of the Account class representing the created savings account.
        my_cd: An instance of the Account class representing the created CD account.
    """
    #setting variables with user inputs for the savings account
    balance=float(input("Enter initial Savings Account balance:"))
    interest=float(input("Enter the Savings Account interest rate:"))
    months=int(input("Enter the Savings Account number of months:"))
    #calling the savings account function to pass the user inputs into the account for calculation
    my_account=create_savings_account(balance,interest,months)
    
    #setting variables with user inputs for the CD
    balance=float(input("Enter initial CD Account balance:"))
    interest=float(input("Enter the CD Account interest rate:"))
    months=int(input("Enter the CD Account number of months:"))
    my_cd=create_cd_account(balance,interest,months)

    #Calculating totals
    print("TOTAL")
    print("-"*50)
    total_balance=my_account.balance+my_cd.balance
    total_interest=my_account.interest+my_cd.interest
    print(f"At the end of the CD and Savings Account durations,\n"
          f"you will have earned ${total_interest:,.2f} in interest,\n" 
          f"for a total of ${total_balance:,.2f}.")
    
#running this function takes user inputs and returns all print functions     
main()
