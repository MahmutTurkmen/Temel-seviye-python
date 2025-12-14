# Kullanıcıdan vize ve final notu alıp ortalamasını ve harf notunu bulan program.
vize = int(input("Vize notunu giriniz: (0-100 arası)"))
final = int(input("Final notunu girin: (0-100 arası)"))
ort = vize * 0.4 + final * 0.6 # Vize'nin %40'ı, Finalin %60'ı alınacak.

if ort >= 90:
  print(f"Harf notun: AA 🎉, ortalaman: {ort}, geçtin")
elif ort >= 80:
  print(f"Harf notun: BA 😄, ortalaman: {ort}, geçtin")
elif ort >= 70:
  print(f"Harf notun: BB 😊, ortalaman: {ort}, geçtin")
elif ort >= 60:
  print(f"Harf notun CB 👍, ortalaman: {ort}, geçtin")
elif ort >= 50:
  print(f"Harf notun CC ✅, ortalaman: {ort}, geçtin")
else:
  print(f"Harf notun: FF ❌, ortalaman: {ort}, kaldın")
