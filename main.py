import mettds

islem = input("işlem seç fakt(F) yada kare için(K) :")

sayı = int(input(f"{islem} sayı gir :"))

if islem == "F":
    sonuc = mettds.faktor(sayi)
elif islem == "K":
    sonuc = mettds.kare(sayi)
else:
    print("yanlis giris amk")

print(sonuc)