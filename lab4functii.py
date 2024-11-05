from lab4main import creeaza_pachet_de_calatorie
from lab4main import lista_pachete, istoric_lista

def adauga(lista, data1, data2, destinatie, pret):
    """
    Adauga in lista de pachete de calatorie un pachet nou cu caracteristicile introduse
    """
    global lista_pachete
    lista.append(creeaza_pachet_de_calatorie(data1, data2, destinatie, pret))
    return lista

def modifica(lista, j, data1, data2, destinatie, pret):
    """
    Modifica pachetul de calatorie selectat
    """
    global lista_pachete
    lista[j] = creeaza_pachet_de_calatorie(data1, data2, destinatie, pret)
    return lista


def adaugare(lista):
    """
    Afisseaza optiunea de a adauga un pachet de calatorie si optiunea de a modifica un pachet de calatorie, apoi citeste de la
    tastatura data de inceput, data de sfarsit, destinatia si pretul care vor fi atribuite pachetului de calatorie adaugat sau modificat
    """
    global lista_pachete
    print('1 . Adauga pachet de calatorie.')
    print('2 . Modifica pachet de calatorie.')
    n = input('Alege o optiune:')
    while not n.isdigit():
        print('Optiune invalida.')
        n = input('Alege o optiune:')
    n = int(n)
    if n == 1:
        print('----------------------')
        data_inceput = input('Data inceput:')
        while not validare_data(data_inceput):
            print('Data introdusa este eronata.')
            data_inceput = input('Data inceput(zz.ll.aaaa):')
        data_sfarsit = input('Data sfarsit:')
        while not validare_data(data_sfarsit):
            print('Data introdusa este eronata.')
            data_sfarsit = input('Data inceput(zz.ll.aaaa):')
        data_in = get_data(data_inceput)
        data_sf = get_data(data_sfarsit)
        while calculare_zile(data_sf) < calculare_zile(data_in):
            print('Data de sfarsit trebuie sa fie dupa cea de inceput.')
            data_sfarsit = input('Data sfarsit(zz.ll.aaaa):')
            data_sf = get_data(data_sfarsit)
        destinatie = input('Destinatie:')
        pret = input('Pret:')
        while not pret.isdigit():
            print('Pretul introdus este eronat.')
            pret = input('Pret:')
        pret = int(pret)
        istoric_lista.append([p for p in lista])
        adauga(lista_pachete, data_inceput, data_sfarsit, destinatie, pret)
    elif n == 2:
        k = 0
        for i in range(len(lista_pachete)):
            print(
                f"{k}. {lista_pachete[i]['data_inceput']} {lista_pachete[i]['data_sfarsit']} {lista_pachete[i]['destinatie']} {lista_pachete[i]['pret']}")
            k += 1
        if len(lista_pachete) != 0:
            j = input('Alege pachetul pe care doresti sa il modifici.')
            while not j.isdigit():
                print('Valoare eronata.')
                j = input('Alege pachetul pe care doresti sa il modifici.')
            j = int(j)
            if j >= 0 and j < len(lista_pachete):
                data_inceput = input('Data inceput:')
                while not validare_data(data_inceput):
                    print('Data introdusa este eronata.')
                    data_inceput = input('Data inceput(zz.ll.aaaa):')
                data_sfarsit = input('Data sfarsit:')
                while not validare_data(data_sfarsit):
                    print('Data introdusa este eronata.')
                    data_sfarsit = input('Data inceput(zz.ll.aaaa):')
                data_in = get_data(data_inceput)
                data_sf = get_data(data_sfarsit)
                while calculare_zile(data_sf) < calculare_zile(data_in):
                    print('Data de sfarsit trebuie sa fie dupa cea de inceput.')
                    data_sfarsit = input('Data sfarsit(zz.ll.aaaa):')
                    data_sf = get_data(data_sfarsit)
                destinatie = input('Destinatie:')
                pret = input('Pret:')
                while not pret.isdigit():
                    print('Pretul introdus este eronat.')
                    pret = input('Pret:')
                pret = int(pret)
                istoric_lista.append([p for p in lista])
                modifica(lista_pachete, j, data_inceput, data_sfarsit, destinatie, pret)
            else:
                print('Acest pachet nu exista.')
        else:
            print('Nu exista nici un pachet.')
    else:
        print('Optiune invalida.')
    print('----------------------')

