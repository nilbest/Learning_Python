from pydoc import describe
from unicodedata import category
import math
import re

class Category:
    
    #self.category_name=""
    #self.ledger = []
    
    def __init__(self,name):
        self.category_name = name
        self.ledger = []
        print("\n"+"#"*40+"\nCategory "+self.category_name+" has been created.\n"+"#"*40+"\n")
    
    def __str__(self):
        ausgabe = []
        anz=int((30-len(self.category_name))/2)
        ausgabe.append("\n"+"*"*anz+self.category_name+"*"*anz)
        for index in self.ledger:
            description = str(index["description"][0:23])
            amount = str(index["amount"])+".00" if type(index["amount"]) == int else str(index["amount"])
            ausgabe.append(description+" "*(23-len(description))+" "*(7-len(amount))+amount)
        ausgabe.append(f"Total: {self.get_balance()}")
        #*************Food*************
        #initial deposit        1000.00
        #groceries               -10.15
        #restaurant and more foo -15.89
        #Transfer to Clothing    -50.00
        #Total: 923.96
        ausgabe="\n".join(ausgabe)
        return ausgabe
    
    
    def deposit(self, amount, description=None):
        if description is None:
            description = str() 
        add_ledger = {"amount": round(amount,2),"description": description}
        self.ledger.append(add_ledger)
    
    def withdraw(self, amount, description=None):
        if self.check_funds(amount) == True:
            if description is None:
                description = str() 
            add_ledger = {"amount": -round(amount,2),"description": description}
            self.ledger.append(add_ledger)
        
    def get_balance(self):
        balance = 0
        #balance = [(balance+float(x["amount"])) for x in self.ledger]
        for index in self.ledger:
            balance= balance + index["amount"]  
        #a= (a + index["amount"]for index in self.ledger)
        #print("Balance: ",balance[0])
        return balance
            
    def transfer(self,amount,category):
        transfer = False
        if self.check_funds(amount) == True:
            self.withdraw(amount,f"Transfer to [{category.category_name}]")
            category.deposit(amount,f"Transfer from [{self.category_name}]")
            transfer = True
        return transfer
    
    def check_funds(self,amount):
        return False if amount > self.get_balance() else True
    
    def __del__(self):
        print("\n"+"#"*40+"\nCategory "+self.category_name+" has been deleted.\n"+"#"*40+"\n")
        





def create_spend_chart(categories):
    create_spend_chart = f"Percentage spent by category"
    return create_spend_chart