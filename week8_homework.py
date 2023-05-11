import random
class Account:
    def __init__(self, name, balance):

        self.name = name
        self.balance = balance
        self.account_number = f"ABN{random.randint(100000000,999999999)}"

    def add_deposit(self,cash):
        self.balance += cash

    def withdraw_money(self,cash):
        if cash > self.balance:
            print("Bakiye yetersiz")
        else:
            self.balance -= cash

class Bank:
    
    def __init__(self):

        self.accounts = []    

    def show_accounts(self):
        for i in self.accounts:
            print(i.__dict__)  
        
    def add_account(self):
    
            user = input("Kullanıcı adınızı giriniz : " )
            name = input("Hesap isminiz nedir :")
            balance = int(input("Bakiye miktarınız  :" ))
            user = Account(name, balance)
            self.accounts.append(user)

    def total_balance(self):
        total_balance = 0
        for i in self.accounts:
            total_balance += i.balance
        print(total_balance)

    def __str__(self) -> str:
        print (f"adı {self.name}")

print(""" Bankacılık sistemine hoş geldiniz! Lütfen bir seçenek seçin:

1-Hesap oluştur
2-Hesapları görüntüle
3-Para yatırma
4-Para çekme
5-Hesap kaldırma
6-Toplam bakiye sorgulama
7-Çıkış

""")
abn = Bank()


while True:
    chose = int(input("Yapmak istediğiniz işlemi seçiniz :  "))
    if chose == 1 :
        abn.add_account()
        print("Hesap başarıyla eklendi..\n")
        continue

    elif chose == 2:
        if abn.accounts == []:
            print("Hesap bulunamadı..")
        else:
            abn.show_accounts()


    elif chose == 3 :
        
        for i in abn.accounts:
            abn.show_accounts()
            enter = input("Para yatırmak istediğiniz hesabın hesap numarasını giriniz :")
            if enter == i.account_number:
                print(f"Bakiyeniz {i.balance} euro.")
                money = int(input("Yatırmak istediğiniz miktarı giriniz :"))
                i.add_deposit(money)
                print(f" Yeni bakiyeniz {i.balance} euro.")
                continue
            else:
                print("Hesap bulunamadı..")
                continue

    elif chose == 4 :
        abn.show_accounts()
        enter = input("Para çekmek istediğiniz hesabın hesap numarasını giriniz :")
        for i in abn.accounts:
            if enter == i.account_number:
                print(f"Bakiyeniz {i.balance} euro.")
                money = int(input("Çekmek istediğiniz miktarı giriniz :"))
                i.withdraw_money(money)
                print(f"Bakiyeniz {i.balance} euro.")
                continue
            else:
                print("Hesap bulunamadı..")
                continue
        
    elif chose == 5:

        abn.show_accounts()                    
        enter = input("Silmek istediğiniz hesabın hesap numarasını giriniz :")
        
        for i in abn.accounts:
            if enter == i.account_number:
                del abn.accounts[abn.accounts.index(i)]
                print(f"{i.account_number} numaralı hesabınız silinmiştir...")
                continue


    elif chose == 6:
        abn.total_balance()
        continue

    elif chose == 7:
        print("Çıkış yapılıyor...")
        break

    else:
        print("Yanlış veri girişi yaptınız..")
        continue
