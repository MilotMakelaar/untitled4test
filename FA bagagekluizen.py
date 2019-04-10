print('1: Ik wil weten hoeveel kluizen nog vrij zijn ')
print('2: Ik wil een nieuwe kluis ')
print('3: Ik wil even iets uit mijn kluis halen ')
print('4: Ik geef mijn kluis terug ')
keuze = int(input('Welke optie kiest u: '))

aantal_kluizen = 12
aantal_beskluizen = 12
if keuze == 1:
    def toon_aantal_kluizen_vrij():
        print('Er zijn {} kluizen vrij.'.format(aantal_kluizen))
else:
        print('Er is een type error gevonden, voer hele getallen in.')

kluisnummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
def nieuwe_kluis():
    if keuze == 2:
        for kluisnummer in kluisnummers():
            print(kluisnummer, end = ', ')
            kluis_keuze = int(input('Welk kluisnummer wil je? t/m 12'))
        print('U krijgt kluisnummer: {}.'.format(kluis_keuze))
        ww = input('Wat is uw wachtwoord: ')
    else:

def kluis_openen():
    if keuze == 3:
        for kluisnummer in kluisnummers():
            ww2 = input('Wat is uw wachtwoord? ')
        elif ww == ww2:
            print('Uw kluis gaat nu open')
            kluisnummers.append(kluisnummer)
    else:
        print('Het wachtwoord is onjuist')

def kluis_teruggeven():
    if keuze == 4:
        print('Uw kluis is opgeheven')