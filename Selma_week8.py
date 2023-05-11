class Account:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print("Yeni bakiyeniz: ", self.balance)
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Yetersiz bakiye. ")
        else:
            self.balance -= amount
            print("Yeni bakiyeniz: ", self.balance)
        
    def check_balance(self):
        print("Hesap bakiyeniz: ", self.balance)
        

class Bank:
    def __init__(self):
        self.accounts = []
        
    def add_account(self, account):
        self.accounts.append(account)
        print("Hesap oluşturuldu.")
        
    def remove_account(self, account_number):
        self.accounts.remove(account)
        print("Hesap kaldırıldı.")
        
     
    def total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.balance
        print("Toplam bakiyeniz: ", total_balance)
        

bank = Bank()

print("\n***Bankacılık sistemine hoş geldiniz!***")
while True:
    
    print("\nLütfen bir işlem seçin:")
    print("1 - Hesap oluştur")
    print("2 - Para yatirma")
    print("3 - Para cekme")
    print("4 - Hesap kaldirma")
    print("5 - Toplam bakiye sorgulama")
    print("6 - Çıkış yap")


    choice = input("\nSeçiminiz (1-6): ")

    if choice == "1":
        account_number = input("Hesap numarasını girin: ")
        account_holder_name = input("Hesap sahibinin adını girin: ")
        balance = float(input("Başlangıç bakiyesini girin: "))
        account = Account(account_number, account_holder_name, balance)
        bank.add_account(account)

    elif choice == "2":
        account_number = input("Hesap numarasını girin: ")
        amount = float(input("Yatırmak istediğiniz tutarı girin: "))
        print("Islem basariyla olusturuldu.")
        account.deposit(amount)

    elif choice == "3":
        account_number = input("Hesap numarasını girin: ")
        amount = float(input("Çekmek istediğiniz tutarı girin: "))
        if balance<amount:
            print("Hesapta olmayandan fazlasini cekemezsiniz.")
        else:
            account.withdraw(amount)
        
    elif choice == "4":
        account_number = input("Hesap numarasını girin: ")
        bank.remove_account(account_number)

    elif choice == "5":
        bank.total_balance()

    elif choice == "6":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen 1-6 arasında bir seçim yap")
