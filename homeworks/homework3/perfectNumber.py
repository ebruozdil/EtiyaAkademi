# Bir sayının kendi hariç tüm bölenlerinin toplamı eğer kendisine eşitse bu Mükemmel Sayıdır. 
# Örnek: 1 + 2 + 3 = 6
# Kullanıcıdan aldığı sayıyının mükemmel olup olmadığını söyleyen bir program yazın. 

number=int(input("Sayıyı giriniz : "))
total=0
for i in range(1,number):
    if number % i ==0 :
        total+=i

if total==number :
    print(f"{number}  sayısı mükemmel sayıdır.")   
else:
    print(f"{number}  sayısı mükemmel sayı değildir.")     