mevcut_maas=int(input("mevcut maaş"))
cocuk_sayisi=int(input("çocuk sayısı"))
zam_miktari=int(input("zam miktarı"))

if mevcut_maas<3000:
    yeni_zam=mevcut_maas*20/100

elif mevcut_maas<=4000 and mevcut_maas>=3000:
    yeni_zam = mevcut_maas * 15 / 100
else:
    yeni_zam = mevcut_maas * 10 / 100

yeni_zam=yeni_zam+(cocuk_sayisi*70)

if zam_miktari>yeni_zam:
    yeni_zam=zam_miktari

print("yeni maaş miktarı {}".format(mevcut_maas+yeni_zam))

