import BankChoices as bc
stop = False
bc.dots()
print("welcome to the banking simulator made by yakov")

account, account_type = bc.open_account()
while stop != True:
    stop = bc.action(account, account_type)
