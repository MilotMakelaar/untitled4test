zin = input('Voer een willekeurige zin in: ')
def gemiddelde(invoer):
    lst = [len(x) for x in invoer.split()]
    gem = sum(lst) / len(lst)
    return round(gem, 2)
print('De gemiddelde lengte van de woorden in de zin is: ' + str(gemiddelde(zin)))