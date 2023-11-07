
from library.Clases import Enfermeros
from library.Clases import Hospital
from library.Funciones import enfermerosdisp
from library.Funciones import asignar_a_Cola
from library.Funciones import LecturaArch
from library.Funciones import atender
from library.Funciones import Calcular_Tiempo

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
  
  while (len(Hospi.listaPacientes) != 0) :
    for i in range(contEnfermeros):
      print(Hospi.listaEnfermeros[i].name)
      print("--------------------------------------------------------------------------------------")
      if Hospi.listaEnfermeros[i].Disponible == True:  
        if len(Hospi.listaPacientes) > 0 and Hospi.listaPacientes[0].atencion == False:
          print("Se le asigna color al paciente ",Hospi.listaPacientes[0].Nombre,Hospi.listaPacientes[0].Apellido)
          Hospi.listaEnfermeros[i].asignarcolor(Hospi.listaPacientes[0])
          asignar_a_Cola(Hospi.listaPacientes[0],Hospi)

      if len(Hospi.listaPacientes) > 1 and i+1 < len(Hospi.listaEnfermeros) and Hospi.listaEnfermeros[i+1].Disponible == True:
        if Hospi.listaPacientes[1].atencion == False:
          print("Se le asigna color al paciente ",Hospi.listaPacientes[1].Nombre,Hospi.listaPacientes[1].Apellido)
          Hospi.listaEnfermeros[i+1].asignarcolor(Hospi.listaPacientes[1])
          asignar_a_Cola(Hospi.listaPacientes[1],Hospi)
        
      if len(Hospi.listaPacientes) > 2 and i+2 < len(Hospi.listaEnfermeros) and Hospi.listaEnfermeros[i+2].Disponible == True:
        if  Hospi.listaPacientes[2].atencion == False:
          print("Se le asigna color al paciente ",Hospi.listaPacientes[2].Nombre,Hospi.listaPacientes[2].Apellido)
          Hospi.listaEnfermeros[i+2].asignarcolor(Hospi.listaPacientes[2])
          asignar_a_Cola(Hospi.listaPacientes[2],Hospi)
        
      if len(Hospi.listaPacientes) > 4 and i+3 < len(Hospi.listaEnfermeros) and Hospi.listaEnfermeros[i+3].Disponible == True:
        if  Hospi.listaPacientes[3].atencion == False:
          print("Se le asigna color al paciente ",Hospi.listaPacientes[3].Nombre,Hospi.listaPacientes[3].Apellido)
          Hospi.listaEnfermeros[i+3].asignarcolor(Hospi.listaPacientes[3])
          asignar_a_Cola(Hospi.listaPacientes[3],Hospi)

      if len(Hospi.listaPacientes) > 5 and i+4 < len(Hospi.listaEnfermeros) and Hospi.listaEnfermeros[i+4].Disponible == True:
        if  Hospi.listaPacientes[4].atencion == False:
          print("Se le asigna color al paciente ",Hospi.listaPacientes[4].Nombre,Hospi.listaPacientes[4].Apellido)
          Hospi.listaEnfermeros[i+4].asignarcolor(Hospi.listaPacientes[4])
          asignar_a_Cola(Hospi.listaPacientes[4],Hospi)

    
    print("--------------------------------------------------------------------------------------")
    
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    Calcular_Tiempo(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
  
    
  while(len(Hospi.colaSecundario)!= 0 or len(Hospi.colaPrincipal)!= 0 ):
    Calcular_Tiempo(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    atender(Hospi)
    

if __name__ == "__main__":
  main()
