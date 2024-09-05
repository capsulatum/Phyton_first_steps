"""
Kullanıcı tarafından girilen şifrenin aşağıdaki
formata uygun olup olmadığını kontrol eden Python
kodunu yazınız.
– Şifre en az 8 , en fazla 12 karakteriçermelidir.
– Sayı ile başlayıp sayı ile bitemez.
– En az 1 büyük harf ve en az 1 küçük harf karakteri içermelidir.
– Boşluk karakteri içeremez.
– Şifre en az 1 tane alfanümerik olmayan karakter içermelidir.
– Şifre içinde tekrarlayan karakter bulunmamalıdır.
– Kendi belirleyeceğiniz 2 adet özel kriter de kontrol edilmelidir
"""

password= input("lütfen şifreyi giriniz:")



if not 8<=len(password)<=12:
    print("şifre en az 8 en fazla 12 harf uzunlukta olmalı")



if password[0].isdecimal() and password[::-1].isdecimal():
    print("password couldn't be started or ended with a number")



bharfler=\
    ["Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S"
        ,"D","F","G","H","J","K","L","Ş","İ","Z","X","C","V"
        ,"B","N","M","Ö","Ç"]

kharfler=\
    ["q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s"
        ,"d","f","g","h","j","k","l","ş","i","z","x","c","v"
        ,"b","n","m","ö","ç"]
kkontrol=0
bkontrol=0
for i in range(len(password)):
    if password[i] in kharfler:
        kkontrol += 1
    if password[i] in bharfler:
        bkontrol += 1
if not kkontrol>0:
    print("bir büyük ve bir küçük harf olmak zorunda en az")
if not bkontrol>0:
    print("bir büyük ve bir küçük harf olmak zorunda en az")


i=0
kontrol=0
for i in range(len(password)):
    if password[i].isspace():
        kontrol=1
if kontrol==1:
    print("boşluk karakteri olamaz")

uyari=0
for i in range(len(password)):
    if password[i].isalnum()==True:
        uyari=1
        if password[i].isalnum()==False:
            uyari=0
if uyari==0:
    print("en az bir alfanümerik olmayan lazım")



dikkat=0
for i in range(len(password)):
    for j in range(1,len(password)):
        if password[i]==password[j]:
            dikkat+=1
if dikkat>0:
    print("şifrenizde tekrarlayan harf olmamalı")


