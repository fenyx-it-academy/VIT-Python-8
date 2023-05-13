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
"""
2- Bu ödevde, bankacılık sistemi modellemek için nesne yönelimli programlamayı kullanan bir Python programı oluşturacaksınız. 
Takim olarak analiz kismi beraber yapilabilir. Program, bir kullanıcının birden çok banka hesabını oluşturmasına ve yönetmesine izin vermelidir. 
Her hesabın bir bakiyesi olmalı ve para yatırma ve çekme işlemlerine izin vermelidir.

Programınız şu sınıfları içermelidir:

Hesap Sınıfı (account class) Özellikler(Attributes): hesap numarası, hesap sahibi adı, bakiye Metodlar: para yatırma, para çekme, bakiye sorgulama

Banka Sınıfı (bank class) Özellikler(Attributes): hesap listesi Metodlar: hesap ekleme, hesap kaldırma, toplam bakiye sorgulama

Programınız, bir kullanıcının birden çok hesap oluşturmasına ve yönetmesine izin veren bir menü tabanlı bir arayüze sahip olmalıdır. İşte menü arayüzünün nasıl çalışabileceğine dair bir örnek:

""""""" Bankacılık sistemine hoş geldiniz! Lütfen bir seçenek seçin:

Hesap oluştur
Para yatırma
Para çekme
Hesap kaldırma
Toplam bakiye sorgulama
Çıkış
Seçenek: Bankacılık sistemine hoş geldiniz! Lütfen bir seçenek seçin:

Hesap oluştur

Hesap numarasını girin: 12345 Başlangıç bakiyesini girin: 1000 Hesap başarıyla oluşturuldu!

Para yatırma

Hesap numarasını girin: 12345 Yatırılacak miktarı girin: 500 İşlem başarıyla tamamlandı. Yeni bakiye: 1500

Para çekme

Hesap numarasını girin: 12345 Çekilecek miktarı girin: 200 İşlem başarıyla tamamlandı. Yeni bakiye: 1300

Hesap kaldırma

Hesap numarasını girin: 12345 Hesap başarıyla kaldırıldı.

Toplam bakiye sorgulama

Hesap numarasını girin: 12345 Toplam bakiye: 1300

Çıkış

Programdan çıkılıyor...
"""
class Account:
    def __init__(self, account_number, account_owner, balance):
        self.account_number = account_number
        self.account_owner = account_owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if not self.balance >= amount:
            print(f"Yetersiz bakiye.\n{account1.get_balance()} Eura'dan daha fazla bir miktar alinamaz!!!")
        else:
            self.balance -= amount
            print(f"{account_owner1} musteri hesabindan {amount1} Euro alindi")
            print(f"İşlem başarıyla tamamlandı. \nYeni bakiye  :  {account1.get_balance()}")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            print("Hesap bulunamadı.")

    def total_balance(self):
        total = 0
        for account in self.accounts.values():
            total += account.get_balance()
        return total

bank = Bank()

while True:
    print("""
    *************************
    Bankacılık sistemine hoş geldiniz!
    Lütfen bir seçenek seçin:
    1. Hesap oluştur
    2. Para yatırma
    3. Para çekme
    4. Hesap kaldırma
    5. Toplam bakiye sorgulama
    6. Çıkış
    ************************
    """)

    choice = input("Seçenek: ")

    if choice == "1":
        account_number1 = input("Hesap numarasını girin  : ")
        account_owner1 = input("Hesap sahibi adını girin  : ")
        balance1 = float(input("Başlangıç bakiyesini girin  : "))
        account1 = Account(account_number1, account_owner1, balance1)
        bank.add_account(account1)
        print(f"{account_number1} numarali {account_owner1} hesabi başarıyla oluşturuldu!")
        print(f"Başlangıç bakiyesi : {balance1}")

    elif choice == "2":
        account_number1 = input("Hesap numarasını girin  : ")
        amount1 = float(input("Yatırılacak miktarı girin  : "))
        if account_number1 in bank.accounts:
            account1 = bank.accounts[account_number1]
            account1.deposit(amount1)
            print(f"{account_number1} nolu hesaba {amount1} Euro yatirildi")
            print(f"İşlem başarıyla tamamlandı. \nYeni bakiye: {account1.get_balance()}")
        else:
            print("Hesap bulunamadı.")

    elif choice == "3":
        account_number1 = input("Hesap numarasını girin  : ")
        print(f"Toplam bakiye: {account1.get_balance()} Euro")
        amount1 = float(input("Çekilecek miktarı girin  : "))
        if account_number1 in bank.accounts:
            account1 = bank.accounts[account_number1]
            account1.withdraw(amount1)   
            #print(f"{account_owner1} musteri hesabindan {amount1} Euro alindi")
            #print(f"İşlem başarıyla tamamlandı. \nYeni bakiye  :  {account1.get_balance()}")
        else:
            print("Hesap bulunamadı.")

    elif choice == "4":
        account_number1 = input("Hesap numarasını girin  : ")
        if balance1 != 0:
            print(f"Lutfen hesaptaki {account1.get_balance()} parayi cekiniz")
        else :    
            bank.remove_account(account_number1)
            print(f"{account_owner1} ,isimli musteri hesabi başarıyla kaldırıldı.")

    elif choice == "5":
        account_number1 = input("Hesap numarasını girin  : ")
        if account_number1 in bank.accounts:
            account1 = bank.accounts[account_number1]
            print(f"Hesap sahibi : {account_owner1}")
            print(f"Toplam bakiye: {account1.get_balance()} Euro")
            
        else:
            print("Hesap bulunamadı")
