class Account:
    def __init__(self, account_number, account_owner, balance):
        self.account_number = account_number
        self.account_owner = account_owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("İşlem başarıyla tamamlandı. Yeni bakiye:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Hesabınızda yeterli bakiye bulunmamaktadır.")
        else:
            self.balance -= amount
            print("İşlem başarıyla tamamlandı. Yeni bakiye:", self.balance)

    def get_balance(self):
        print("Toplam bakiye:", self.balance)


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print("Hesap başarıyla oluşturuldu!")

    def remove_account(self, account_number):
        del self.accounts[account_number]
        print("Hesap başarıyla kaldırıldı!")

    def get_total_balance(self):
        total_balance = 0
        for account_number in self.accounts:
            total_balance += self.accounts[account_number].balance
        print("Toplam bakiye:", total_balance)


def main():
    bank = Bank()
    while True:
        print("""Bankacılık sistemine hoş geldiniz! Lütfen bir seçenek seçin:
        1. Hesap oluştur
        2. Para yatırma
        3. Para çekme
        4. Hesap kaldırma
        5. Toplam bakiye sorgulama
        6. Çıkış""")
        choice = input("Seçenek: ")
        if choice == "1":
            account_number = input("Hesap numarasını girin: ")
            account_owner = input("Hesap sahibi adını girin: ")
            balance = float(input("Başlangıç bakiyesini girin: "))
            account = Account(account_number, account_owner, balance)
            bank.add_account(account)
        elif choice == "2":
            account_number = input("Hesap numarasını girin: ")
            amount = float(input("Yatırılacak miktarı girin: "))
            bank.accounts[account_number].deposit(amount)
        elif choice == "3":
            account_number = input("Hesap numarasını girin: ")
            amount = float(input("Çekilecek miktarı girin: "))
            bank.accounts[account_number].withdraw(amount)
        elif choice == "4":
            account_number = input("Hesap numarasını girin: ")
            bank.remove_account(account_number)
        elif choice == "5":
            account_number = input("Hesap numarasını girin: ")
            bank.accounts[account_number].get_balance()
        elif choice == "6":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()            
