# alias takma isim demek as m dersek mat yerine m kullanabiliriz.
#import mat as m
#print(mat.topla(10+20))
#print(m.topla(10,20))

#mat modülünün hepsini değil de içinden fonksiyonları kullanmak istiyorsak from kullarak yapabiliriz. topla,bolme olarak kullanabiliriz

from mat import topla as toplamaIslemi
from human import Human
import random

print(toplamaIslemi(10,20))

print(random.randint(0,100))

human1 = Human("Mirza")
human1.talk("Merhaba")
