# İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturun. 
# Örnek: [ 1, 1, 2, 3, 5, 8, 13, 21, 34..... ]
# Fibonacci Serisi : Serideki her bir sayı kendisinden önceki iki sayının toplamına eşittir.

fibonacciList =[1,1]
for i in range(20):
    if (len(fibonacciList)<20):
        added = fibonacciList[-1] + fibonacciList[-2]
        fibonacciList.append(added)
    else:
        break
print(fibonacciList)
