alinacaksayi=int(input("kaç adet sayi gireceksiniz"))
i=0
toplam=0

while i<alinacaksayi:
    sayi=int(input("sayi giriniz"))
    toplam = toplam + (sayi**2)
    i+=1

print("kare toplamı:", toplam)