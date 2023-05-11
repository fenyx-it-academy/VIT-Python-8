import random

class Account:
    def __init__(self, name, balance):

        self.account_number = f"ABN{random.randint(100000000,999999999)}"
        self.name = name
        self.balance = balance

    def add_deposit(self,cash):
        self.balance += cash

    def withdraw_money(self,cash):
        if cash<=self.balance:
            self.balance -= cash


    def __str__(self) -> str:
        return f"\nIsim : {self.name}\nBakiyesi : {self.balance}\nHesap no : {self.account_number}\n"

class Bank():
    
    def __init__(self):
        self.accounts : list[Account] = []
        
        
    def add_account(self):
        user = input("Kullanıcı adınızı giriniz : " )
        name = input("İsim giriniz : " )
        balance = int(input("Bakiyenizi girinizi : " ))
        
        user=Account(name,balance)
        self.accounts.append(user)
        print("Kullanici basariyla olusturuldu..")
        return user
        
    
    def del_account(self):
        print(Abn_Bank)
        user = input("Silinecek kişinin hesap numarasi :")
        for i in self.accounts :
            if i.account_number == user:
                return self.accounts.remove(i)


    
    
    def total_balance(self):
        user = input("Hangi hesap numarasi :")
        for i in self.accounts:
            if i.account_number == user:
                return i.balance


    
    def hesabi_bul(self,account_number):
        for i in self.accounts:
            if i.account_number == account_number :
                return i
            
    def __str__(self):
        result=""
        for i in self.accounts:
            result +=str(i)
        return result



Abn_Bank=Bank()
while True:
    print(""" Bankacılık sistemine hoş geldiniz! Lütfen bir seçenek seçin

1-Hesap oluştur
2-Para yatırma
3-Para çekme
4-Hesap kaldırma
5-Toplam bakiye sorgulama
6-Çıkış

""")
    chose = int(input("Yapmak istediğiniz işlemi seçiniz :  "))
    if chose == 1 :
        print(Abn_Bank.add_account())
        print("Hesap başarıyla olusturuldu..\n")
        
        

    elif chose == 2 :
        money = int(input("Yatırmak istediğiniz miktarı giriniz :"))
        who=input("Yatırmak istediğiniz hesap no : ")
        user=Abn_Bank.hesabi_bul(who)
        user.add_deposit(money)
        print(f" {money} euro hesabınıza yatırıldı..")
        print(f"Yeni bakiye: {user.balance}")

    elif chose == 3 :
        money = int(input("Cekmek istediğiniz miktarı giriniz :"))
        who=input("Cekmek istediğiniz hesap no : ")
        user=Abn_Bank.hesabi_bul(who)
        user.withdraw_money(money)
        print(f" {money} euro hesabınızdan cekildi..")
        print(f"Yeni bakiye: {user.balance}")
        

    elif chose == 4:
        Abn_Bank.del_account()
        print("Hesap başarıyla silindi..\n")
        

    elif chose == 5:
        print(f"Toplam bakiyeniz {Abn_Bank.total_balance()}")
        

    elif chose == 6:
        print("Hesaptan çıkış yapıldı..\n")
        break

    
    else:
        print("yanlış giriş yaptınız")
        


