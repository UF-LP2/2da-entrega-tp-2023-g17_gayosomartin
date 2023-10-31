from library.Clases import Pacientes
from library.Clases import Enfermeros
from library.Clases import Hospital
from library.Clases import Sintomas
from library.Voraz import asingar_beneficio
from library.Voraz import enfermerosdisp
from library.Voraz import asignar_a_Cola
from library.Voraz import LecturaArch
import time

def main() -> None:

 #funcion crear hosp 
  Hospi = Hospital()
  LecturaArch(Hospi)
  Enf1 = Enfermeros()
  Enf2 = Enfermeros()
  Enf3 = Enfermeros()
  Enf4 = Enfermeros()
  Enf5 = Enfermeros()
  Hospi.listaEnfermeros.append(Enf1)
  Hospi.listaEnfermeros.append(Enf2)
  Hospi.listaEnfermeros.append(Enf3)
  Hospi.listaEnfermeros.append(Enf4)
  Hospi.listaEnfermeros.append(Enf5)

  #funcion que lee el archivo de paciente y los va agregando a la lista general 
  contEnfermeros:int
  contEnfermeros= enfermerosdisp(Hospi)
  
  while (len(Hospi.listaPacientes) != 0):
    for i in range(1, contEnfermeros):
      if Hospi.listaEnfermeros[i].Disponible == True:

        if Hospi.listaPacientes[0].atencion == False:
          Hospi.listaEnfermeros[i].asignarcolor(Hospi.listaPacientes[0])
          asingar_beneficio(Hospi.listaPacientes[0])
          asignar_a_Cola(Hospi.listaPacientes[0],Hospi)

        elif  Hospi.listaPacientes[1].atencion == False:
          Hospi.listaEnfermeros[i].asignarcolor(Hospi.listaPacientes[1])
          asingar_beneficio(Hospi.listaPacientes[1])
          asignar_a_Cola(Hospi.listaPacientes[1],Hospi)

        elif  Hospi.listaPacientes[2].atencion == False:
          Hospi.listaEnfermeros[i].asignarcolor(Hospi.listaPacientes[2])
          asingar_beneficio(Hospi.listaPacientes[2])
          asignar_a_Cola(Hospi.listaPacientes[2],Hospi)

        elif  Hospi.listaPacientes[3].atencion == False:
          Hospi.listaEnfermeros[i].asignarcolor(Hospi.listaPacientes[3])
          asingar_beneficio(Hospi.listaPacientes[3])
          asignar_a_Cola(Hospi.listaPacientes[3],Hospi)

        elif  Hospi.listaPacientes[4].atencion == False:
          Hospi.listaEnfermeros[i].asignarcolor(Hospi.listaPacientes[4])
          asingar_beneficio(Hospi.listaPacientes[4])
          asignar_a_Cola(Hospi.listaPacientes[4],Hospi)
  
  
    while i==0: #true
        for p in Hospi.colaPrincipal:
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - Hospi.colaPrincipal[p].Tiempollegada  
            tiempo_que_queda = Hospi.colaPrincipal[p].tiempomax - tiempo_transcurrido
            if tiempo_transcurrido > Hospi.colaPrincipal[p].tiempomax
              #murio


    while True:
        for p in Hospi.colaSecundario:
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - Hospi.colaSecundario[p].Tiempollegada  
            tiempo_que_queda = Hospi.colaSecundario[p].tiempomax - tiempo_transcurrido
            if tiempo_que_queda <= 10:
               Hospi.colaSecundario[p].color = "rojo"

               
        


if __name__ == "__main__":
  main()
