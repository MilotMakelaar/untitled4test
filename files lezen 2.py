teller1 = 0
with open('kaartnummers.txt') as k:
    for gegevens in k:
        teller1 += 1
    print('Deze file telt ' + str(teller1) + ' regels')

infile = open('kaartnummers.txt', 'r')
lst = []
for lineList in infile.readlines():
    item = lineList.split(',')
    kaartnr = item[0]
    lst.append(kaartnr)
grootsteKaartnr = max(lst)
regelKaartnr = lst.index(grootsteKaartnr) + 1
print('Het grootste kaartnummer is: ' + str(grootsteKaartnr) + ' en dat staat op regel ' + str(regelKaartnr))