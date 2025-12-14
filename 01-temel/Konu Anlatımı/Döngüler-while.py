# Python'daki ilk döngümüz 'while' döngüsüdür.
# while döngüsü şu şekilde kullanılır:
# i= 0  --> döngü değişkenini tanımlamalıyız.
# while koşul: --> Koşul doğru olduğu sürece while döngüsü çalışır.
#   codes 
#   codes
#   codes
#   i+= 1   --> Döngü değişkeninin değerini değiştirmemiz lazım. Yoksa sonsuz döngü olur. 
# Ben örnek olarak döngü değişkenini 1'er 1'er artırdım.

# Örnek kod: Ekrana 10 kere Hello World yazdıralım.😊
i= 0
# Döngü değişkeni 0'dan başladığı için 10 dahil edilmemeli, terim sayısı = (son terim- ilk terim)/ artış miktarı
while i< 10: 
  print("Hello World")
  i+= 1 # Döngü değişkenini 1'er 1'er artırıyoruz.
