cevap1
import random

class Client:
    def __init__(self, name,last_name,balance , children =0 ,gender='uncertain'):
        self.name = name
        self.last_name = last_name
        self.email = f"{name.lower()}.{last_name}@company.com"
        self.balance= balance
        self.gender = gender
        self.children= children
        self.account_number = ('ABN' + f'{random.randint(1000000000,9999999999)}')
    
    def kind_balance(self):
        self.balance+=(250*self.children)
        return self.balance
            
    def add_deposit(self, amount):
        self.balance+= amount
        print(f"Your balance increased by {amount}")
        print(f"Total balance for {self.name} is {self.balance}")
    def withdraw_money(self,amount):
        self.balance -= amount
        print(f"Your balance decreased by {amount}")
        print(f"Total balance for {self.name} is {self.balance}")

    def send_money(self, receiver_account_number, amount):
      if self.balance <= amount:
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

c1=Client('Ali','kaya',5000,2,'M')
c2=Client('Ayse','Ok',2000,4,'V')
c3=Client('Ahmet','Son',3000,'M')
print(c1.kind_balance())
cevap2
class Acount:
    def __init__(self,name,acount_number,balance):
        self.acount_number=acount_number
        self.balance=balance
        self.name=name
    def add_money(self, amount):
        self.balance+=amount
        print(f'Islem tamamlandi .Sayin {self.name} Yeni Bakiye:', self.balance)
    def withdraw_money(self, amount):
        if amount>= self.balance:
            print('Bakiye yetersiz')
        else:
            self.balance-=amount
        print(f'Islem tamamlandi Sayin {self.name} Yeni Bakiye', self.balance)
    def show_balance(self):
        print(f'{self.acount_number},hesap nolu {self.name} musterisinin  toplam bakiyesi {self.balance} Euro dir')

class Banka():
    
    def __init__(self):
        
        self.hesaplar={}
        
        
    def hesap_olustur(self,name,acount_number,amount):
        self.hesaplar[acount_number]=Acount(name,acount_number,amount)
        print(f'{name} Adina Hesap olusturuldu')
    def hesap_kaldirma(self,acount_number):
        del self.hesaplar[acount_number]
        print('Hesap kaldirma islemi basariyla gerceklestirildi.')
    def menu(self):
        while True:
            print('Bankacılık Sistemine Hoş Geldiniz! ')
            print('1-Hesap Oluştur\n2-Para Yatırma\n3-Para Cekme\n4-Hesap Kaldırma\n5-Toplam Bakiye Sorgulama\n6-Çıkış\n')
            choise=int(input('Lütfen bir seçenek seçin:'))
            if choise==1:
                
                acount_number=input('Hesap numarasini giriniz:')
                name=input('Adinizi ve Soyadinizi Giriniz:')
                amount=float(input('Baslangic Bakiyesini Giriniz:'))
                self.hesap_olustur(name,acount_number,amount)
                                        
            elif choise==2:
            
                acount_number=input('Hesap numarasini giriniz:')
                amount=float(input('Yatirilacak miktari giriniz:'))
                self.hesaplar[acount_number].add_money(amount)
                    
            elif choise==3:
                acount_number=input('Hesap numarasini giriniz:')
                amount=float(input('Cekeceginiz miktari giriniz:'))
                self.hesaplar[acount_number].withdraw_money(amount)
                
            elif choise==4:
                acount_number=input('Hesap numarasini giriniz:')
                self.hesap_kaldirma(acount_number)
            elif choise==5:
                acount_number=input('Hesap numarasini giriniz:')
                if acount_number not in self.hesaplar:
                    print('Hesap numarasi bulunamadi')
                else:
                    self.hesaplar[acount_number].show_balance()
            elif choise==6:
                break
            else:
                print('Hatali giris yaptiniz Tekrar Deneyiniz')

islem=Banka()
islem.menu()

