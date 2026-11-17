# name: Pratik Varma roll no:33
# Smart ATM Banking System

balance = 5000
correct_pin = 1234

try:
    pin = int(input("Enter your 4-digit ATM PIN: "))
    if pin != correct_pin:
        raise ValueError("Incorrect PIN!")

    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if amount > balance:
        raise ArithmeticError("Insufficient account balance!")

    balance -= amount
    print("\nTransaction Successful!")
    print("Amount withdrawn: Rs.", amount)
    print("Remaining balance: Rs.", balance)

except ValueError as e:
    print("Input Error:", e)

except ArithmeticError as e:
    print("Transaction Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Thank you for using Smart ATM.")
