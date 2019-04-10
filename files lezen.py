kaartnr1 = open('kaartnummers.txt', 'w')
kaartnr1.write('325255, Jan Jansen\n334343, Erik Materus\n235434, Ali Ahson\n645345, Eva Versteeg\n534545, Jan de Wilde\n345355, Henk de Vries')
kaartnr1.close()

with open('kaartnummers.txt') as k:
    for gegevens in k:
        gegevensA = gegevens.split(',')
        naam = (gegevensA[1].strip())
        kaartnummer = gegevensA[0]
        print(naam + ' heeft kaartnummer: ' + kaartnummer)