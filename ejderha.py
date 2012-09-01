import random
import time

def girişBölümünüGöster():
    print('Ejderhalarla dolu topraklardasın. Önünde ')
    print('iki tane mağara görüyorsun. Mağaranın birindeki')
    print('ejderha arkadaş dostu ve hazinelerini seninle')
    print('paylaşacak. Diğer ejderha aç gözlü ve karnı aç,')
    print('seni gördüğü yerde yiyecek')
    print()

def mağaraSeç():
    mağara = ''
    while mağara != '1' and mağara != '2':
        print('Hangi mağaraya gitmek istersin? (1 ya da 2)')
        mağara = input()
    return mağara

def mağarayıKontrolEt(seçilenMağara):
    print('Mağaraya doğru yaklaşıyorsun')
    time.sleep(2)
    print('İçerisi karanlık ve ürkütücü')
    time.sleep(2)
    print('Büyük bir ejderha dışarı fırlar ve şimdi önünde! Ağzını kocaman açar ve..')
    print()
    time.sleep(2)

    arkadaşCanlısıMağara = random.randint(1, 2)

    if seçilenMağara == str(arkadaşCanlısıMağara):
        print('Sana hazineyi verir!')
    else:
        print('Seni bir lokmada yutar!')

tekrarOyna = 'evet'
while tekrarOyna == 'evet' or tekrarOyna == 'e':

    girişBölümünüGöster()

    mağaraNumarası = mağaraSeç()

    mağarayıKontrolEt(mağaraNumarası)

    print('Tekrar oynamak istiyormusun? (evet hayır)')
    tekrarOyna = input()
