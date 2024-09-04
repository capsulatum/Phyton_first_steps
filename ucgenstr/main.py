"""
Kullanıcıdan alınan stringi sırayla
her seferinde tek karakter ekleyerek
ekranda gösteren Python kodunu yazınız"""


str=input("lütfen kelime giriniz:")
uzunluk=int(len(str))

for i in range(1,uzunluk+1):
    print(str[0:i:])