# Bu bir yorum satırıdır (yorumlar # ile başlar)
# Ekrana mesaj yazdırma
print("Hello World!") # Çıktı: Hello World!
print("Merhaba Python!") # Çıktı: Merhaba Python
# Kullanıcıdan giriş alma
isim = input("Adınızı girin: ")
# Veri tiplerini ekrana yazdırma
sayi = 42
pi = 3.14
dogru_mu = True
yanlis_mi = False

print("Senin adın: ",isim) # Örnek çıktı: Senin adın: Mahmut
print("Bir sayı: ",sayi) # Çıktı: 42
print("Pi sayısı: ",pi) # Çıktı: 3.14
print("Doğru mu: ",dogru_mu) # Çıktı: True
print("Yanlış mı: ",yanlis_mi) # Çıktı: False

# type() fonksiyonu ile tip kontrolü
print("isim değişkeninin tipi: ",type(isim).__name__)
print("sayi değişkeninin tipi: ",type(sayi).__name__)
print("pi değişkeninin tipi: ",type(pi).__name__)
print("dogru_mu değişkeninin tipi: ",type(dogru_mu).__name__)
print("yanlis_mi değişkeninin tipi: ",type(yanlis_mi).__name__)
