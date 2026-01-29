lista = [1,3,4,2]


for i in range(len(lista)):
	smallest=lista[i]
	for item in lista[i:]:
		if 	item < smallest:
			smallest = item
	lista[lista.index(smallest)] ,lista[lista.index(item)] = lista[lista.index(item)] ,lista[lista.index(smallest)] 
		
print(lista)