def sterge_destinatie(lista, destinatie):
    """
    Sterge toate pachetele de calatorie care au destinatia introdusa
    """
    lista_noua = []
    for i in range(len(lista)):
        if lista[i].destinatie != destinatie:
            lista_noua.append(lista[i])
    if lista == lista_noua:
        print('Nu a fost sters nici un pachet.')
        print('----------------------')
    else:
        istoric_lista.append([p for p in lista])
    lista = lista_noua
    return lista

def get_data(x):
    an = int(x[6:10])
    luna = int(x[3:5])
    zi = int(x[0:2])
    return (an, luna, zi)
def calculare_zile(data):
    """
    Calculeaza numarul numarul de zile pana la data introdusa
    """
    luni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    s = 0
    for j in range(data[0]):
        s += 365
        if (data[0] % 4 == 0 and data[0] % 100 > 0) or (data[0] % 400 != 0):
            s += 1
    for j in range(data[1]):
        s += luni[j]
    s += data[2]
    return s
def sterge_zile(lista, nr_zile):
    """
    Sterge toate pachetele de calatorie care au durata in zile mai mica decat numarul de zile introdus
    """
    lista_noua = []
    for i in range(len(lista)):
        data_in = get_data(lista[i].data_inceput)
        data_sf = get_data(lista[i].data_sfarsit)
        if calculare_zile(data_sf) - calculare_zile(data_in) >= nr_zile:
            lista_noua.append(lista[i])
    if lista == lista_noua:
        print('Nu a fost sters nici un pachet.')
        print('----------------------')
    else:
        istoric_lista.append([p for p in lista])
    lista = lista_noua
    return lista_noua

def sterge_pret(lista, pret):
    lista_noua = []
    for i in range(len(lista)):
        if lista[i].pret <= pret:
            lista_noua.append(lista[i])
    if lista == lista_noua:
        print('Nu a fost sters nici un pachet.')
        print('----------------------')
    else:
        istoric_lista.append([p for p in lista])
    lista = lista_noua
    return lista_noua

def transforma_data(data):
    """
    Transforma o data de forma zz.ll.aaaa intr-un tuple (an, luna, zi).
    """
    zi, luna, an = map(int, data.split('.'))
    return (an, luna, zi)

def verifica_interval(data1, data2, data3, data4):
    """
    Verifica daca data1 si data2 sunt in intervalul [data3, data4].
    """
    d1 = transforma_data(data1)
    d2 = transforma_data(data2)
    d3 = transforma_data(data3)
    d4 = transforma_data(data4)
    return d3 <= d1 <= d4 and d3 <= d2 <= d4

def cautare_interval(lista, data_in, data_sf):
    lista_noua = []
    for i in range(len(lista)):
        if verifica_interval(lista[i].data_inceput, lista[i].data_sfarsit, data_in, data_sf):
            if lista[i].destinatie != "test":
                print(lista[i].data_inceput, lista[i].data_sfarsit, lista[i].destinatie, lista[i].pret)
            lista_noua.append(lista[i])
    if lista == lista_noua:
        print('Nu a fost gasit nici un pachet.')
        print('----------------------')
    lista = lista_noua
    return lista

def cautare_destinatie_pret(lista, destinatie, pret):
    """
    Cauta si afiseaza pachetele de calatorie cu pretul mai mic decat cel introdus si cu destinatia introdusa
    """
    lista_noua = []
    k = 0
    for i in range(len(lista)):
        if lista[i].destinatie == destinatie and lista[i].pret < pret:
            if lista[i].destinatie != "test":
                print(lista[i].data_inceput, lista[i].data_sfarsit, lista[i].destinatie, lista[i].pret)
            lista_noua.append(lista[i])
            k += 1
    if k == 0 and lista[0].destinatie != "test":
        print('Nu a fost gasit nici un pachet.')
        print('----------------------')
    lista = lista_noua
    return lista

