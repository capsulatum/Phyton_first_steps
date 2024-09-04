#2,3 ve 5 ‘e aynı anda bölünebilen 300’den
# küçük pozitif sayıları
#bulan Python kodunu yazınız

for i in range(1,300,1):
    if i%2==0:
        if i%3==0:
            if i%5==0:
                print(i)