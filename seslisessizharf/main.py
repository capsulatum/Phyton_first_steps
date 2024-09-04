"""
Kullanıcıdan alınan stringin içindeki
sesli ve sessiz harfleri ayırarak
ekranda gösteren Python kodunu yazınız
"""

str= input("kelime giriniz:")

sesli=["a","e","i","o","u","ü","ö","ı"]
seslilist=[]
sessizlist=[]

for i in range(len(str)):
    if str[i].isalpha():
        if str[i] in sesli:
            seslilist+=str[i]
        else:
            sessizlist+=str[i]

print("sessizler:",sessizlist)
print("sesliler:",seslilist)