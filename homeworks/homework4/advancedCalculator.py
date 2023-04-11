"""""
Kullanıcıyı sürekli konsolda tutarak istediği kadar işlem yapmasını sağlayacak bir hesap makinesi programlayacağız. 
Hesaplama işlemlerinin her biri ayrı fonksiyon olmalıdır.
Kullanıcı klavyeden ilk olarak istediği işlemi ( + - / * % ) girmelidir. 
Dört işleme ek mod hesaplama da dahil. Daha sonra gireceği iki sayının kullanıcının istediği işleme 
yönlendirilmesini eğer kullanıcıdan alınan değer yukarıdaki beş sembolden biri değilse programın hata vermesini 
sağlayalım. Kullanıcı işlem seçmek yerine “q” harfi girişi yaparsa programı sonlandıralım aksi takdirde program 
her hesaplama sonrası tekrar işlem yapabilir olmalıdır. 
"""
def toplama(a, b):
    return a + b


def cikarma(a, b):
    return a - b


def carpma(a, b):
    return a * b


def bolme(a, b):
    if (b == 0):
        return "Bölen sıfır olmamalıdır!!"
    return a / b


def mod(a, b):
    if (b == 0):
        return "Bölen sıfır olmamalıdır!!"
    return a % b


while True:
    secim = input(
        "Lütfen bir işlem seçiniz: ( +, -, *, /, % ) ya da çıkmak için 'q' ya basınız. ")
    if secim == "q":
        print("Çıkış yapıldı.")
        break
    if secim not in ["+", "-", "*", "/", "%"]:
        print("Hatalı giriş yaptınız.")
        continue
    print(f"Seçilen işlem : {secim}")
    a = float(input("İlk sayıyı giriniz: "))
    b = float(input("İkinci sayıyı giriniz: "))
    if secim == "+":
        sonuc = toplama(a, b)
    elif secim == "-":
        sonuc = cikarma(a, b)
    elif secim == "*":
        sonuc = carpma(a, b)
    elif secim == "/":
        sonuc = bolme(a, b)
    elif secim == "%":
        sonuc = mod(a, b)
    else:
        print("Hatalı giriş yaptınız.")

    print(f"Sonuc : {sonuc}")