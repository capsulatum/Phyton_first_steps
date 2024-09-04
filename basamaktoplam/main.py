"""Kullanıcı tarafından girilen
sayının basamakları toplamını bulan Python
 kodunu yazınız"""

number = abs(int (input("enter a number")))
basamaksayisi=0
basamaktoplam=0

if number<10:
    print("basamak toplamı:",number)

else:
    while number > 0:
        deger = number % 10
        number //= 10
        basamaksayisi += 1

        basamaktoplam = basamaktoplam + deger

    print("basamak toplamı:",basamaktoplam)