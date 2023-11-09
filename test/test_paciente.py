from library.Clases import Pacientes
from library.Clases import Enfermeros
import pytest

def test_ColorNaranja():
    Paciente = Pacientes("Maria","Fres","34789765",[1,8,5])
    Enfermero = Enfermeros("Enf")
    Enfermero.asignarcolor(Paciente)
    assert Paciente.color == "naranja"

def test_NotColorAzul():
    Paciente = Pacientes("Paula", "Martin", "356842", [2,4,9])
    Enf = Enfermeros("Mario")
    Enf.asignarcolor(Paciente)

    assert Paciente.color != "Azul"

def test_Tiempo():
    Paciente = Pacientes("Maria","Fres","34789765",[0,8,5])
    Enfermero = Enfermeros("luis")
    Enfermero.asignarcolor(Paciente)
    assert Paciente.tiempomax == 4

def test_Beneficio():
 Paciente = Pacientes("Maria","Fres","34789765",[0,8,5])
 Enfermero = Enfermeros("luis")
 Enfermero.asignarcolor(Paciente)
 assert Paciente.Beneficio == 2
    

    