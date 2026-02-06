import random as rd
import time as t
symbols = ["⭐","🍉","🍒","🍋","🔔"]

def spin_row():
    result = [rd.choice(symbols) for _ in range(3)]
    return result

def print_row(row):
    print("--------------")
    print(" | ".join( row))
    print("--------------")

def get_payout(row,bet):
        if row[0] == row[1] == row[2]:

            if row[0] == "⭐":
                return bet * 3
            elif row[0] == "🍉":
                return bet  * 4
            elif row[0] == "🍒":
                return bet * 2
            elif row[0] == "🍋":
                return bet  * 5
            elif row[0] == "🔔":
                return bet  * 6
        return 0

def main():
    is_running = True
    balance = 100
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("      Welcome to Python SLot Game         ")
    print("      SYMBOLS: ⭐  🍉  🍒  🍋  🔔        ")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")
    while is_running:
        print(f"Current balance : ${balance}")
        bet = input("Place your bet : $ ")
        if bet.isdigit():
            bet= int(bet)
            if bet > balance:
                print("Insufficient Funds")
                continue
            else:
                balance -= bet
                row  = spin_row()
                print("spinning...// \n")
                t.sleep(1)
                print_row(row)
                payout = get_payout(row,bet)
                if payout > 0:
                    print(f"Congo! 🥂 You won ${payout} ")
                    balance += payout
                    print(f"Current Balance : {balance} ")
                else:
                    print("sorry you lost! The Round")


        else:
            print("Enter An Valid Bet")
        again = input("Wanna Play Again ?(Y/N) :").upper()
        if  again == "N":
            is_running = False
        elif again == "Y":
            continue
        else:
            print("Enter the Valid Input")
            again = input("Press Enter to Continue .....")
            continue
    print("Thank you! Have a nice Day!@")
if __name__=="__main__":
    main()
