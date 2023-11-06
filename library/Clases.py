from enum import Enum
import random
from typing import List
#from collections import deque
from queue import Queue
import time

class Sintomas(Enum):
    Politraumatismograve = 0
    #----------------- ROJO
    Coma = 1
    Convulsiones = 2
    Hemorragiadigestiva = 3
    Isquemia = 4
    #---------------- NARANJA
    Cefaleabrusca = 5
    Paresia = 6
    Hipertensiónarterial = 7
    VértigoconAfectaciónVegetativa = 8
    Síncope = 9
    UrgenciasPsiquiátricas = 10
    #--------------------- AMARILLO
    Otalgias = 11  
    Odontalgias = 12 
    DoloresInespecíficosLeves = 13
    Traumatismos = 14
    Esguinces = 15
    #------------------------- VERDE 
    Laringitis = 16
    Gripe = 17
    Diarrea = 18
    Amigdalitis = 19
          
class Pacientes:
     def __init__(self,Nombre,Apellido, Dni, Zintomas: List[int]):    
          self.color = ""  #lo asigna un medico
          self.sintomas = Zintomas
          self.atencion = False #esta variable es para saber si el paciente esta siendo atendido o no
          self.tiempomax = 0
          self.Nombre = Nombre
          self.Apellido = Apellido
          self.Dni = Dni
          self.Beneficio = 0
          self.Tiempollegada = time.time()

class Enfermeros:
     def __init__(self,name):
          self.Disponible = True #si el medico esta dispoible true y si no false
          self.name = name
          
          
     def asignarcolor(self, Paciente: Pacientes): #si tenemos lista de sintomas buscamos el numero mas chiquico y usamos ese para asignar color
          self.Disponible = False
          
          Paciente.atencion = True

          numero_mas_chico = min(Paciente.sintomas)   
          if numero_mas_chico == 0:
               Paciente.color = "rojo"
               Paciente.tiempomax = 1 
               Paciente.Beneficio = 2
                   

          elif numero_mas_chico in range(1,5):
               Paciente.color = "naranja"
               Paciente.tiempomax = 10 #segundos
               Paciente.Beneficio = 4
               

          elif numero_mas_chico in range(5,11):
               Paciente.color = "amarillo"
               Paciente.tiempomax = 60 #segundos
               Paciente.Beneficio = 6
               

          elif numero_mas_chico in range(11,16):
               Paciente.color = "verde"
               Paciente.tiempomax = 120 #segundos
               Paciente.Beneficio = 8
               
          else:
                Paciente.color = "azul"
                Paciente.tiempomax = 240 #segundos
                Paciente.Beneficio = 10
               
          print("El color del paciente es ", Paciente.color)
          self.Disponible = True

       
class Hospital:
      def __init__(self):
           self.listaPacientes = []
           self.listaEnfermeros = []
           self.colaPrincipal = []
           self.colaSecundario = []
     
