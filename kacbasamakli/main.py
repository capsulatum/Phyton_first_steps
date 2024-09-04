#Kullanıcı tarafından girilen
#sayının kaç basamaklı olduğu bulan
#Python kodunu yazınız.

"""
number = abs(int(input("enter number")))

number=str(number)
basamaksayisi=0

for i in number:
    basamaksayisi+=1

print("basamak sayısı: ",basamaksayisi)
"""

import itertools

number = abs(int(input("enter number")))
for i in itertools.count():
    power= 10**i
    if power> number:
        print("basamak sayisi", i)
        break