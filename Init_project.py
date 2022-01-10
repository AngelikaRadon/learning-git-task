lista_liczb = []
for liczba in range (0,100):
  if liczba %5 == 0:
    lista_liczb.append(liczba)
    print(liczba)
potegowanie = [p * p *p for p in lista_liczb]
print(potegowanie) 