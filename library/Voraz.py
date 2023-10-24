from Clases import Pacientes
from collections import deque
from queue import Queue

def asignar_a_Cola(Paciente: Pacientes):
    if Paciente.color == "rojo" and  Paciente.color == "naranja":
        colaPrincipal = deque()
        colaPrincipal.append(Paciente)
        insertion_sort(colaPrincipal)

        

def insertion_sort (colaP:Queue):
    for j in range(1, len(colaP)):
        aux = colaP[j]

        i = j-1
        while i>= 0 and colaP[i]> aux:
            colaP[i+1] = colaP[i]
            i -= 1
            colaP[i+1]=aux




        
    



    