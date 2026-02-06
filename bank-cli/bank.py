
available_balance = 0.0

def balance():
    print("-------------------------------------------------")
    print(f"Your current account balance : ${available_balance:.2f} ")
    print("--------------------------------------------------")

def deposit(amt):
    global available_balance
    print("--------------------------------------------------")
    available_balance += amt
    print(f"As per your Request you deposied your amount ${amt:.2f} into your Bank account")
    print(f"Your current balance after deposite : ${available_balance} ")

def withdraw(amt):
    global available_balance
    print("--------------------------------------------------")
    if(available_balance <= 0 or available_balance < amt):
         print("Low Balance, Withdraw failed ")
    else:
        available_balance -= amt
        print(f"As per your Request you withdrawl your amount ${amt:.2f} from your account")
        print(f"Your current balance after withdrawl : ${available_balance   }")
def main():
    print("                     WELCOME TO BANK 🏦                   ")
    is_running = True
    while is_running:
        print("----------------Available Options------------------")
        print("")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("---------------------------------------------------")
        opt = input("Enter the service number You wanted : ")
        if opt.isdigit():
            opt = int(opt)
            match opt:
                case 1:
                    balance()
                case 2:
                    amt = float(input("Enter the amount to be deposited : $"))
                    deposit(amt)
                case 3:
                    amt = float(input("Enter the amount To withdraw : $"))
                    withdraw(amt)
                case 4:
                    is_running=False
                case _:
                    print("Enter the VALID input ")
        else:
            print("Enter a valid input")
    print("Thank You!!!")
if __name__== "__main__":
    main()
