"""Q1(c): test program. Run:  python test_wallet.py"""
from wallet import Wallet, NAME, BAL

w = Wallet(NAME, BAL)
print("Opening balance:", w.getBalance())

w.deposit(100)
print("1. Deposit 100 ->", w.getBalance())

w.withdraw(200)
print("2. Valid withdrawal of 200 ->", w.getBalance())

try:
    w.withdraw(1000)
except ValueError as e:
    print("3. Refused (bigger than balance):", e)

try:
    w.withdraw(150)  # 200 + 150 = 350 > LIMIT
except ValueError as e:
    print("4. Refused (daily limit):", e)

w.balance = -500  # attempt to set directly
print("5. After w.balance = -500, getBalance() ->", w.getBalance())
print("   Python did not raise an error: it created a NEW, unrelated attribute")
print("   'balance'. The real private field (_Wallet__balance) is unchanged.")

w.newDay()
w.withdraw(150)
print("After newDay(), withdraw 150 works ->", w.getBalance())
