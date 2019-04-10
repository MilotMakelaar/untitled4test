inlezen_str = eval(input("Geef lijst met minimaal 10 strings: "))
nieuwe_lijst = []
i = 0
for woord in inlezen_str:
    if (len(inlezen_str[i]) == 4):
        nieuwe_lijst.append(inlezen_str[i])
    i += 1

print('De nieuw-gemaakte lijst met alle vier-letter strings is:' + str(nieuwe_lijst))