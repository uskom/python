import random

RESIMLER = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''

  +----+
  |    |
 [O    |
 /|\   |
 / \   |
       |
==========''', '''

  +----+
  |    |
 [O]   |
 /|\   |
 / \   |
       |
==========''']

kelimeler = {'Renkler':'kırmızı turuncu sarı yeşil mavi lacivert mor beyaz siyah \
             kahverengi'.split(),
             'Şekiller':'kare üçgen dörtgen daire elips beşgen altıgen yedigen \
             sekizgen'.split(),
             'Meyveler':'elma armut kiraz üzüm muz karpuz kavun çilek greyfurt \
             portakal'.split(),
             'Hayvanlar':'karınca porsuk yarasa ayı kunduz deve kedi istiridye kobra \
             puma çakal karga geyik köpek ördek kartal gelincik tilki kurbağa keçi \
             kaz şahin aslan kertenkele lama köstebek maymun geyik panda papağan \
             güvercin tavşan koç gergedan köpekbalığı koyun yılan örümcek leylek \
             kuğu kaplan kurbağa alabalık hindi kaplumbağa gelincik balina kurt \
             zebra'.split()}

def rastgeleKelimeSeç(sözlük):
    #  Bu işlev kendisine geçilen sözlükten rastgele bir kelime seçer
    #  İlkönce rastgele bir anahtar seç
    anahtar = random.choice(list(sözlük.keys()))

    #  Sonra listeden rastgele bir kelime seç
    no = random.randint(0, len(sözlük[anahtar]) - 1)
    return [sözlük[anahtar][no], anahtar]

def oyunTahtasınıGöster(RESIMLER, kullanılanHarfler, doğruHarfler, rastgeleKelime):
    print(RESIMLER[len(kullanılanHarfler)])
    print()

    print('Kullanılan harfler:', end = ' ')
    for harf in kullanılanHarfler:
        print(harf, end = ' ')
    print()

    boşluklar = '_' * len(gizliKelime)

    for i in range(len(gizliKelime)): # boşlukları doğru tahmin edilen harflerle yer değiştir
        if gizliKelime[i] in doğruHarfler:
            boşluklar = boşluklar[:i] + gizliKelime[i] + boşluklar[i + 1:]

    for harf in boşluklar:
        print(harf, end=' ')
    print()

def harfIste(tahminEdilenHarfler):
    # Kullanıcının girdiği harfi döndürür
    while True:
        print('Bir harf giriniz.')
        tahmin = input()
        tahmin = tahmin.lower()
        if (len(tahmin) != 1):
            print('Lütfen bir harf giriniz')
        elif tahmin in tahminEdilenHarfler:
            print('Zaten bu harfi kullanmıştınız. Tekrar deneyin')
        elif tahmin not in 'abcçdefgğhıijklmnoöprsştuüvyzqwx':
            print('Lütfen bir HARF girin')
        else:
            return tahmin

def tekrarOynamakİstiyor():
    # Eğer kullanıcı tekrar oynamak istiyorsa bu işlev True döndürür aksi halde False döndürür
    print('Tekrar oynamak istermisin? (evet hayır)')
    return input().lower().startswith('e')

print('A D A M  A S M A C A')
kullanılanHarfler = ''
doğruHarfler = ''
gizliKelime = rastgeleKelimeSeç(kelimeler)
gizliAnahtar = gizliKelime[1]
gizliKelime = gizliKelime[0]
oyunBitti = False

while True:
    oyunTahtasınıGöster(RESIMLER, kullanılanHarfler, doğruHarfler, gizliKelime)

    # Kullanıcıdan bir harf iste
    tahmin = harfIste(kullanılanHarfler + doğruHarfler)

    if tahmin in gizliKelime:
        doğruHarfler = doğruHarfler + tahmin

        # Oyuncu kazandı mı
        tümHarfleriBildi = True
        for i in range(len(gizliKelime)):
            if gizliKelime[i] not in doğruHarfler:
                tümHarfleriBildi = False
                break
        if tümHarfleriBildi:
            print('Evet! Gizli kelime "' + gizliKelime + '" idi! Oyunu kazandınız!')
            oyunBitti = True
    else:
        kullanılanHarfler = kullanılanHarfler + tahmin

        # Oyuncu tüm haklarını kullanıp kaybetti mi
        if len(kullanılanHarfler) == len(RESIMLER) - 1:
            oyunTahtasınıGöster(RESIMLER, kullanılanHarfler, doğruHarfler, gizliKelime)
            print('Oyunu kaybettiniz!\n')
            print(str(len(doğruHarfler)) + ' harfi bildiniz ' + str(len(kullanılanHarfler)), end = ' ')
            print('harfi bilemediniz. Kelime ' + gizliKelime + ' idi.')
            oyunBitti = True

    # Oyun bittiyse kullanıcıya tekrar oynamak isteyip istemediğini sor
    if oyunBitti:
        if tekrarOynamakİstiyor():
            kullanılanHarfler = ''
            doğruHarfler = ''
            oyunBitti = False
            gizliKelime = rastgeleKelimeSeç(kelimeler)
            gizliAnahtar = gizliKelime[1]
            gizliKelime = gizliKelime[0]
        else:
            break
