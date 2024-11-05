from lab4functii import *
from lab4main import creeaza_pachet_de_calatorie

def test_adauga():
    """
    Functie de test pentru functia adauga
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "Cluj", 150)
    p2 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "Cluj", 150)
    lista = [p1, p2]
    lista2 = [p1, p2, p2]
    adauga(lista, "10.10.2024", "15.10.2024", "Cluj", 150)
    assert lista == lista2

def test_modifica():
    """
    Functie de test pentru functia modifica
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "Cluj", 150)
    p2 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "Cluj", 150)
    lista = [p1, p2]
    pachet_modificat = creeaza_pachet_de_calatorie("15.10.2024", "20.10.2024", "Sighisoara", 500)
    modifica(lista, 1, "15.10.2024", "20.10.2024", "Sighisoara", 500)
    assert lista[1] == pachet_modificat

def test_sterge_destinatie():
    """
    Functie de test pentru functia sterge_destinatie
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "Cluj", 150)
    p2 = creeaza_pachet_de_calatorie("11.10.2024", "16.10.2024", "Sibiu", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "17.10.2024", "Cluj", 250)
    lista = [p1, p2, p3]
    lista_asteptata = [p2]
    lista = sterge_destinatie(lista, "Cluj")
    assert lista == lista_asteptata

def test_sterge_zile():
    """
    Functie de test pentru functia sterge_zile
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "12.10.2024", "Cluj", 150)
    p2 = creeaza_pachet_de_calatorie("11.10.2024", "16.10.2024", "Sibiu", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "15.10.2024", "Brasov", 250)
    lista = [p1, p2, p3]
    lista_asteptata = [p2]
    lista = sterge_zile(lista, 4)
    assert lista == lista_asteptata

def test_sterge_pret():
    """
    Functie de test pentru functia sterge_pret
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "Cluj", 100)
    p2 = creeaza_pachet_de_calatorie("11.10.2024", "16.10.2024", "Sibiu", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "17.10.2024", "Brasov", 300)
    lista = [p1, p2, p3]
    lista_asteptata = [p1]
    lista = sterge_pret(lista, 150)
    assert lista == lista_asteptata

def test_cautare_interval():
    """
    Functie de test pentru functia cautare_interval
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "test", 100)
    p2 = creeaza_pachet_de_calatorie("11.10.2025", "16.10.2025", "test", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "17.10.2024", "test", 300)
    lista = [p1, p2, p3]
    lista_asteptata = [p2]
    lista = cautare_interval(lista, "10.10.2025", "20.10.2025")
    assert lista == lista_asteptata

def test_cautare_destinatie_pret():
    """
    Functie de test pentru functia cautare_destinatie_pret
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "test", 50)
    p2 = creeaza_pachet_de_calatorie("11.10.2025", "16.10.2025", "test", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "17.10.2024", "test2", 50)
    lista = [p1, p2, p3]
    lista_asteptata = [p1]
    lista = cautare_destinatie_pret(lista, "test", 100)
    assert lista == lista_asteptata

def test_cautare_data_sfarsit():
    """
    Functie de test pentru functia cautare_data_sfarsit.
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "test", 50)
    p2 = creeaza_pachet_de_calatorie("11.10.2025", "16.10.2025", "test", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "17.10.2024", "test2", 50)
    lista = [p1, p2, p3]
    lista_asteptata = [p2]
    lista = cautare_data_sfarsit(lista, "16.10.2025")
    assert lista == lista_asteptata

def test_rapoarte_destinatie():
    """
    Functie de test pentru functia rapoarte_destinatie
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "test", 50)
    p2 = creeaza_pachet_de_calatorie("11.10.2025", "16.10.2025", "test", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "17.10.2024", "test2", 50)
    lista = [p1, p2, p3]
    assert rapoarte_destinatie(lista, "test") == 2

def test_rapoarte_medie():
    """
    Functie de test pentru functia rapoarte_medie
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "test", 100)
    p2 = creeaza_pachet_de_calatorie("11.10.2025", "16.10.2025", "test", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "17.10.2024", "test2", 50)
    lista = [p1, p2, p3]
    assert rapoarte_medie(lista, "test") == 150

def test_filtrare_pret_destinatie():
    """
    Functie de test pentru functia filtrare_pret_destinatie
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.10.2024", "test", 50)
    p2 = creeaza_pachet_de_calatorie("11.10.2025", "16.10.2025", "test", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "17.10.2024", "test2", 50)
    lista = [p1, p2, p3]
    lista_asteptata = [p1]
    assert filtrare_pret_destinatie(lista, 100, "test") == lista_asteptata

def test_filtrare_luna():
    """
    Functie de test pentru functia filtrare_luna
    """
    p1 = creeaza_pachet_de_calatorie("10.10.2024", "15.12.2024", "test", 50)
    p2 = creeaza_pachet_de_calatorie("11.10.2025", "16.11.2025", "test", 200)
    p3 = creeaza_pachet_de_calatorie("12.10.2024", "17.10.2024", "test2", 50)
    lista = [p1, p2, p3]
    lista_asteptata = [p3]
    assert filtrare_luna(lista, 11) == lista_asteptata