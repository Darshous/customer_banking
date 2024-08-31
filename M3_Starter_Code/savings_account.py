"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE # code ref from 8/27/24 class on import modules
from Account import Account
# Define a function for the Savings Account


def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE # refernce 8/29/24 class instance required the hint, found no reference in class notes
    savings_account = Account(balance, 0)
    # Calculate interest earned
    # ADD YOUR CODE HERE #initial mistake code interest = balance * interest_rate * months or i=prt
    interest = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE # created new function and simple math referencing
    update_balance = balance + interest
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE #only reference to this was the .get but instead.set which was an option in auto fill
    savings_account.set_balance(update_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE #same as above
    savings_account.set_interest(interest)
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE recommended solution based on 8/29.24 when updating the car values red and mileage
    return update_balance, interest
