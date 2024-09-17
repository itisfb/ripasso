#1) Da lista1 = [1, 2, 3, 4, 5], creo lista2 che ha tutti i valori raddoppiati
lista1 = [1,2,3,4,5]
lista2 = []
for i in range(5):
    n = lista1[i] * 2
    lista2.append(n)    #essendo una lista vuota non posso assegnare valori ma devo usare append
print(lista1[i])
print(lista2[i])

#2) Trovo il fattoriale di un numero inserito in input
num = int(input('Inserisci un numero: '))
fatt = 1
for i in range(num,1,-1):
    fatt = fatt * i     #a ogni ciclo moltiplico fatt per la posizione attuale del ciclo
print(fatt)

#3) Dizionario: {"a": 1, "b": 2, "c": 3}, scambio la posizione tra chiave e valore
dizionario = {"a": 1, "b": 2, "c": 3}
dizionario_invertito = {}
for chiave, valore in dizionario.items():   #ciclo per ogni coppia chiave-valore
    dizionario_invertito[valore] = chiave
print(dizionario_invertito)
