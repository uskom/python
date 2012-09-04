import random

resimler = ['''

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
=========''']

kelimeler = 'karınca porsuk yarasa ayı kunduz deve kedi istiridye kobra puma çakal karga geyik köpek eşek ördek kartal gelincik tilki kurbağa keçi kaz şahin aslan kertenkele lama köstebek maymun geyik fare panda papağan güvercin tavşan koç gergedan köpekbalığı koyun yılan örümcek leylek kuğu kaplan kurbağa alabalık hindi kaplumbağa gelincik balina kurt zebra'.split()

def rastgeleKelimeSeç(kelimeListesi):
    # Bu işlev kendisine geçilen listeden rastgele bir kelime seçer
    no = random.randint(0, len(kelimeListesi) - 1)
    return kelimeListesi[no]

print('A D A M  A S M A C A')
