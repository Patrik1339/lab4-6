from lab4ui import *

def creeaza_pachet_de_calatorie(data_inceput, data_sfarsit, destinatie, pret):
    pachet = {
        'data_inceput': data_inceput,
        'data_sfarsit': data_sfarsit,
        'destinatie': destinatie,
        'pret': pret
    }
    return pachet

p1 = creeaza_pachet_de_calatorie("05.12.2024", "15.12.2024", "Cluj", 150)
p2 = creeaza_pachet_de_calatorie("20.06.2025", "27.06.2025", "Mamaia", 150)
p3 = creeaza_pachet_de_calatorie("10.10.2024", "20.11.2024", "Sighisoara", 20)
p4 = creeaza_pachet_de_calatorie("10.10.2024", "20.08.2024", "Aiud", 50)
p5 = creeaza_pachet_de_calatorie("10.10.2024", "12.12.2024", "Sighisoara", 150)
lista_pachete = [p1, p2, p3, p4, p5]
istoric_lista = [[p1, p2, p3, p4, p5]]

def main():
    global lista_pachete
    global istoric_lista
    while True:
        meniu()
        x = input('Alege o optiune:')
        while not x.isdigit():
            print('Optiune invalida.')
            x = input('Alege o optiune:')
        x = int(x)
        if x == 6 and len(istoric_lista) == 0:
            print('Nu a fost realizata nici o modificare.')
        while len(lista_pachete) == 0 and x != 1 and x != 8 and x != 6:
            print('Nu exista nici un pachet de calatorie.')
            print('----------------------')
            meniu()
            x = input('Alege o optiune:')
            while not x.isdigit():
                print('Optiune invalida.')
                x = input('Alege o optiune:')
            x = int(x)
        if x == 1:
            adaugare(lista_pachete)
        elif x == 2:
            print('1. Sterge toate pachetele de calatorie cu destinatia introdusa.')
            print('2. Sterge toate pachetele de calatorie cu durata mai mica decat numarul de zile introdus.')
            print('3. Sterge toate pachetele de calatorie care au pretul mai mare decat suma introdusa.')
            y = input('Alege o optiune:')
            while not y.isdigit():
                print('Optiune invalida.')
                y = input('Alege o optiune:')
            y = int(y)
            print('----------------------')
            if y == 1:
                destinatie = input('Destinatie:')
                lista_pachete = sterge_destinatie(lista_pachete, destinatie)
            elif y == 2:
                z = input('Numarul de zile:')
                while not z.isdigit():
                    print('Numarul de zile este eronat.')
                    z = input('Numarul de zile:')
                z = int(z)
                lista_pachete = sterge_zile(lista_pachete, z)
            elif y == 3:
                pret = input('Pret:')
                while not pret.isdigit():
                    print('Valoare eronata.')
                    pret = input('Pret:')
                pret = int(pret)
                lista_pachete = sterge_pret(lista_pachete, pret)
            else:
                print('Optiune invalida.')
        elif x == 3:
            print('1. Tiparirea pachetelor de calatorie din intervalul introdus.')
            print(
                '2. Tiparirea pachetelor de calatorie cu destinatia introdusa si cu pretul mai mic decat cel introdus.')
            print('3. Tiparirea pachetelor de calatorie cu data de sfarsit introdusa.')
            y = input('Alege o optiune:')
            while not y.isdigit():
                print('Optiune invalida.')
                y = input('Alege o optiune:')
            y = int(y)
            print('----------------------')
            if y == 1:
                data_inceput = input('Data inceput(zz.ll.aaaa):')
                while not validare_data(data_inceput):
                    print('Data introdusa este eronata.')
                    data_inceput = input('Data inceput(zz.ll.aaaa):')
                data_sfarsit = input('Data sfarsit(zz.ll.aaaa):')
                while not validare_data(data_sfarsit):
                    print('Data introdusa este eronata.')
                    data_sfarsit = input('Data inceput(zz.ll.aaaa):')
                print('----------------------')
                cautare_interval(lista_pachete, data_inceput, data_sfarsit)
            elif y == 2:
                destinatie = input('Destinatie:')
                pret = input('Pret:')
                while not pret.isdigit():
                    print('Pretul este eronat.')
                    pret = input('Pret:')
                pret = int(pret)
                print('----------------------')
                cautare_destinatie_pret(lista_pachete, destinatie, pret)
            elif y == 3:
                data_sfarsit = input('Data sfarsit(zz.ll.aaaa):')
                while not validare_data(data_sfarsit):
                    print('Data introdusa este eronata.')
                    data_sfarsit = input('Data inceput(zz.ll.aaaa):')
                print('----------------------')
                cautare_data_sfarsit(lista_pachete, data_sfarsit)
        elif x == 4:
            print('1. Tiparirea numarului de oferte pentru destinatia introdusa.')
            print('2. Tiparirea pachetelor disponibile in intervalul introdus.')
            print('3. Tiparirea mediei de pret pentru destinatia introdusa.')
            y = input('Alege o optiune:')
            while not y.isdigit():
                print('Optiune invalida.')
                y = input('Alege o optiune:')
            y = int(y)
            print('----------------------')
            if y == 1:
                destinatie = input('Destinatie:')
                print('----------------------')
                rapoarte_destinatie(lista_pachete, destinatie)
            elif y == 2:
                data_inceput = input('Data inceput(zz.ll.aaaa):')
                while not validare_data(data_inceput):
                    print('Data introdusa este eronata.')
                    data_inceput = input('Data inceput(zz.ll.aaaa):')
                data_sfarsit = input('Data sfarsit(zz.ll.aaaa):')
                while not validare_data(data_sfarsit):
                    print('Data introdusa este eronata.')
                    data_sfarsit = input('Data inceput(zz.ll.aaaa):')
                print('----------------------')
                rapoarte_interval(lista_pachete, data_inceput, data_sfarsit)
            elif y == 3:
                destinatie = input('Destinatie:')
                print('----------------------')
                print(
                    f"Media preturilor pachetelor de calatorie cu destinatia {destinatie} este {rapoarte_medie(lista_pachete, destinatie)}")
                print('----------------------')
            else:
                print('Optiune invalida.')
                print('----------------------')
        elif x == 5:
            print(
                '1. Eliminare pachetelor de calatorie care au pretul mai mare decat cel introdus si destinatia diferita de cea introdusa.')
            print('2. Eliminarea pachetelor de calatorie ce presupun zile din luna introdusa.')
            y = input('Alege o optiune:')
            while not y.isdigit():
                print('Optiune invalida.')
                y = input('Alege o optiune:')
            y = int(y)
            print('----------------------')
            if y == 1:
                pret = input('Pret:')
                while not pret.isdigit():
                    print('Optiune invalida.')
                    pret = input('Pret:')
                pret = int(pret)
                destinatie = input('Destinatie:')
                print('----------------------')
                lista_pachete = filtrare_pret_destinatie(lista_pachete, pret, destinatie)
            elif y == 2:
                luna = input('Luna(1-12):')
                while not luna.isdigit():
                    print('Valoare eronata.')
                    luna = input('Luna(1-12):')
                luna = int(luna)
                while not (luna < 13 and luna != 0):
                    print('Luna introdusa este eronata.')
                    luna = input('Luna(1-12):')
                    while not luna.isdigit():
                        print('Valoare eronata.')
                        luna = input('Luna(1-12):')
                    luna = int(luna)
                lista_pachete = filtrare_luna(lista_pachete, luna)
        elif x == 6:
            lista_pachete.clear()
            lista_pachete.extend(undo(lista_pachete, istoric_lista))
        elif x == 7:
            if len(lista_pachete) != 0:
                for i in range(len(lista_pachete)):
                    y = lista_pachete[i]
                    print(y['data_inceput'], y['data_sfarsit'], y['destinatie'], y['pret'])
            else:
                print('Nu exista pachete de calatorie.')
        elif x == 8:
            return
        else:
            print('Optiune invalida.')

if __name__ == '__main__':
    main()