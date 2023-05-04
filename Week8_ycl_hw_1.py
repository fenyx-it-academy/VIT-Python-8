import random

class Client:
    def __init__(self, name,last_name, balance, children= 0, gender='uncertain'):
        self.name = name
        self.last_name = last_name
        self.email = f"{name.lower()}.{last_name}@company.com"
        self.balance= balance
        self.children = children
        self.gender = gender
        self.account_number = ('ABN' + f'{random.randint(1000000000,9999999999)}')

    def add_deposit(self, amount):
        self.balance+= amount
        print(f"Your balance increased by {amount}")
        print(f"Total balance for {self.name} is {self.balance}")
    def withdraw_money(self,amount):
        self.balance -= amount
        print(f"Your balance decreased by {amount}")
        print(f"Total balance for {self.name} is {self.balance}")

    def send_money(self, receiver_account_number, amount):
            if self.balance < amount:
                return 'balance is not enough'
            else:
                client_object = [obj for obj in globals().values() if isinstance(
                    obj, Client) and obj.account_number == receiver_account_number]
                if len(client_object) == 0:
                    print('client not found')
                else:
                    reciever_object = client_object[0]
                    reciever_object.balance += amount
                    self.balance -= amount
                
    def add_bonus_child(self):
    
        amount = self.children*250
        self.balance += amount
        print(f"Your balance increased by {amount}")
        print(f"Total balance for {self.name} is {self.balance}")
        
c1 = Client('Joop', 'Hoopman', 3000, 2, 'M')    
c2 = Client('Cees', 'Buys', 7000, 1, 'M')    
c3 = Client('Lobke', 'De Vries', 2000, 0, 'F')

c1.add_bonus_child()
c2.add_bonus_child()
c3.add_bonus_child()

        
        
          