import random
sayı1 = random.randint(1, 10)
sayı2 = random.randint(1, 10)
print(str(sayı1) + ' + ' + str(sayı2) + ' kaçtır?')
cevap = input()
if int(cevap) == sayı1 + sayı2:
    print('Doğru!')
else:
    print('Hayır. Cevap ' + str(sayı1 + sayı2))
