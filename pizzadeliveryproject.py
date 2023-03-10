# -*- coding: utf-8 -*-
"""PizzaDeliveryProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ARRJ0Tq8h0EpA5gqqDki2wqZaU7TBhNJ
"""

# Author: Bilal Berkam Dertli and Mehmet Yıldırgan


class Pizza():
  desc = "Bu henüz hazırlanmamış bir pizza."
  price = 0

  def get_description(self):
    return self.desc
  def get_cost(self):
    return self.price
  

class Klasik(Pizza):#Klasik pizza classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu bir klasik pizza. "
  price = 50
  
class Margherita(Pizza):#Margherita classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu bir Margherita pizzası. "
  price = 60

class Turk(Pizza):#Türk pizza classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu bir Türk pizzası. "
  price = 70

class Sade(Pizza):#Sade pizza classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu bir Sade pizza. "
  price = 80


class Decorator(Pizza):
  def get_cost(self):
       return self.price 


  def get_description(self):
      return self.desc


class Zeytin(Decorator): #Zeytin classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu pizza zeytinli."
  price = 10

class Mantarlar(Decorator):#Mantarlar classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu pizza mantarlı."
  price = 12

class Peynir(Decorator):#Keçi peyniri classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu pizza Keçi Peynirli."
  price = 14

class Et(Decorator):#Et classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu pizza Etli."
  price = 16

class Sogan(Decorator):#Soğan classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu pizza Soğanlı."
  price = 18

class Misir(Decorator):#Mısır classı, bilgi ve fiyat bilgisini içeriyor.
  desc = "Bu pizza Mısırlı."
  price = 20



# Author: Bilal Berkam Dertli
import csv
import datetime

with open('Menu.txt', 'r') as file:
    text = file.read()
    print(text)



name = input("Merhaba, lütfen isminizi giriniz: ")

pizzaType = int(input(name + ", lütfen bir pizza tipi seçiniz: (1: Klasik / 2: Margarita / 3: TürkPizza / 4: Sade Pizza) "))

pizzaSos = int(input(name + ", lütfen bir pizza sosu seçiniz: (11: Zeytin / 12: Mantarlar / 13: Keçi Peyniri / 14: Et / 15: Soğan / 16: Mısır)"))

totalprice = 0 #Fiyatı tutacağımız değişken

taban = True #Yanlış tercih varsa diye kontrol etmek için
sos = True


if(pizzaType == 1): # Pizza tabanı tercihi klasik ise, klasik class objesi oluştur.
  mypizza = Klasik()
elif(pizzaType == 2): # Pizza tabanı tercihi margherita ise, margherita class objesi oluştur.
  mypizza = Margherita()
elif(pizzaType == 3): # Pizza tabanı tercihi Türk ise, Türk class objesi oluştur.
  mypizza = Turk()
elif(pizzaType == 4): # Pizza tabanı tercihi sade ise, sade class objesi oluştur.
   mypizza = Sade()
else:      #Bir yanlışlık varsa
  print("Yanlış pizza tabanı tercih yaptınız.")
  taban = False



if(pizzaSos == 11): #Sos tercihim zeytin ise, zeytin class objesi oluştur.
  mysauce = Zeytin()
elif(pizzaSos == 12):#Sos tercihim mantar ise, mantar class objesi oluştur.
  mysauce = Mantarlar()
elif(pizzaSos == 13):#Sos tercihim peynir ise, peynir class objesi oluştur.
  mysauce = Peynir()
elif(pizzaSos == 14):#Sos tercihim et ise, et class objesi oluştur.
   mysauce = Et()
elif(pizzaSos == 15):#Sos tercihim soğan ise, soğan class objesi oluştur.
   mysauce = Sogan()
elif(pizzaSos == 16):#Sos tercihim mısır ise, mısır class objesi oluştur.
   mysauce = Misir()   
else:      #Bir yanlışlık varsa
  print("Yanlış sos tercihi yaptınız.")  
  sos = False



if(sos and taban): # eğer tercihlerde eksik veya yanlışlık yoksa
  totalprice += mypizza.get_cost() + mysauce.get_cost()
  print(f"Toplam fiyat {totalprice} lira tuttu.")
  password = input("Ödeme için lütfen kredi kart şifrenizi giriniz: ")
  credit = input("Ödeme için lütfen kredi kart numaranızı giriniz: ")
  TC = input("Ödeme için lütfen TC numaranızı giriniz: ")
  
  generaldesc = mypizza.get_description()  + mysauce.get_description()
  

  
  # CSV dosyasını açmak için
  with open("Orders_Database.csv", "w", newline="") as csvfile:
      # csv yazmak için csv objesi oluşturma
      writer = csv.writer(csvfile)

      # başlık
      writer.writerow(["Kullanıcı adı: ", "Kimlik numarası:", "Fiyat:", "Açıklama", "Kart numarası:", "Kart şifresi:"])

      # bilgileri eklemek
      writer.writerow([name, TC, totalprice, generaldesc, credit, password])

else: #eğer tercihlerde yanlış olursa burası ekrana yazdırılacak.
  print("Tercihlerinizde eksik veya hata bulundu, lütfen daha sonra tekrar deneyiniz.")
