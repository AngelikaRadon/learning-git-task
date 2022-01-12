List = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
newList = List[1:4] + List[5:10] + List[12:14]
print(newList)
newList1 = List[0:1] + List[4:5]+ List[10:12]
print(newList1)

lista_liczb = []
for liczba in range (0,100):
  if liczba %5 == 0:
    lista_liczb.append(liczba)
    print(lista_liczb)
    