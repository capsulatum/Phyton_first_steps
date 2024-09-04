"""
Sayı Bulma Oyunu– 1-100 arasında rasgele bir pozitif tam sayı belirleyin.
 • importrandom →random.randint(1,100)
 – Kullanıcıya 5 seçim hakkı vererek onu aşağı-yukarı şeklinde yönlendirin.
 – Kullanıcı sayıyı doğru tahmin ederse «Tebrikler» mesajı, tüm haklarını kullanıp
bilemediyse «Üzgünüz, kaybettiniz. Sayı : XX ‘di» mesajını ekrana yazdırın"""

import random

random_number = random.randint(1,100)
hak=0

while hak<5:
    secim = int(input("lutfen seciminizi giriniz"))
    if secim<random_number:
        print("daha buyuk bir sayı seçmeyi deneyin")
    elif secim>random_number:
        print("daha küçük bir sayı seçmeyi deneyin")
    else:
        print("tebrikler doğru bildiniz sayı şu idi:",random_number)
    hak+=1

if hak ==5 :
    print("Üzgünüz, kaybettiniz. Sayı : {} ‘di".format(random_number))