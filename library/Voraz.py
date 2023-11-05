from library.Clases import Pacientes
from library.Clases import Hospital
from typing import List
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
    if Paciente.color == "rojo" or  Paciente.color == "naranja":
       Hospital1.colaPrincipal.append(Paciente) 
       Hospital1.colaPrincipal = quick_sort(Hospital1.colaPrincipal)  

       print("El paciente: ",Paciente.Nombre,Paciente.Apellido,"Fue asignado a la cola de prioridad principal")

       print("Cola Principal")
       for pac in range(len(Hospital1.colaPrincipal)):
           print(Hospital1.colaPrincipal[pac].Nombre, ", Color: ", Hospital1.colaPrincipal[pac].color)

       if Paciente in Hospital1.listaPacientes:
        Hospital1.listaPacientes.remove(Paciente)

        
       

    else:
        Hospital1.colaSecundario.append(Paciente) 
        Hospital1.colaSecundario = quick_sort (Hospital1.colaSecundario)

        print("El paciente: ",Paciente.Nombre,Paciente.Apellido,"Fue asignado a la cola de prioridad secundaria")
        
        print("Cola Secundaria")
        for pac in range(len(Hospital1.colaSecundario)):
           
           print(Hospital1.colaSecundario[pac].Nombre,", Color: ", Hospital1.colaSecundario[pac].color)
    
        if Paciente in Hospital1.listaPacientes:
            Hospital1.listaPacientes.remove(Paciente)

       

        

def quick_sort (colaP: List[Pacientes]):
    if len(colaP)<2:
        return colaP
    else:
        copia_cola = list(colaP)
        pivote = copia_cola.pop()
        mayores = []
        menores = []

        for pac in copia_cola:
            if pac.Beneficio > pivote.Beneficio:
                menores.append(pac)
            else:
                mayores.append(pac)
        return( quick_sort(menores) + [pivote] + quick_sort(mayores) )
    
    


def enfermerosdisp(Hospi: Hospital)->int:
    tiempo = time.localtime() 
    enfer:int
    if  23<=tiempo.tm_hour<6:
        Hospi.listaEnfermeros[0].Disponible = True
        Hospi.listaEnfermeros[1].Disponible = False
        Hospi.listaEnfermeros[2].Disponible = False
        Hospi.listaEnfermeros[3].Disponible = False
        Hospi.listaEnfermeros[4].Disponible = False
        enfer = 1
    elif 6<=tiempo.tm_hour<10:
        Hospi.listaEnfermeros[0].Disponible = True
        Hospi.listaEnfermeros[1].Disponible = True
        Hospi.listaEnfermeros[2].Disponible = False
        Hospi.listaEnfermeros[3].Disponible = False
        Hospi.listaEnfermeros[4].Disponible = False
        enfer = 2
    elif 10<=tiempo.tm_hour<16:
        Hospi.listaEnfermeros[0].Disponible = True
        Hospi.listaEnfermeros[1].Disponible = True
        Hospi.listaEnfermeros[2].Disponible = True
        Hospi.listaEnfermeros[3].Disponible = True
        Hospi.listaEnfermeros[4].Disponible = True
        enfer = 5

    elif 16<=tiempo.tm_hour<23:
        Hospi.listaEnfermeros[0].Disponible = True
        Hospi.listaEnfermeros[1].Disponible = True
        Hospi.listaEnfermeros[2].Disponible = True
        Hospi.listaEnfermeros[3].Disponible = False
        Hospi.listaEnfermeros[4].Disponible = False
        enfer = 3
    else:
        enfer = 0
    print("La cantidad de anfermeros disponibles es de",enfer)
    return enfer

def atender(Hosp: Hospital):
    if (len(Hosp.colaPrincipal)!= 0):
        print(Hosp.colaPrincipal[0].Nombre,"atendido")
        Hosp.colaPrincipal.remove(Hosp.colaPrincipal[0])
        
    else:
        print(Hosp.colaSecundario[0].Nombre,"atendido")
        Hosp.colaSecundario.remove(Hosp.colaSecundario[0])

def LecturaArch(Hosp: Hospital):
    
    with open(r"Prueba_Pac.csv") as file:
        reader  = csv.reader(file)
        for row in reader:
            nombre = row[0]
            apellido = row[1]
            dni = row[2]
            sintomas = [int(Sintoma) for Sintoma in row[3:]]
            paciente = Pacientes(nombre, apellido, dni,sintomas)
            Hosp.listaPacientes.append(paciente)
    return Hosp.listaPacientes
