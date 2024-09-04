list= []
ort_toplam=0
degiskensayisi = int(input("kaç adet sayı gireceksiniz"))

for i in range(degiskensayisi):
    sayi=int(input("sayi giriniz"))
    list.append(sayi)

for i in range(degiskensayisi):
    ort_toplam+=list[i]

ort_toplam=ort_toplam/degiskensayisi
print(ort_toplam)