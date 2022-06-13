class Account():

    def __init__( accountholder, atm_card_number, pin_number, account_balance ):
        accountholder.atm_card_number = atm_card_number,
        accountholder.pin_number = pin_number,
        accountholder.account_balance = int(account_balance)

    def balance_enquiry(accountholder):
        return print("Your account balance is", accountholder.account_balance)

    def cash_withdrawal(accountholder):
        money_withdrawn = int(input("Enter amount of money to be withdrawn from account balance "))

        if( money_withdrawn > accountholder.account_balance ):
            return print("You are trying to withdraw more money than you have deposited.")
        else:
            accountholder.account_balance = accountholder.account_balance - money_withdrawn
            return print("Money withdrawn. \nBalance remaining :", accountholder.account_balance)


morrissey = Account(1984, 1083728, 10000)