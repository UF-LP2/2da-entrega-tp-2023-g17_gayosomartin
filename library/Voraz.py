from library.Clases import Pacientes
from library.Clases import Hospital
from collections import deque
from queue import Queue
import time
import csv

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

def asignar_a_Cola(Paciente: Pacientes, Hospital1: Hospital):
    if Paciente.color == "rojo" and  Paciente.color == "naranja":
       Hospital1.colaPrincipal.put(Paciente) 
       insertion_sort(Hospital1.colaPrincipal)
       Hospital1.listaPacientes.remove(Paciente)

    else:
        Hospital1.colaSecundario.put(Paciente) 
        insertion_sort(Hospital1.colaSecundario)
        Hospital1.listaPacientes.remove(Paciente)

        

def insertion_sort (colaP:Queue [Pacientes]):
    for j in range(1, len(colaP)):
        aux: Pacientes = colaP[j]
        
        i = j-1
        while i>= 0 and colaP[i].Beneficio> aux.Beneficio:
            colaP[i+1] = colaP[i]
            i -= 1
            colaP[i+1]=aux


def enfermerosdisp(Hospi: Hospital)->int:
    tiempo = time.localtime() 
    if  23<tiempo.tm_hour<6:
        Hospi.listaEnfermeros[0].Disponible = True
        Hospi.listaEnfermeros[1].Disponible = False
        Hospi.listaEnfermeros[2].Disponible = False
        Hospi.listaEnfermeros[3].Disponible = False
        Hospi.listaEnfermeros[4].Disponible = False
    elif 6<tiempo.tm_hour<10:
        Hospi.listaEnfermeros[0].Disponible = True
        Hospi.listaEnfermeros[1].Disponible = True
        Hospi.listaEnfermeros[2].Disponible = False
        Hospi.listaEnfermeros[3].Disponible = False
        Hospi.listaEnfermeros[4].Disponible = False
    elif 10<tiempo.tm_hour<16:
        Hospi.listaEnfermeros[0].Disponible = True
        Hospi.listaEnfermeros[1].Disponible = True
        Hospi.listaEnfermeros[2].Disponible = True
        Hospi.listaEnfermeros[3].Disponible = True
        Hospi.listaEnfermeros[4].Disponible = True
    elif 16<tiempo.tm_hour<23:
        Hospi.listaEnfermeros[0].Disponible = True
        Hospi.listaEnfermeros[1].Disponible = True
        Hospi.listaEnfermeros[2].Disponible = True
        Hospi.listaEnfermeros[3].Disponible = False
        Hospi.listaEnfermeros[4].Disponible = False


def atender(Hosp: Hospital):
    if (len(Hosp.colaPrincipal)!= 0):
        Hosp.colaPrincipal.get(Hosp.colaPrincipal[0])
    else:
        Hosp.colaSecundario.get(Hosp.colaSecundario[0])

def LecturaArch(Hosp: Hospital):
    
    with open(r"Pacinetes_Data.csv") as file:
        reader  = csv.reader(file)
        for row in reader:
            Hosp.listaPacientes.append(row)
    return Hosp.listaPacientes