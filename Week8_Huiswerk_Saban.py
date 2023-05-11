#Soru 1- Banka olarak kayit olan musterilere cocuk basina 250 euro bonus verilme karari alindi. 
#Buna gore 3 musteri(object) olusturup 2 sinin cocugu oldugunu dusunerek objeleri tanimlayin.

import random


class Client :

    bank_name = 'ABN AMRO'
    total_balance = 0

    def __init__(self,name,surname,balance,child_number):
        self.name = name
        self.surname = surname
        self.balance = balance
        self.email = f'{name}.{surname.lower()}@gmail.com'
        self.account_number = (f'ABN{random.randint(1000000000,9999999999)}')
        self.child_number = child_number

    def add_child_bonnus(self)    :
        if self.child_number <= 0 :
            print(f"{Client.bank_name}'ya hoş geldiniz\nSayin {self.name} {self.surname}.\nHesabınız başarıyla oluşturuldu.")
            print ("Extra cocuk yardimi alamiyorsunuz")
            print(f"Bakiye : {self.balance}")
        
        else:    
            self.balance += self.child_number * 250
            bonus = self.child_number * 250
            print(f"{Client.bank_name}'ya hoş geldiniz\nSayin {self.name} {self.surname}.\nHesabınız başarıyla oluşturuldu.")
            print(f"Çocuklarınıza toplamda {bonus} euro hediye verilecek.")
            print(f"Son bakiye : {self.balance}")

   

c1 = Client('Omer','Uygur',5000,2,)
c2 = Client('cafer','Erdem',200,3,)
c3 = Client('Kamil','Insan',200,0,)

print(c1.add_child_bonnus())
print(c2.add_child_bonnus())
print(c3.add_child_bonnus())
