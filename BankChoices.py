import BankInfo as bi
import Bank as b
bank_holders = {}

def dots():
    print("...."*15)

def get_type():
    stop = False
    allowed = ["s", "c","r"]
    while not stop:
        print("...." * 10)
        print("would you like to open a savings, checking or reuglar banking account?")
        acc_type = input("type (s/c/r) then hit enter\n -> ")
        if acc_type in allowed:
            stop = True
        else:
            print("That wasn't one of the options")
    dots()
    return acc_type


def user_name():
    accepted = "abcdefghijklmnopqrstuvwxyz"
    while True:
        stop = False
        name = input("What is your name? ")
        for name in name:
            if name not in accepted:
                stop = True
        if not stop:
            break
        print("That's not an acceptable account name, make sure to use only letters")
    return name


def get_amount(a_type):
    stop = False
    while not stop:
        try:
            amount = int(input(f"choose an ammount for your {a_type}\n -> "))
        except ValueError:
            print("That wasn't a number")
            continue
        return amount

def open_account():
    account_type = get_type()
    name = user_name()
    if account_type == "s":
        amount = get_amount("minimal savings")
        account = b.SavingsAccount(name, amount)
        print("your savings account has been successfully opened")
    elif account_type == "c":
        account = b.CheckingAccount(name)
        print("your checking account has been successfully opened")
    else:
        account = b.BankAccount(name)
        print("Your bank account has been successfully opened")
    print(f"your bank id is {account.id}")
    dots()
    return account, account_type

def action_type(account_type):
    accapted = ["d","w","q"]
    ask = "(d/w/q)"
    do = ""
    if account_type == "c":
        accapted = ["d","w","c","q"]
        do = "issue a checkbook, "
        ask = "(d/w/c/q)"
    while True:
        action = input(f"would you like to deposit, {do}withdraw or quit?\ntype {ask} then hit enter\n -> ")
        if action in accapted:
            break
        else:
            print("that wasnt one of the options")
    return action
    
def action(account,account_type):
    action = action_type(account_type)
    if action == "d":
        amount = get_amount("deposit")
        account.deposit(amount)
    elif action == "w":
        amount = get_amount("withdrawel")
        account.withdraw(amount)
    elif action == "c":
        account.issue_checkbook()
    else:
        action = True
    dots()
    return action
    
def save_info(account):
    pass
    





