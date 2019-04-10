def inlezen_beginstation(stations):
    beginstation = input('Beginstation: ')
    if beginstation in stations:
        return beginstation
    else:
        print('Beginstation (Schagen-Maastricht): ')

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Eindstation: ')
    if eindstation.index() > beginstation.index():
        return eindstation
    else:
        print('Eindstation (Schagen-Maastricht): ')

def omroepen_reis(stations, beginstation, eindstation):
    print('Het beginstation ' + beginstation + 'is het ' + int(beginstation.index()) + 'station in het traject.')
    print('Het eindstation ' + eindstation + 'is het ' + int(eindstation.index()) + 'station in het traject.')
    afstand = eindstation.index() - beginstation.index()
    print('De afstand bedraagt ' + afstand + 'station(s).')
    prijs = int(afstand * 5)
    print('De prijs van het kaartje is ' + prijs + 'euro.')

stations = ['Schagen', 'Heerhugowaard','Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)