import random


class Client:
    def __init__(self, name, last_name, balance, children=0, gender='uncertain'):
        self.name = name
        self.last_name = last_name
        self.full_name = name + " " + last_name
        self.email = f"{name.lower()}.{last_name}@company.com"
        self.balance = balance
        self.children = children
        self.gender = gender
        self.account_number = (
            'ABN' + f'{random.randint(1000000000,9999999999)}')

    def add_deposit(self, amount):
        self.balance += amount
        print(f"Your balance increased by {amount}")
        print(f"Total balance for {self.full_name} is {self.balance}")

    def withdraw_money(self, amount):
        self.balance -= amount
        print(f"Your balance decreased by {amount}")
        print(f"Total balance for {self.full_name} is {self.balance}")

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

    def children_money(self):
        if self.children > 0:
            amount = self.children * 250
            print("Congratulations!\nYour bank has made a decision.\nEvery customer who has a child will receive 250 euro per child.")
            self.add_deposit(amount)


cl_1 = Client("Yavuz", "Gulderen", 2500, 0, "M")
cl_2 = Client("Selcen", "Guldur", 5000, 1, "F")
cl_3 = Client("Aysun", "Caliskan", 10000, 2, "F")

print(cl_2.full_name)

obje_list = [obj for obj in globals().values() if isinstance(obj, Client)]

for Client in obje_list:
    Client.children_money()
