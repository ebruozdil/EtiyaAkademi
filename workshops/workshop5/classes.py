# 11/04/2023
# sınıflar => classlar
# modules
# paket yöneticisi

# class Human:
#     def talk(self):
#         print("Human talking")
#     def walk(self):
#         print("Human walking")
# human1 = Human() #instance from class
# human1.talk()
"""class Human:   ------> human.py classına taşındı.
    # built-in fonk. nesne ürettiğimizde çalışan alan. önce çalışır
    # constructor
    # initialize
    def __init__(self, name):
        self.name = name
        print("Bir human instance'i üretildi.")
    def __str__(self): #print nesne yapıldığında adres yerine ne yazılacağını conf.etmek için kullanıldı
        return f"Str fonk. dönen değer: {self.name}"
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")"""

# instance => örnek

from workshops.workshop5.human import Human


human1 = Human("Enes")
#human1.name = "Enes"
human1.talk("Merhaba")
human1.walk()

human2 = Human("Mevlüt")
#human2.name = "Mevlüt"
human2.talk("Selam")
human2.walk()

Human("Ebru").talk("Merhaba")