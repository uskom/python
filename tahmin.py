# Bu bir sayı tahmin oyunudur
import random

tahminSayısı = 0

print('Merhaba! İsminiz nedir?')
isim = input()

sayı = random.randint(1, 20)
print('Selam, ' + isim + ', aklımdan 1 ile 20 arasında bir sayı tuttum')

while (tahminSayısı < 6):
    print('Tahmin et kaç.') # print'in önünde 4 boşluk var
    tahmin = input()
    tahmin = int(tahmin)

    tahminSayısı = tahminSayısı + 1

    if tahmin < sayı:
        print('Tuttuğum sayı daha büyük') # print'in önünde 8 boşluk var

    if tahmin > sayı:
        print('Tuttuğum sayı daha küçük')

    if tahmin == sayı:
        break

if tahmin == sayı:
    tahminSayısı = str(tahminSayısı)
    print('Tebrikler, ' + isim + '! ' + tahminSayısı + ' seferde sayıyı buldun')

if tahmin != sayı:
    sayı = str(sayı)
    print('Bulamadın. Tuttuğum sayı ' + sayı + ' idi')
