"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account


def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE # similar to the savings_account requirement when instancing the Account class
    cd_account = Account(balance, 0)
    # Calculate interest earned
    # ADD YOUR CODE HERE # using same code from savings_account
    interest = balance * (interest_rate / 100) * (months / 12)
    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE # Same code as savings_account
    updated_balance = balance + interest
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.  #?? should this be CD_account variable rather than class?
    # ADD YOUR CODE HERE
    cd_account.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class. #?? should this be CD_account variable rather than class?
    # ADD YOUR CODE HERE
    cd_account.set_interest(interest)
    # Return the updated balance and interest earned.
    return updated_balance, interest  # ADD YOUR CODE HERE
