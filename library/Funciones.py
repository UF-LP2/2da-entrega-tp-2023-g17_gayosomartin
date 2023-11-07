from library.Clases import Pacientes
from library.Clases import Hospital
from typing import List
from tkinter import Tk
import time
import csv



def asignar_a_Cola(Paciente: Pacientes, Hospital1: Hospital):
    if Paciente.color == "rojo" or  Paciente.color == "naranja":
       Hospital1.colaPrincipal.append(Paciente) 
       Hospital1.colaPrincipal = quick_sort(Hospital1.colaPrincipal)  

        #esta cola auxiliar la utilizamos apra mostrar en la interfaz
       Hospital1.colaAux.append(Paciente)
       Hospital1.colaAux = quick_sort(Hospital1.colaAux)  
        
       print("El paciente: ",Paciente.Nombre,Paciente.Apellido,"Fue asignado a la cola de prioridad principal")

       print("Cola Principal")
       for pac in range(len(Hospital1.colaPrincipal)):
           print(Hospital1.colaPrincipal[pac].Nombre, ", Color: ", Hospital1.colaPrincipal[pac].color)

       if Paciente in Hospital1.listaPacientes:
        Hospital1.listaPacientes.remove(Paciente)

    else:
        Hospital1.colaSecundario.append(Paciente) 
        Hospital1.colaSecundario = quick_sort (Hospital1.colaSecundario)

        Hospital1.colaAux.append(Paciente)
        Hospital1.colaAux = quick_sort(Hospital1.colaAux)  

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
            if pac.Beneficio <= pivote.Beneficio:
                menores.append(pac)
                
            else:
                mayores.append(pac)
        return( quick_sort(menores) + [pivote] + quick_sort(mayores) )
    
    


def enfermerosdisp(Hospi: Hospital)->int:
    
    tiempo = time.localtime()  
    enfer:int
    if  23==tiempo.tm_hour or 0<=tiempo.tm_hour<6:
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

def atender(Hosp: Hospital)->int:

    if (len(Hosp.colaPrincipal)!= 0):
        print(Hosp.colaPrincipal[0].Nombre,"atendido")
        Hosp.colaPrincipal.remove(Hosp.colaPrincipal[0])
        return 1
        
    elif(len(Hosp.colaSecundario)!= 0):
        print(Hosp.colaSecundario[0].Nombre,"atendido")
        Hosp.colaSecundario.remove(Hosp.colaSecundario[0])
        return 1
    else:
       print("No hay pacientes")
       return 0

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


def Calcular_Tiempo(Hospi:Hospital)->int:
    #if len(Hospi.colaPrincipal) != 0 :
    for p in range(len(Hospi.colaPrincipal)):
        if p < len(Hospi.colaPrincipal):
            print(Hospi.colaPrincipal[p].Nombre,Hospi.colaPrincipal[p].color, Hospi.colaPrincipal[p].Tiempollegada,Hospi.colaPrincipal[p].tiempomax)
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - Hospi.colaPrincipal[p].Tiempollegada    
            print(tiempo_transcurrido)
            tiempo_que_queda = Hospi.colaPrincipal[p].tiempomax - tiempo_transcurrido
            print(tiempo_que_queda)
            if tiempo_transcurrido > Hospi.colaPrincipal[p].tiempomax:
                print("murio")
                Hospi.colaPrincipal.remove(Hospi.colaPrincipal[p])
                return 1 # este return lo hacemos para saber cuanta gente murio
            else:
                print("todavia vive")
                return 0

    print("--------------------------------------------------------------------------------------")

    
    for k in range(len(Hospi.colaSecundario)):
      if k < len(Hospi.colaSecundario):
        print(Hospi.colaSecundario[k].Nombre,Hospi.colaSecundario[k].color, Hospi.colaSecundario[k].Tiempollegada,Hospi.colaSecundario[k].tiempomax)
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - Hospi.colaSecundario[k].Tiempollegada 
        print(tiempo_transcurrido) 
        tiempo_que_queda = Hospi.colaSecundario[k].tiempomax - tiempo_transcurrido 
        print(tiempo_que_queda)
        if tiempo_que_queda <= 10:
            Hospi.colaSecundario[k].color = "naranja"
            asignar_a_Cola(Hospi.colaSecundario[k],Hospi)
            Hospi.colaSecundario.remove(Hospi.colaSecundario[k])
            return 0
        else:
            print("todavia vive")
            return 0

    print("----------------------------------------------------------------------------------- ---")




