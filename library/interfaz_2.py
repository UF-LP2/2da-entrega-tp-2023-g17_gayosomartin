import tkinter as tk
from tkinter import font
import time
from library.Clases import Enfermeros
from library.Clases import Hospital
from library.Funciones import enfermerosdisp
from library.Funciones import asignar_a_Cola
from library.Funciones import LecturaArch
from library.Funciones import atender
from library.Funciones import Calcular_Tiempo

# Le ponemos segun el color del paciente como se deberia pintar el cuadrado
colores = {"rojo": "#FF0000", "naranja": "#FFA500", "amarillo": "#FFFF00", "verde": "#17E60C", "azul": "#1E75FF"}

root = tk.Tk()

root.title("Simulación de Triage")


canvas = tk.Canvas(root, width=1000, height=600)
canvas.pack()

#Creamos la interfaaz para ver pacientes atendidos
def Mostrar_Paciente(pacientes,c1,c2,c3,c4,k1,contenfer):
    
    root = tk.Tk()
    root.geometry("800x600")  # tamaño de la ventana
    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=True)
    global sala_espera, conslutorio1, conssultorio2, consultorio3, consultorio4,pacientern,otrosp
    root.wm_state('zoomed')
    

    # tamaño y posición de la sala de espera
    sala_de_espera_x1 = 50
    sala_de_espera_y1 = 50
    sala_de_espera_x2 = 750
    sala_de_espera_y2 = 550
    sala_espera =canvas.create_rectangle(sala_de_espera_x1, sala_de_espera_y1, sala_de_espera_x2, sala_de_espera_y2, outline="black", width=2)

    
    rojo_Nar_pacientes = [paciente for paciente in pacientes if paciente.color in ["rojo", "naranja"]]
    otros_pacientes = [paciente for paciente in pacientes if paciente.color in ["amarillo", "verde", "azul"]]
    
    canvas.create_text((sala_de_espera_x1 + sala_de_espera_x2) / 2, sala_de_espera_y1 + 20, text="Cola Prioridad Principal", font=("Arial", 14), anchor=tk.CENTER)
    for i, paciente in enumerate(rojo_Nar_pacientes):
        x_offset = (i % 10) * 70  #  espacio horizontal entre los grupos(rojo/naranjas y los otros)
        y_offset = (i // 10) * 50 +50  # espacio vertical entre los grupos
        pacientern =canvas.create_rectangle(sala_de_espera_x1 + 10 + x_offset, sala_de_espera_y1 + 10 + y_offset, sala_de_espera_x1 + 50 + x_offset, sala_de_espera_y1 + 50 + y_offset, fill=colores[paciente.color], width=0)
        canvas.create_text(sala_de_espera_x1 + 30 + x_offset, sala_de_espera_y1 + 30 + y_offset, text=f"{paciente.Nombre}", anchor=tk.CENTER)
        
    canvas.create_text((sala_de_espera_x1 + sala_de_espera_x2) / 2, sala_de_espera_y1 + 220, text="Cola Prioridad Secundaria", font=("Arial", 14), anchor=tk.CENTER)

    # pacientes amarillos, verdes y azules
    for i, paciente in enumerate(otros_pacientes):
        x_offset = (i % 10) * 70  
        y_offset = (i // 10) * 60 + 50
        otrosp =canvas.create_rectangle(sala_de_espera_x1 + 10 + x_offset, sala_de_espera_y1 + 200 + y_offset, sala_de_espera_x1 + 50 + x_offset, sala_de_espera_y1 + 240 + y_offset, fill=colores[paciente.color], width=0)
        canvas.create_text(sala_de_espera_x1 + 30 + x_offset, sala_de_espera_y1 + 220 + y_offset, text=f"{paciente.Nombre}", anchor=tk.CENTER)
        
 
    #consultorio 1
    conslutorio1 = canvas.create_rectangle(800,50,1150,400)
    canvas.create_text(975,60, text=f"Consultorio 1")
    canvas.create_text(975,200, text=f"La cantidad de pacientes atendidos en este consultorio fue de: {c1}")

    conssultorio2 =canvas.create_rectangle(1150,50,1500,400)
    canvas.create_text(1325,60, text=f"Consultorio 2")
    canvas.create_text(1325,200, text=f"La cantidad de pacientes atendidos en este consultorio fue de: {c2}")

    consultorio3 = canvas.create_rectangle(800,350,1150,750)
    canvas.create_text(975,420, text=f"Consultorio 3")
    canvas.create_text(975,550, text=f"La cantidad de pacientes atendidos en este consultorio fue de: {c3}")

    consultorio4 =canvas.create_rectangle(1150,350,1500,750)
    canvas.create_text(1325,420, text=f"Consultorio 4")
    canvas.create_text(1325,550, text=f"La cantidad de pacientes atendidos en este consultorio fue de: {c4}")
    font_del_Texto1 = font.Font(family= "Arial",size=20)
    canvas.create_text(150,650, text=f" La cantidad de muertos fue: {k1}",font = font_del_Texto1)
    Hora_Actual = time.localtime()
    font_del_Texto2 = font.Font(family= "Arial",size=30)
    canvas.create_text(300,730, text=f" La hora actual es : {Hora_Actual.tm_hour} :{Hora_Actual.tm_min}, por lo que la cantidad de medicos es de {contenfer}",font = font_del_Texto2)



    

       
def funcion_antencio_pacientes():
   
  Hospi = Hospital()
  #Leemos el archivo que tiene a los pacientes y los ponemos en la lista general del Hopital
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

  cont1 =cont2 = cont3 = cont4 = Muertos= 0  #cantidad de personas antendias por este primer consultorio

  
  #Nos fijamos segun la hora cuantos medicos disponibles hay
  contEnfermeros= enfermerosdisp(Hospi)
  
  #Vamos a estar en este while asignandole el color a los pacientes hasta que no queden mas en la lista
  while (len(Hospi.listaPacientes) != 0) :
    for i in range(contEnfermeros):
      print(Hospi.listaEnfermeros[i].name)
      print("--------------------------------------------------------------------------------------")
      #Verificamos que el Enf 1 este disponible y que el paciente [0], necesite ser atendido
      if Hospi.listaEnfermeros[i].Disponible == True:  
        if len(Hospi.listaPacientes) > 0 and Hospi.listaPacientes[0].atencion == False:
          print("Se le asigna color al paciente ",Hospi.listaPacientes[0].Nombre,Hospi.listaPacientes[0].Apellido)
          Hospi.listaEnfermeros[i].asignarcolor(Hospi.listaPacientes[0])
          asignar_a_Cola(Hospi.listaPacientes[0],Hospi)
            
            #Pasamos al siguiente enfermero de la lista asi el mismo enfermero no tiene que atender a todos los paciente
            # Es como si tuviera un descnaso entre paciente y paciente  
      if len(Hospi.listaPacientes) > 1 and i+1 < len(Hospi.listaEnfermeros) and Hospi.listaEnfermeros[i+1].Disponible == True:
       
        # y revisamos posicion [1] ya que el otro ya fue atendido
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
    
   
    #Calculamos cuanto tiempo les queda a los pacientes
    Muertos = Muertos + Calcular_Tiempo(Hospi)
    #Consultorio 1
    cont1 = cont1 + atender(Hospi) # atender vendria a ser como un consultorio
    #Consultorio 2
    #Los cont son para saber la cantidad de gente que se atendio en cada consultorio
    cont2 = cont2 + atender(Hospi)

    
    
  
    
    # este while esta hecho para cuando ya todos los pacientes tiene un color asignado por lo cual ya no estan
    # en la lista general pero todavia quedan pacientes sin atender en las colas

  while(len(Hospi.colaSecundario)!= 0 or len(Hospi.colaPrincipal)!= 0 ):
    Muertos = Muertos + Calcular_Tiempo(Hospi)
    #Consultorio 3
    
    cont3 = cont3 + atender(Hospi)
    #Consutorio 4
    cont4 = cont4 + atender(Hospi)

  
  root.state('iconic')  # Para Minimiza la ventana principal
  Mostrar_Paciente(Hospi.colaAux,cont1,cont2,cont3,cont4,Muertos,contEnfermeros) 
  



   



iniciar_button = tk.Button(root, text="Iniciar Simulación", command=funcion_antencio_pacientes)
iniciar_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


root.mainloop()