def cautare_data_sfarsit(lista, data_sfarsit):
    """
    Cauta si afiseaza pachetele de calatorie cu data de sfarsit introdusa
    """
    lista_noua = []
    for i in range(len(lista)):
        if lista[i].data_sfarsit == data_sfarsit:
            if lista[i].destinatie != "test":
                print(lista[i].data_inceput ,lista[i].data_sfarsit, lista[i].destinatie, lista[i].pret)
            lista_noua.append(lista[i])
    if len(lista_noua) == 0:
        print('Nu a fost gasit nici un pachet.')
    if lista[0].destinatie != "test":
        print('----------------------')
    lista = lista_noua
    return lista

def rapoarte_destinatie(lista, destinatie):
    k = 0
    """
    Afiseaza numarul de pachete de calatorie cu destinatia introdusa.
    """
    for i in range(len(lista)):
        if lista[i].destinatie == destinatie:
            k += 1
    if lista[0].destinatie != "test":
        print(f"Sunt {k} pachete de calatorie cu destinatia {destinatie}")
        print('----------------------')
    return k

def rapoarte_interval(lista, data_in, data_sf):
    """
    Afiseaza pachetele de calatorie din intervalul de date introdus.
    """
    lista_noua = []
    for i in range(len(lista)):
        if verifica_interval(lista[i].data_inceput, lista[i].data_sfarsit, data_in, data_sf):
            if lista[i].destinatie != "test":
                print(lista[i].data_inceput, lista[i].data_sfarsit, lista[i].destinatie, lista[i].pret)
            lista_noua.append(lista[i])
    if lista == lista_noua:
        print('Nu a fost gasit nici un pachet.')
        print('----------------------')
    lista = lista_noua
    return lista

def rapoarte_medie(lista, destinatie):
    """
    Calculeaza media de pret a pachetelor de calatorie cu destinatia introdusa.
    """
    s = 0
    k = 0
    for i in range(len(lista)):
        if lista[i].destinatie == destinatie:
            s += lista[i].pret
            k += 1
    return s/k

def filtrare_pret_destinatie(lista, pret, destinatie):
    """
    Elimina din lista pachetele de calatorie cu destinatia diferita de cea introdusa si pretul mai mare decat cel introdus.
    """
    lista_noua = []
    for i in range(len(lista)):
        if lista[i].destinatie == destinatie and lista[i].pret <= pret:
            lista_noua.append(lista[i])
    if lista != lista_noua:
        istoric_lista.append([p for p in lista])
    lista = lista_noua
    return lista_noua

def filtrare_luna(lista, luna):
    """
    Elimina din lista pachetele de calatorie ce presupun un sejur in luna introdusa.
    """
    lista_noua = []
    for i in range(len(lista)):
        if int(lista[i].data_inceput[3:5]) < luna and int(lista[i].data_sfarsit[3:5]) < luna or int(lista[i].data_inceput[3:5]) > luna and int(lista[i].data_sfarsit[3:5]) < luna or int(lista[i].data_inceput[3:5]) > luna and int(lista[i].data_sfarsit[3:5]) > luna:
            lista_noua.append(lista[i])
    if lista != lista_noua:
        istoric_lista.append([p for p in lista])
    lista = lista_noua
    return lista

def undo(lista_pachete, istoric_lista):
    """
    Readuce lista de pachete de calatorii la starea de dinaintea ultimei modificari
    """
    lista = []
    if len(istoric_lista) != 0:
        lista = istoric_lista.pop()
        return
    return lista

def validare_data(x):
    """
    Verifica daca data introdusa este corecta
    """
    return (len(x) == 10 and x[0:2].isdigit() and int(x[0:2]) < 32 and int(x[0:2]) != 0  and x[2] == "." and x[3:5].isdigit()
            and int(x[3:5]) < 13 and int(x[3:5]) != 0 and x[5] == "." and x[6:10].isdigit())