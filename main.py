from library.Clases import Pacientes
from library.Clases import Enfermeros
from library.Clases import Hospital
from library.Clases import Sintomas
from library.Voraz import asingar_beneficio
from library.Voraz import enfermerosdisp
from library.Voraz import asignar_a_Cola
from library.Voraz import LecturaArch
from library.Voraz import atender
import time

def main() -> None:
 #funcion crear hosp 
  Hospi = Hospital()
  LecturaArch(Hospi)
  Enf1 = Enfermeros("Enf1")
  Enf2 = Enfermeros("Enf2")
  Enf3 = Enfermeros("Enf3")
  Enf4 = Enfermeros("Enf4")
  Enf5 = Enfermeros("Enf5")
  Hospi.listaEnfermeros.append(Enf1)
  Hospi.listaEnfermeros.append(Enf2)
  Hospi.listaEnfermeros.append(Enf3)
  Hospi.listaEnfermeros.append(Enf4)
  Hospi.listaEnfermeros.append(Enf5)

  

  #funcion que lee el archivo de paciente y los va agregando a la lista general 
  
  contEnfermeros= enfermerosdisp(Hospi)
  
  while (len(Hospi.listaPacientes) != 0):
    for i in range(contEnfermeros):
      print(Hospi.listaEnfermeros[i].name)
      print("--------------------------------------------------------------------------------------")
      if Hospi.listaEnfermeros[i].Disponible == True:  
        if Hospi.listaPacientes[0].atencion == False:
          Hospi.listaEnfermeros[i].asignarcolor(Hospi.listaPacientes[0])
          asingar_beneficio(Hospi.listaPacientes[0])
          asignar_a_Cola(Hospi.listaPacientes[0],Hospi)

      if i+1 < len(Hospi.listaEnfermeros) and Hospi.listaEnfermeros[i+1].Disponible == True:
        if Hospi.listaPacientes[1].atencion == False:
          Hospi.listaEnfermeros[i+1].asignarcolor(Hospi.listaPacientes[1])
          asingar_beneficio(Hospi.listaPacientes[1])
          asignar_a_Cola(Hospi.listaPacientes[1],Hospi)
        
      if i+2 < len(Hospi.listaEnfermeros) and Hospi.listaEnfermeros[i+2].Disponible == True:
        if  Hospi.listaPacientes[2].atencion == False:
          Hospi.listaEnfermeros[i+2].asignarcolor(Hospi.listaPacientes[2])
          asingar_beneficio(Hospi.listaPacientes[2])
          asignar_a_Cola(Hospi.listaPacientes[2],Hospi)
        
      if i+3 < len(Hospi.listaEnfermeros) and Hospi.listaEnfermeros[i+3].Disponible == True:
        if  Hospi.listaPacientes[3].atencion == False:
          Hospi.listaEnfermeros[i+3].asignarcolor(Hospi.listaPacientes[3])
          asingar_beneficio(Hospi.listaPacientes[3])
          asignar_a_Cola(Hospi.listaPacientes[3],Hospi)

      if i+4 < len(Hospi.listaEnfermeros) and Hospi.listaEnfermeros[i+4].Disponible == True:
        if  Hospi.listaPacientes[4].atencion == False:
          Hospi.listaEnfermeros[i+4].asignarcolor(Hospi.listaPacientes[4])
          asingar_beneficio(Hospi.listaPacientes[4])
          asignar_a_Cola(Hospi.listaPacientes[4],Hospi)
    print("--------------------------------------------------------------------------------------")
    
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)

    for p in range(len(Hospi.colaPrincipal)):
      print(Hospi.colaPrincipal[p].Nombre,Hospi.colaPrincipal[p].color, Hospi.colaPrincipal[p].Tiempollegada,Hospi.colaPrincipal[p].tiempomax)
      tiempo_actual = time.time()
      tiempo_transcurrido = tiempo_actual - Hospi.colaPrincipal[p].Tiempollegada    
      print(tiempo_transcurrido)
      tiempo_que_queda = Hospi.colaPrincipal[p].tiempomax - tiempo_transcurrido
      print(tiempo_que_queda)
      if tiempo_transcurrido > Hospi.colaPrincipal[p].tiempomax:
        print("murio")
        Hospi.colaPrincipal.remove(Hospi.colaPrincipal[p])
      else:
        print("todavia vive")

    print("--------------------------------------------------------------------------------------")
      
    for k in range(len(Hospi.colaSecundario)):
      print(Hospi.colaSecundario[k].Nombre,Hospi.colaSecundario[k].color, Hospi.colaSecundario[k].Tiempollegada,Hospi.colaSecundario[k].tiempomax)
      tiempo_actual = time.time()
      tiempo_transcurrido = tiempo_actual - Hospi.colaSecundario[k].Tiempollegada 
      print(tiempo_transcurrido) 
      tiempo_que_queda = Hospi.colaSecundario[k].tiempomax - tiempo_transcurrido 
      print(tiempo_que_queda)
      if tiempo_que_queda <= 10:
        Hospi.colaSecundario[k].color = "naranja"
        asignar_a_Cola(Hospi.colaSecundario[k],Hospi)
      else:
        print("todavia vive")

    print("--------------------------------------------------------------------------------------")
    
  
  

               
        


if __name__ == "__main__":
  main()
