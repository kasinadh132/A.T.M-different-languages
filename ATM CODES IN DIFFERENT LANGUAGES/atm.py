import random

class Account:
    #construct an account object
    def __init__(self, id , balance =0, annualInterstRate = 3.4):
        self.id = id
        self.balance = balance
        self.annualInterstrate = annualInterstRate
        
def getID(self):
    return self.id

def getbalance(self):
    return self.balance

def getAnnualIntrestRate(self):
    return self.annualInterstRate

def getmonthlyIntrestRate(self):
    return self.annualInterstRate /12

def withdraw(self,amount):
    self.balance -=amount
    
def  deposit(self,amount):
    self.balance +=amount
    
def  getMonthlyIntrestRate(self):
    return self.balance * self.getMonthlyIntrestRate()

def main():
 #creating accounts
 accounts =[]
 for i in range(1000,9999):
    account = Account(i,0)
    accounts.append(account)
    
#ATM Proccesses
while  True:
    
    #Reading id from user
    id = int(input("\n Enter account pin:"))
    
    #Loop till id is valid
    while id < 1000 or id > 9999:
     id =  int(input("\n Enter account pin"))

#Iterating over account session
while  True:
    
    #printing menu
    print("\n1 - veiw  balance \t 2 - withdraw \ t 3 - Deposit \t 4 Exit")
    
    #Reading selction
    selction = int(input("\n Enter Your selction"))
    
    #Getting account object
    for acc in  accounts:
        #comparing account id:
        if  acc.getId() == id:
            accountobj = Acc
            break
        #veiw Balnce
        if selction ==1:
            #printing balance
            print(accountobj . getBalance())
            
    # Withdraw
           elif  selection == 2:
               # Reading amount
               amt = float(input("\nEnter amount to withdraw: "))
               ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
 
               if ver_withdraw == "Yes":
                   print("Verify withdraw")
               else:
                   break
 
               if amt < accountObj.getBalance():
                  # Calling withdraw method
                  accountObj.withdraw(amt)
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
               else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " n")
                    print("\nPlease make a deposit.");
    # Deposit
            elif lection == 3:
               # Reading amount
               amt = float(input("\nEnter amount to deposit: "))
               ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
 
               if ver_deposit == "Yes":
                  # Calling deposit method
                  accountObj.deposit(amt);
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
               else:
                   break
        elif selection == 4:
               print("n Transaction is now complete.")
               print("Transaction number: ", random. randit(10000,1000000))
               print("Current Intrest Rate: ", accountobj.annualInterstRate)
               print("Monthly Interst Rate: ", accountobj.annualInterstRate / 12)
               print("Thanks for choosing us your bank")
               exit()
               
        #Any other choice
        else:
            print("nThat's an invalid choice. ")
            
#Main function
main()