import json
def dots():
    print("...."*15)

def register_user():
    username = input("whats your new username ")

    with open("user_data.json","r+") as f:
        user_data = json.load(f)
        if username in user_data:
            print("username already exsits")
            return
        
        password = input("whats your new password ")
        user_data[username] = password
        f.seek(0)
        json.dump(user_data,f,indent=4)

def login():
    username = input("whats your username ")
    attempts = 5
    with open("user_data.json","r") as f:
        user_data = json.load(f)
        if username in user_data:
            while True:
                password = input("Whats your password ")
                if password == user_data[username]:
                    print("succsesfully loged in")
                    return
                elif attempts == 0:
                    print("login failed")
                    return
                else:
                    attempts -= 1
                    print(f"wrong password {attempts} attempts left")
                    dots()
    print("User name not found please register first")

def main():
    action = input("type r to register a new account, l to login or q to quit ").lower()
    if action == "r":
        register_user()
    elif action == "l":
        login()
    elif action == "q":
        return True
    else:
        print("that wasnt one of the options")
    dots()
    return False

stop = False
while not stop:
    stop = main()

