from library.Clases import Pacientes
from library.Clases import Enfermeros
from library.Clases import Hospital
from library.Clases import Sintomas
from library.Voraz import asingar_beneficio

def main() -> None:
  contenfermeros = 0
  # while len(listagenral) !=0
  # dependiendo de la hora el contador va a tenr un valor dif
  # if hora == tal
  #  conrenfer = k 
  #  listaenfermeros = [k]
  #   lisntaenf[i].dsiponible == true 
  #     if listagenral[0].atencion == false
  #       lisntaenf[i] =  Enfermeros(Lista_General[0])
  #       lisntaenf[i] = .asignacolor
  #     else //o sea si el paciente ya esta atenido
  #     lisntaenf[i].dsiponible == true       
  
  Pac1 = Pacientes("Juan pedro","Fernandez","43219008",[14,13,11], 2)
  Lista_General = []
  Lista_General.append(Pac1)
  Enf1 = Enfermeros(Lista_General[0])
  Enf1.asignarcolor()
  asingar_beneficio(Lista_General[0])
  
  
  

if __name__ == "__main__":
  main()
