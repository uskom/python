import random
print('Bir parayı 1000 kere atacağım. Kaç kere tura geleceğini tahmin et.')
print('(Başlamak için Enter\'a bas)')
input()
kaçkere = 0
tura = 0
while kaçkere < 1000:
    if random.randint(0, 1) == 1:
        tura = tura + 1
    kaçkere = kaçkere + 1

    if kaçkere == 900:
        print('900 kere attım ve ' + str(tura) +  ' tanesi tura geldi')
    if kaçkere == 100:
        print('100 atıştan şimdilik ' + str(tura) + ' tanesi tura')
    if kaçkere == 500:
        print('Yarısı bitti ve gelen tura sayısı ' + str(tura))

print()
print('1000 atıştan ' + str(tura) + ' tanesi tura geldi!')
print('Tahminin yakınmıydı?')
        
    
