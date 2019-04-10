getal_lijst = []
while True:
    getal = float(input('Geef een getal: '))
    if getal != 0:
        getal_lijst.append(getal)
        aantal = len(getal_lijst)
        som = sum(getal_lijst)
    else:
        break
print('Er zijn ' + str(aantal) + ' getallen ingevoerd, de som is: ' + str(som))