import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import aseegg as ag

dane = pd.read_csv(r"C:\Users\asiam\Desktop\KCK\zajecia13\sub-01-trial-010.csv", delimiter=',', engine='python', names=['number', '01', '02', '03', '04', 'wyswietlana'])

sygnal = dane['01']
liczba = dane['wyswietlana']

czestProbkowania = 200
czas=len(sygnal)/czestProbkowania
t=np.linspace(0,czas,czas*czestProbkowania)

przefiltrowany = ag.pasmowozaporowy(sygnal, czestProbkowania, 49, 51)
przefiltrowany2 = ag.pasmowoprzepustowy(przefiltrowany, czestProbkowania, 1, 50)

plt.subplot(3,1,1)
plt.plot(t, sygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")

plt.subplot(3,1,2)
plt.plot(t, przefiltrowany2)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")

plt.subplot(3,1,3)
plt.plot(t, liczba)
plt.xlabel("Czas [s]")
plt.ylabel("Liczba [-]")
plt.show()

reset=0
print ("Cyfry, na które patrzyła osoba badana - przed odflitrowaniem 'podwójnego mrugnięcia'")
for i in range (7564):
    wartosc = przefiltrowany2[i]
    if reset>liczba[i]:
        reset=0
    if reset<liczba[i]:
        if wartosc > 0.2:
            print(liczba[i])
            reset=liczba[i]
print ("Cyfry, na które patrzyła osoba badana - po odfiltrowaniu 'podwójnego mrugnięcia'")
for i in range (7564):
    wartosc = przefiltrowany2[i]
    if reset>liczba[i]:
        reset=0
    if reset<1:
        if wartosc > 0.2:
            print(liczba[i])
            reset=liczba[i]
