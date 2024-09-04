"""
Kullanıcıdan alınan stringin palindrome
olup olmadığını bulan Python kodunu yazınız
"""

str= input("lütfen bir kelime giriniz:")
uzunluk=len(str)//2
ispalindrome=False

for i in range(0,uzunluk):
    if str == str[::-1]:
        ispalindrome=True
    else:
        ispalindrome=False

if ispalindrome==True:
    print("palindromedur")
else:
    print("palindrome değildir")