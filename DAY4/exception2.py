class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance"""

    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """
        try:
            # TODO: Implement withdrawal logic
            pass  
        except ValueError as ve:
            print(ve)
             # TODO: Handle negative withdrawal amounts
        except InsufficientFundsError as isf:
            print(isf)
             # TODO: Handle insufficient funds
        except Exception as e:
            print(e)
            pass  # TODO: Handle unexpected errors

# Example Usage:
account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  
