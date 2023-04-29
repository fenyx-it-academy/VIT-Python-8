# VIT-Python-8

Odev: 

########################################################################################

1- Banka olarak kayit olan musterilere cocuk basina 250 euro bonus verilme karari alindi.
Buna gore 3 musteri(object) olusturup 2 sinin cocugu oldugunu dusunerek objeleri tanimlayin.



########################################################################################

2- 
Bu ödevde, bankacılık sistemi modellemek için nesne yönelimli programlamayı kullanan bir Python programı oluşturacaksınız. Takim olarak analiz kismi beraber yapilabilir. 
Program, bir kullanıcının birden çok banka hesabını oluşturmasına ve yönetmesine izin vermelidir. Her hesabın bir bakiyesi olmalı ve para yatırma ve çekme işlemlerine izin vermelidir.

Programınız şu sınıfları içermelidir:

Hesap Sınıfı (account class)
Özellikler(Attributes): hesap numarası, hesap sahibi adı, bakiye
Metodlar: para yatırma, para çekme, bakiye sorgulama

Banka Sınıfı (bank class)
Özellikler(Attributes): hesap listesi
Metodlar: hesap ekleme, hesap kaldırma, toplam bakiye sorgulama

Programınız, bir kullanıcının birden çok hesap oluşturmasına ve yönetmesine izin veren bir menü tabanlı bir arayüze sahip olmalıdır. 
İşte menü arayüzünün nasıl çalışabileceğine dair bir örnek:

"""""""
Bankacılık sistemine hoş geldiniz!
Lütfen bir seçenek seçin:

1. Hesap oluştur
2. Para yatırma
3. Para çekme
4. Hesap kaldırma
5. Toplam bakiye sorgulama
6. Çıkış

Seçenek:
Bankacılık sistemine hoş geldiniz!
Lütfen bir seçenek seçin:

1. Hesap oluştur

    Hesap numarasını girin: 12345
    Başlangıç bakiyesini girin: 1000
    Hesap başarıyla oluşturuldu!

2. Para yatırma

    Hesap numarasını girin: 12345
    Yatırılacak miktarı girin: 500
    İşlem başarıyla tamamlandı. Yeni bakiye: 1500

3. Para çekme

    Hesap numarasını girin: 12345
    Çekilecek miktarı girin: 200
    İşlem başarıyla tamamlandı. Yeni bakiye: 1300

4. Hesap kaldırma

    Hesap numarasını girin: 12345
    Hesap başarıyla kaldırıldı.

5. Toplam bakiye sorgulama

    Hesap numarasını girin: 12345
    Toplam bakiye: 1300

6. Çıkış

    Programdan çıkılıyor...

"""""""
