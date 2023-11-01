from enum import Enum
import random
from typing import List
from collections import deque
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
     def __init__(self):
          self.Disponible = True #si el medico esta dispoible true y si no false
          
          
     def asignarcolor(self, Paciente: Pacientes): #si tenemos lista de sintomas buscamos el numero mas chiquico y usamos ese para asignar color
          self.Disponible = False
          Paciente.atencion = True

          numero_mas_chico = min(self.Paciente.sintomas)
          if numero_mas_chico == 0:
               self.Paciente.color = "rojo"
               self.tiempomax = 0 
               
               

          elif numero_mas_chico in range(1,5):
               self.Paciente.color = "naranja"
               self.tiempomax = 10 #segundos
               

          elif numero_mas_chico in range(5,11):
               self.Paciente.color = "amarillo"
               self.tiempomax = 60 #segundos
               

          elif numero_mas_chico in range(11,16):
               self.Paciente.color = "verde"
               self.tiempomax = 120 #segundos
               
          else:
                self.Paciente.color = "azul"
                self.tiempomax = 240 #segundos
               
          print("El color del paciente es ", self.Paciente.color)
          self.Disponible = True

       
class Hospital:
      def __init__(self):
           self.listaPacientes = [Pacientes]
           self.listaEnfermeros = [Enfermeros]
           self.colaPrincipal = Queue()
           self.colaSecundario = Queue()
     