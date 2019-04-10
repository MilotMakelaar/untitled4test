invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoer_lst = invoer.split('-')
invoerG = list(map(int, invoer_lst))
invoerG.sort()
max_lst = max(invoerG)
min_lst = min(invoerG)
aantalG = len(invoerG)
somG = sum(invoerG)
gemG = somG / aantalG

print('Gesorteerde list van ints: ' + str(invoerG) + '\n' + 'Grootste getal: ' + str(max_lst) + ' en Kleinste getal: ' + str(min_lst) + '\n' + 'Aantal getallen: ' + str(aantalG) + ' en Som van de getallen: ' + str(somG) + '\n' + 'Gemiddelde: ' + str(gemG))