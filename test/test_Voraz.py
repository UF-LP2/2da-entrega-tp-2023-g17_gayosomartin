from library.Clases import Pacientes
from library.Clases import Enfermeros
from library.Voraz import asignar_a_Cola
from library.Voraz import insertion_sort
from library.Voraz import asingar_beneficio
import pytest

def test_a_cola():
    pac1 = Pacientes("Maria","Fres","34789765",[0,8,5],0)
    pac2 = Pacientes("Maria","Fres","34789765",[2,4,5],0)
    pac3 = Pacientes("Maria","Fres","34789765",[9,8,7],0)
    pac4 = Pacientes("Maria","Fres","34789765",[16],0)
    Enfermero = Enfermeros(pac1)
    Enfermero.asignarcolor()
    Enfermero = Enfermeros(pac2)
    Enfermero.asignarcolor()
    Enfermero = Enfermeros(pac3)
    Enfermero.asignarcolor()
    Enfermero = Enfermeros(pac4)
    Enfermero.asignarcolor()
    ListaGeneral = []
    ListaGeneral.append(pac1,pac2,pac3,pac4)
    for i in range(i,len(ListaGeneral)):
        asignar_a_Cola(ListaGeneral[i])
    


    

def test_beneficio():
    Pac = Pacientes("marcos","diaz", "12099877",[7,3,2],0)
    asingar_beneficio(Pac)
    assert Pac.Beneficio == 4


    