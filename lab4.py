def main():
    lista_pachete = []
    istoric_lista = []
    class pachet:
        def __init__(self, data_inceput, data_sfarsit, destinatie, pret):
            self.data_inceput = data_inceput
            self.data_sfarsit = data_sfarsit
            self.destinatie = destinatie
            self.pret = pret
        def __eq__(self, other):
            if isinstance(other, pachet):
                return (self.data_inceput == other.data_inceput and
                        self.data_sfarsit == other.data_sfarsit and
                        self.destinatie == other.destinatie and
                        self.pret == other.pret)
            return False

    def salveaza_stare(lista, istoric_lista):
        """
        Adauga starea curenta a listei de pachete de calatorie in istoric_lista
        """
        istoric_lista.append([p for p in lista])
    def adauga(lista, data1, data2, destinatie, pret):
        """
        Adauga in lista de pachete de calatorie un pachet nou cu caracteristicile introduse
        """
        salveaza_stare(lista, istoric_lista)
        lista.append(pachet(data1, data2, destinatie, pret))
        return lista
    def modifica(lista, j, data1, data2, destinatie, pret):
        """
        Modifica pachetul de calatorie selectat
        """
        salveaza_stare(lista, istoric_lista)
        lista[j].data_inceput = data1
        lista[j].data_sfarsit = data2
        lista[j].destinatie = destinatie
        lista[j].pret = pret
        return lista
    def adaugare(lista):
        """
        Afisseaza optiunea de a adauga un pachet de calatorie si optiunea de a modifica un pachet de calatorie, apoi citeste de la
        tastatura data de inceput, data de sfarsit, destinatia si pretul care vor fi atribuite pachetului de calatorie adaugat sau modificat
        """
        print('1 . Adauga pachet de calatorie.')
        print('2 . Modifica pachet de calatorie.')
        n = int(input('Alege o optiune:'))
        if n == 1:
            print('----------------------')
            data_inceput = input('Data inceput:')
            data_sfarsit = input('Data sfarsit:')
            destinatie = input('Destinatie:')
            pret = int(input('Pret:'))
            adauga(lista_pachete ,data_inceput, data_sfarsit, destinatie, pret)
        elif n == 2:
            k = 0
            for i in range(len(lista_pachete)):
                print(f"{k}. {lista_pachete[i].data_inceput} {lista_pachete[i].data_sfarsit} {lista_pachete[i].destinatie} {lista_pachete[i].pret}")
                k += 1
            if len(lista_pachete) != 0:
                j = int(input('Alege pachetul pe care doresti sa il modifici.'))
                if j >= 0 and j < len(lista_pachete):
                    data_inceput = input('Data inceput:')
                    data_sfarsit = input('Data sfarsit:')
                    destinatie = input('Destinatie:')
                    pret = int(input('Pret:'))
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
            salveaza_stare(lista, istoric_lista)
        lista = lista_noua
        return lista
    def sterge_zile(lista, nr_zile):
        """
        Sterge toate pachetele de calatorie care au durata in zile mai mica decat numarul de zile introdus
        """
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
            salveaza_stare(lista, istoric_lista)
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
            salveaza_stare(lista, istoric_lista)
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
        s = 0
        k = 0
        for i in range(len(lista)):
            if lista[i].destinatie == destinatie:
                s += lista[i].pret
                k += 1
        return s/k
    def filtrare_pret_destinatie(lista, pret, destinatie):
        lista_noua = []
        for i in range(len(lista)):
            if lista[i].destinatie == destinatie and lista[i].pret <= pret:
                lista_noua.append(lista[i])
        if lista != lista_noua:
            salveaza_stare(lista, istoric_lista)
        lista = lista_noua
        return lista_noua
    def filtrare_luna(lista, luna):
        lista_noua = []
        for i in range(len(lista)):
            if int(lista[i].data_inceput[3:5]) < luna and int(lista[i].data_sfarsit[3:5]) < luna or int(lista[i].data_inceput[3:5]) > luna and int(lista[i].data_sfarsit[3:5]) < luna or int(lista[i].data_inceput[3:5]) > luna and int(lista[i].data_sfarsit[3:5]) > luna:
                lista_noua.append(lista[i])
        if lista != lista_noua:
            salveaza_stare(lista, istoric_lista)
        lista = lista_noua
        return lista

    def undo(lista, istoric_lista):
        if istoric_lista:
            """
            Readuce lista de pachete de calatorii la starea de dinaintea ultimei modificari
            """
            lista_restaurata = istoric_lista.pop()
            lista.clear()
            lista.extend(lista_restaurata)

    def test_adauga():
        p1 = pachet("10.10.2024", "15.10.2024", "Cluj", 150)
        p2 = pachet("10.10.2024", "15.10.2024", "Cluj", 150)
        lista = [p1, p2]
        lista2 = [p1, p2, p2]
        adauga(lista, "10.10.2024", "15.10.2024", "Cluj", 150)
        assert lista == lista2
    def test_modifica():
        p1 = pachet("10.10.2024", "15.10.2024", "Cluj", 150)
        p2 = pachet("10.10.2024", "15.10.2024", "Cluj", 150)
        lista = [p1, p2]
        pachet_modificat = pachet("15.10.2024", "20.10.2024", "Sighisoara", 500)
        modifica(lista, 1, "15.10.2024", "20.10.2024", "Sighisoara", 500)
        assert lista[1] == pachet_modificat
    def test_sterge_destinatie():
        p1 = pachet("10.10.2024", "15.10.2024", "Cluj", 150)
        p2 = pachet("11.10.2024", "16.10.2024", "Sibiu", 200)
        p3 = pachet("12.10.2024", "17.10.2024", "Cluj", 250)
        lista = [p1, p2, p3]
        lista_asteptata = [p2]
        lista = sterge_destinatie(lista, "Cluj")
        assert lista == lista_asteptata
    def test_sterge_zile():
        p1 = pachet("10.10.2024", "12.10.2024", "Cluj", 150)
        p2 = pachet("11.10.2024", "16.10.2024", "Sibiu", 200)
        p3 = pachet("12.10.2024", "15.10.2024", "Brasov", 250)
        lista = [p1, p2, p3]
        lista_asteptata = [p2]
        lista = sterge_zile(lista, 4)
        assert lista == lista_asteptata
    def test_sterge_pret():
        p1 = pachet("10.10.2024", "15.10.2024", "Cluj", 100)
        p2 = pachet("11.10.2024", "16.10.2024", "Sibiu", 200)
        p3 = pachet("12.10.2024", "17.10.2024", "Brasov", 300)
        lista = [p1, p2, p3]
        lista_asteptata = [p1]
        lista = sterge_pret(lista, 150)
        assert lista == lista_asteptata
    def test_cautare_interval():
        p1 = pachet("10.10.2024", "15.10.2024", "test", 100)
        p2 = pachet("11.10.2025", "16.10.2025", "test", 200)
        p3 = pachet("12.10.2024", "17.10.2024", "test", 300)
        lista = [p1, p2, p3]
        lista_asteptata = [p2]
        lista = cautare_interval(lista, "10.10.2025", "20.10.2025")
        assert lista == lista_asteptata
    def test_cautare_destinatie_pret():
        p1 = pachet("10.10.2024", "15.10.2024", "test", 50)
        p2 = pachet("11.10.2025", "16.10.2025", "test", 200)
        p3 = pachet("12.10.2024", "17.10.2024", "test2", 50)
        lista = [p1, p2, p3]
        lista_asteptata = [p1]
        lista = cautare_destinatie_pret(lista, "test", 100)
        assert lista == lista_asteptata
    def test_cautare_data_sfarsit():
        p1 = pachet("10.10.2024", "15.10.2024", "test", 50)
        p2 = pachet("11.10.2025", "16.10.2025", "test", 200)
        p3 = pachet("12.10.2024", "17.10.2024", "test2", 50)
        lista = [p1, p2, p3]
        lista_asteptata = [p2]
        lista = cautare_data_sfarsit(lista, "16.10.2025")
        assert lista == lista_asteptata
    def test_rapoarte_destinatie():
        p1 = pachet("10.10.2024", "15.10.2024", "test", 50)
        p2 = pachet("11.10.2025", "16.10.2025", "test", 200)
        p3 = pachet("12.10.2024", "17.10.2024", "test2", 50)
        lista = [p1, p2, p3]
        assert rapoarte_destinatie(lista, "test") == 2
    def test_rapoarte_medie():
        p1 = pachet("10.10.2024", "15.10.2024", "test", 100)
        p2 = pachet("11.10.2025", "16.10.2025", "test", 200)
        p3 = pachet("12.10.2024", "17.10.2024", "test2", 50)
        lista = [p1, p2, p3]
        assert rapoarte_medie(lista, "test") == 150
    def test_filtrare_pret_destinatie():
        p1 = pachet("10.10.2024", "15.10.2024", "test", 50)
        p2 = pachet("11.10.2025", "16.10.2025", "test", 200)
        p3 = pachet("12.10.2024", "17.10.2024", "test2", 50)
        lista = [p1, p2, p3]
        lista_asteptata = [p1]
        assert filtrare_pret_destinatie(lista, 100, "test") == lista_asteptata
    def test_filtrare_luna():
        p1 = pachet("10.10.2024", "15.12.2024", "test", 50)
        p2 = pachet("11.10.2025", "16.11.2025", "test", 200)
        p3 = pachet("12.10.2024", "17.10.2024", "test2", 50)
        lista = [p1, p2, p3]
        lista_asteptata = [p3]
        assert filtrare_luna(lista, 11) == lista_asteptata

    test_adauga()
    test_modifica()
    test_sterge_destinatie()
    test_sterge_zile()
    test_sterge_pret()
    test_cautare_interval()
    test_cautare_destinatie_pret()
    test_cautare_data_sfarsit()
    test_rapoarte_destinatie()
    test_rapoarte_medie()
    test_filtrare_pret_destinatie()
    test_filtrare_luna()

    while True:
        print('1. Adaugare sau modificare pachet de calatorie')
        print('2. Stergere pachet de calatorie')
        print('3. Cautare pachet de calatorie')
        print('4. Rapoarte')
        print('5. Filtrare')
        print('6. Undo')
        print('7. Afisare pachete de calatorie')
        print('8. Iesire')
        print('----------------------')
        x = int(input('Alege o optiune:'))
        if x == 1:
            adaugare(lista_pachete)
        elif x == 2:
            print('1. Sterge toate pachetele de calatorie cu destinatia introdusa.')
            print('2. Sterge toate pachetele de calatorie cu durata mai mica decat numarul de zile introdus.')
            print('3. Sterge toate pachetele de calatorie care au pretul mai mare decat suma introdusa.')
            y = int(input('Alege o optiune:'))
            print('----------------------')
            if y == 1:
                destinatie = input('Destinatie:')
                lista_pachete = sterge_destinatie(lista_pachete, destinatie)
            elif y == 2:
                z = int(input('Numarul de zile:'))
                lista_pachete = sterge_zile(lista_pachete, z)
            elif y == 3:
                pret = int(input('Pret:'))
                lista_pachete = sterge_pret(lista_pachete, pret)
            else:
                print('Optiune invalida.')
        elif x == 3:
            print('1. Tiparirea pachetelor de calatorie din intervalul introdus.')
            print('2. Tiparirea pachetelor de calatorie cu destinatia introdusa si cu pretul mai mic decat cel introdus.')
            print('3. Tiparirea pachetelor de calatorie cu data de sfarsit introdusa.')
            y = int(input('Alege o optiune:'))
            print('----------------------')
            if y == 1:
                data_inceput = input('Data inceput(zz.ll.aaaa):')
                data_sfarsit = input('Data sfarsit(zz.ll.aaaa):')
                print('----------------------')
                cautare_interval(lista_pachete, data_inceput, data_sfarsit)
            elif y == 2:
                destinatie = input('Destinatie:')
                pret = int(input('Pret:'))
                print('----------------------')
                cautare_destinatie_pret(lista_pachete, destinatie, pret)
            elif y == 3:
                data_sfarsit = input('Data sfarsit(zz.ll.aaaa):')
                print('----------------------')
                cautare_data_sfarsit(lista_pachete, data_sfarsit)
        elif x == 4:
            print('1. Tiparirea numarului de oferte pentru destinatia introdusa.')
            print('2. Tiparirea pachetelor disponibile in intervalul introdus.')
            print('3. Tiparirea mediei de pret pentru destinatia introdusa.')
            y = int(input('Alege o optiune:'))
            print('----------------------')
            if y == 1:
                destinatie = input('Destinatie:')
                print('----------------------')
                rapoarte_destinatie(lista_pachete ,destinatie)
            elif y == 2:
                data_inceput = input('Data inceput(zz.ll.aaaa):')
                data_sfarsit = input('Data sfarsit(zz.ll.aaaa):')
                print('----------------------')
                rapoarte_interval(lista_pachete, data_inceput, data_sfarsit)
            elif y == 3:
                destinatie = input('Destinatie:')
                print('----------------------')
                print(f"Media preturilor pachetelor de calatorie cu destinatia {destinatie} este {rapoarte_medie(lista_pachete ,destinatie)}")
                print('----------------------')
            else:
                print('Optiune invalida.')
                print('----------------------')
        elif x == 5:
            print('1. Eliminare pachetelor de calatorie care au pretul mai mare decat cel introdus si destinatia diferita de cea introdusa.')
            print('2. Eliminarea pachetelor de calatorie ce presupun zile din luna introdusa.')
            y = int(input('Alege o optiune:'))
            print('----------------------')
            if y == 1:
                pret = int(input('Pret:'))
                destinatie = input('Destinatie:')
                print('----------------------')
                lista_pachete = filtrare_pret_destinatie(lista_pachete ,pret, destinatie)
            elif y == 2:
                luna = int(input('Luna(1-12):'))
                lista_pachete = filtrare_luna(luna)
        elif x == 6:
            undo(lista_pachete ,istoric_lista)
        elif x == 7:
            if len(lista_pachete) != 0:
                for i in range(len(lista_pachete)):
                    y = lista_pachete[i]
                    print(y.data_inceput, y.data_sfarsit, y.destinatie, y.pret)
            else:
                print('Nu exista pachete de calatorie.')
        elif x == 8:
            return
        else:
            print('Optiune invalida.')

if __name__ == '__main__':
    main()