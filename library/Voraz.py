from Clases import Pacientes
from collections import deque
from queue import Queue

def asingar_beneficio(Paciente: Pacientes):
    if Paciente.color == "rojo":
        Paciente.Beneficio = 2
    elif Paciente.color == "naranja":
        Paciente.Beneficio = 4
    elif Paciente.color == "amarillo":
        Paciente.Beneficio = 6
    elif Paciente.color == "verde":
        Paciente.Beneficio = 8
    else:
        Paciente.Beneficio =10

def asignar_a_Cola(Paciente: Pacientes):
    if Paciente.color == "rojo" and  Paciente.color == "naranja":
        colaPrincipal = deque()
        colaPrincipal.append(Paciente)
        insertion_sort(colaPrincipal)
    else:
        colaSecundaria = deque()
        colaSecundaria.append(Paciente)
        insertion_sort(colaSecundaria)

        

def insertion_sort (colaP:Queue [Pacientes]):
    for j in range(1, len(colaP)):
        aux = colaP[j]
        
        i = j-1
        while i>= 0 and colaP[i].Beneficio> aux.Beneficio:
            colaP[i+1] = colaP[i]
            i -= 1
            colaP[i+1]=aux




        
    



    