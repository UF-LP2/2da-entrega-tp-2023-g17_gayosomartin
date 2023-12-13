from library.Clases import Pacientes
from library.Clases import Enfermeros
from library.Clases import Hospital
from library.Funciones import asignar_a_Cola
from library.Funciones import enfermerosdisp
from library.Funciones import atender
import time
import pytest
   

def test_QuickSort():
    Pac1 = Pacientes("Monica", "sdfg", "1111111", [4,3,1])
    Pac2 = Pacientes("luis", "jhgw", "3334", [3,5,9,2])
    Pac3 = Pacientes("Fabricio", "ahjld", "9732467", [6,7,0])
    Hosp = Hospital()
    Hosp.listaPacientes.append(Pac1)
    Hosp.listaPacientes.append(Pac2)
    Hosp.listaPacientes.append(Pac3)
    Enfermero = Enfermeros("Camila")
    Enfermero.asignarcolor(Pac1)
    Enfermero.asignarcolor(Pac2)
    Enfermero.asignarcolor(Pac3)
    asignar_a_Cola(Pac1, Hosp)
    asignar_a_Cola(Pac2, Hosp)
    asignar_a_Cola(Pac3, Hosp)
    assert Hosp.colaPrincipal == [Pac3, Pac1, Pac2]

def test_cantidad_enfermeros():
    Hosp = Hospital()
    Enf1 = Enfermeros("Enf1")
    Enf2 = Enfermeros("Enf2")
    Enf3 = Enfermeros("Enf3")
    Enf4 = Enfermeros("Enf4")
    Enf5 = Enfermeros("Enf5")
    Hosp.listaEnfermeros.append(Enf1)
    Hosp.listaEnfermeros.append(Enf2)
    Hosp.listaEnfermeros.append(Enf3)
    Hosp.listaEnfermeros.append(Enf4)
    Hosp.listaEnfermeros.append(Enf5)
    Cantidad = enfermerosdisp(Hosp)
    tiempo = time.localtime() 
    if  23<=tiempo.tm_hour<6:
        assert Cantidad == 1
    elif 6<=tiempo.tm_hour<10:
        assert Cantidad == 2
    elif 10<=tiempo.tm_hour<16:
        assert Cantidad == 5
    elif 16<=tiempo.tm_hour<23:
        assert Cantidad == 3

def test_Atender():
    Pac3 = Pacientes("Fabricio", "ahjld", "9732467", [6,7,0])
    Pac2 = Pacientes("luis", "jhgw", "3334", [3,5,9,2])
    Pac3.Beneficio=2
    Pac3.color = "rojo"
    Pac3.tiempomax = 1 
    Pac2.Beneficio=4
    Pac2.color = "naranja"
    Pac2.tiempomax = 10 
    Hosp=Hospital()
    Hosp.colaPrincipal.append(Pac3)
    Hosp.colaPrincipal.append(Pac2)
    atender(Hosp)
    assert Hosp.colaPrincipal == [Pac2]
    



    



    