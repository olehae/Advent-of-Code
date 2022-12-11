with open('input1.txt') as f:
    lines = f.readlines()

summe = 0
summenliste = []
for i in lines:
    if i == '\n':
        summenliste.append(summe)
        summe = 0
    else:
        i.replace('\n', '')
        summe += int(i)

print(lines)
print(summenliste)

endsumme = 0

print(summenliste.index(max(summenliste)), max(summenliste))
endsumme += max(summenliste)
summenliste.remove(max(summenliste))
print(summenliste.index(max(summenliste)), max(summenliste))
endsumme += max(summenliste)
summenliste.remove(max(summenliste))
print(summenliste.index(max(summenliste)), max(summenliste))
endsumme += max(summenliste)
summenliste.remove(max(summenliste))
print(endsumme)
