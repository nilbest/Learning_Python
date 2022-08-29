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
        ausgabe.append("*"*anz+self.category_name+"*"*anz)
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
            return True
        return False
        
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
            self.withdraw(amount,f"Transfer to {category.category_name}")
            category.deposit(amount,f"Transfer from {self.category_name}")
            transfer = True
        return transfer
    
    def check_funds(self,amount):
        return False if amount > self.get_balance() else True
    
    def __del__(self):
        print("\n"+"#"*40+"\nCategory "+self.category_name+" has been deleted.\n"+"#"*40+"\n")
        





def create_spend_chart(categories):
#    Percentage spent by category
#100|          
# 90|          
# 80|          
# 70|          
# 60| o        
# 50| o        
# 40| o        
# 30| o        
# 20| o  o     
# 10| o  o  o  
#  0| o  o  o  
#    ----------
#     F  C  A  
#     o  l  u  
#     o  o  t  
#     d  t  o  
#        h     
#        i     
#        n     
#        g 
    all_lines = []
    
    all_lines.append(f"Percentage spent by category")
    sum_all_withdraws=0
    sum_category=0
    
    for category in categories:
        for index in category.ledger:
            if index["amount"] < 0:
                sum_all_withdraws=sum_all_withdraws+(-index["amount"])
    
    #print("Summe aller Ausgaben:"+str(sum_all_withdraws))
    
    spendings = []
    
    for category in categories:
        for index in category.ledger:
            if index["amount"] < 0:
                #print(sum_category+index["amount"])
                sum_category = (sum_category+(-index["amount"]))
        #print("Summe: " +str(sum_category))
        #spendings = {f"{str(category)}":str(category),"Percentage":round((sum_category/(100/len(categories))),-1)}
        #print(sum_category/sum_all_withdraws)
        spendings.append((sum_category/sum_all_withdraws))
        sum_category=0
        
    line=[]
    
    for x in range(100,-10,-10):
        for index in range(0,len(categories)):
            #print(index)
            #print(round(spendings[index]*100))
            #print(x)
            line.append("o"+" "*2)if round(spendings[index]*100)>=x else line.append(" "+" "*2)
            #print(line)         
        all_lines.append(" "*(3-len(str(x)))+f"{x}| "+"".join(line))
        line=[]
    
    all_lines.append(" "*4+"-"+"-"*3*len(categories))
    
    max_word=0
    for category in categories:
        #print("Category: "+str(category.category_name))
        if len(category.category_name)>max_word:
            max_word = len(category.category_name)
    
    #print("MaxWord: "+str(max_word))
    
    word_list=[]
    anz=0
    for category in categories:
        for index in range(0,max_word):
            if anz == 0:
                if index < len(category.category_name):
                    word_list.append(""+category.category_name[index]+" "*2)
                else:
                    word_list.append("".join(" "*3))
                #print("Index: "+str(index))
                #print("Laenge Wort: "+str(len(category.category_name)))
            else:
                if index < len(category.category_name):
                    word_list[index]="".join([word_list[index],category.category_name[index]+" "*2])
                else:
                    word_list[index]="".join([word_list[index]," "*3])
                #print(word_list)
        anz = anz+1

    #[' F  C  A  ', ' o  l  u  ', ' o  o  t  ', ' d  t  o  ', '   h     ', '   i     ', '   n     ', '   g     '] 

    #print(word_list)    
    for index in range(0,max_word):
        all_lines.append(" "*5+word_list[index]) 
            
    create_spend_chart = "\n".join(all_lines)
    return create_spend_chart