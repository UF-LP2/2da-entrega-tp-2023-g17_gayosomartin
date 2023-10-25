from library.Clases import Pacientes
from library.Clases import Enfermeros
import pytest

def test_Color():
    Paciente = Pacientes("Maria","Fres","34789765",[1,8,5],0)
    Enfermero = Enfermeros(Paciente)
    Enfermero.asignarcolor()
    assert Paciente.color == "naranja"

def test_Tiempo():
    Paciente = Pacientes("Maria","Fres","34789765",[0,8,5],0)
    Enfermero = Enfermeros(Paciente)
    Enfermero.asignarcolor()
    assert Paciente.tiempomax == 0

    