max = 100
min = 1
tahmin = 50
bitis = False
print("Aşağı için a , yukarı için y , doğruysa d")
def nextguess():
    global max,min,tahmin
    tahmin = (min+max)/2
    return tahmin
while bitis == False :
    giris = input(f"Tuttuğunuz sayı {int(tahmin)} mi ?")
    if giris == "a":
        max = tahmin
        nextguess()
    elif giris == "y":
        min = tahmin
        nextguess()
    elif giris == "d":
        print("Ben kazandım.")
        bitis = True
        break