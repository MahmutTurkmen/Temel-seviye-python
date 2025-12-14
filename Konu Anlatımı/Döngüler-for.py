# Önce for döngüsünün nasıl kullanılacağını öğrenelim😊

# 1-) Değişkenin içinde for döngüsü ile gezinmek 
# (Bu str, list, set, tuple vb. için gerçerli, int, float vb. için değil.)
# isim değişkeninin bir string olduğunu varsayalım. 
# Biz bu değişkenin içinde, her bir harf için, döngü ile dolaşacağız.
# Döngü değişkenini istediğiniz şekilde seçebilirsiniz, ben i olarak seçtim.
# for i in isim: 
#     kod satırı
#     kod satırı
#     kod satırı
# for içindeki girinti bittiği zaman döngü biter.

# 2-) range fonksiyonu ile for kullanımı
#  range() --> Belirli bir aralık seçmemizi sağlar. 
#  Başlangıç değeri varsayılan olarak sıfır(0)'dır.
#  range(10) demek --> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 demektir.
#  range() başlangıç değerini dahil eder, bitiş değerini dahil etmez.
#  indeksleme 0'dan başladığı için 0 var 10 yok. Bu sayede 10 eleman oldu.
#  range(5, 10) demek --> 5, 6, 7, 8, 9 demektir.
#  Şimdi range()'da artık miktarini değiştirmeyi görelim.
#  range(5, 10, 3) demek --> 5, 8 demektir. 3'er 3'er artırdık.
#  range(20,0,-2) demek --> 20, 18, 16, 14, 12, 10, 8, 6, 4, 2 
#  0'ın olmayacağına dikkat edin! Bitiş değeri dahil değil ⚠️

# Şimdi basit bir örnek yapalım. Ekrana 10 kere Hello World yazdıralım😊
for i in range(10): 
    print("Hello World")
# Hadi 2. basit örneğimizi yapalım, bu sefer değişkenin içinde gezinelim.
isim= input("İsminizi girin: ")
print("İsminizdeki harfler: ")
for i in isim:
    print(i)
