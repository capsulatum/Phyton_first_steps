#Kullanıcının girdiği parola içinde bulunan
#Türkçe karakterleri tespit
#ederek ekranda gösteren Python kodunu yazınız

password=input("enter password")

turkcekarakterler=\
    ["ğ","ü","ı","ş","ö","ç","İ","Ğ","Ü","Ş","Ö","Ç"]

for char in password:
    if char in turkcekarakterler:
        print(char)