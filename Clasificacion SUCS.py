#Clasificacion SUCS por ASTM D2487

#**********************DATOS**********************

# % de gruesos = G + S, debe ser >=0 y <= 100%
# Nota: cuando %F es > 50 poner cualquier valor en Cu y Cc p.ej Cu=0 , Cc=0
Pgrava = 28
Parena = 70
Cu = 1
Cc = 2
LL = 60
IP = 0


#**********************CALCULOS**********************
#Calcula automático el % de finos
Pgruesos = Pgrava + Parena
Pfinos = 100 - Pgruesos

if Pgruesos > 50 :
	TipoSuelo = "Grueso"
	
elif Pgruesos <= 50 :
	
    TipoSuelo = "Fino"
else:
	print("Error")



#********OBTENER EL TIPO DE FINO********************************
#(también sirve para suelos gruesos con 5 <= Pfinos <= 12 

#Obtener el valor de la linea A
if LL <= 25.5 :
        LineaA = 4

elif LL > 25.5 :
        LineaA = 0.73 * (LL - 20)

else:
        print("Error")


#Nombre del fino
if LL < 50 and IP >= LineaA and 4 <= IP <= 7:
        SimboloDeFino = "CL-ML"
        NombreDelFino = "Arcilla Limosa"

elif LL < 50 and IP >= LineaA and IP > 7 :
        SimboloDeFino = "CL"
        NombreDelFino = "Arcilla Ligera"

elif LL < 50 and IP < LineaA :
    SimboloDeFino = "ML"
    NombreDelFino = "Limo"       

elif LL >= 50 and IP >= LineaA :
        SimboloDeFino = "CH"
        NombreDelFino = "Arcilla Gruesa"

elif LL >= 50 and IP < LineaA  :
    SimboloDeFino = "MH"
    NombreDelFino = "Limo Elástico"  

else:
     print("Error")



#APELLIDO del fino
    
if Pgruesos < 15:
    ApellidoDelFino = " " 

elif 15 <= Pgruesos < 30 and Parena >= Pgrava:
    ApellidoDelFino = " con arena"   

elif 15 <= Pgruesos < 30 and Parena < Pgrava:
    ApellidoDelFino = " con grava"   

elif Pgruesos >= 30 and Parena >= Pgrava and Pgrava < 15:
    ApellidoDelFino = " arenoso(a)" 

elif Pgruesos >= 30 and Parena >= Pgrava and Pgrava >= 15:
    ApellidoDelFino = " arenoso(a) con grava"   

elif Pgruesos >= 30 and Parena < Pgrava and Pgrava < 15:
    ApellidoDelFino = " gravoso(a)"   

elif Pgruesos >= 30 and Parena < Pgrava and Pgrava >= 15:
    ApellidoDelFino = " gravoso(a) con arena"  

else:
    print("Error")




#*********CLASIFICACIÓN SUELOS GRUESOS***********************************
if Pgrava > Parena :
    TipoSuelo = "Grueso"

    if Pfinos < 5 :
        TipoSueloGrueso = "Pfinos < 5"

        if Cu >= 4 and 1 <= Cc <= 3 :
            SimboloDeGrupo = "GW"

            if Parena < 15 :
                NombreDelGrupo = "Grava bien graduada"
                
            elif Parena >= 15 :
                NombreDelGrupo = "Grava bien graduada con arena"

            else:
                print("Error")
        

            
        elif Cu < 4 or Cc < 1 or Cc > 3  :
            SimboloDeGrupo = "GP"

            if Parena < 15 :
                NombreDelGrupo = "Grava mal graduada"
                
            elif Parena >= 15 :
                NombreDelGrupo = "Grava mal graduada con arena"

            else:
                print("Error")

        else:
            print("Error")
     

    elif Pfinos >= 5 and Pfinos <= 12 :
        TipoSueloGrueso = "Pfinos >= 5 and Pfinos <= 12"

        if (Cu >= 4 and 1 <= Cc <= 3) and (SimboloDeFino == "ML" or SimboloDeFino == "MH") :
            SimboloDeGrupo = "GW-GM"

            if Parena < 15 :
                NombreDelGrupo = "Grava bien graduada con limo"
                
            elif Parena >= 15 :
                NombreDelGrupo = "Grava bien graduada con limo y arena"

            else:
                print("Error")
 
        elif (Cu >= 4 and 1 <= Cc <= 3) and (SimboloDeFino == "CL" or SimboloDeFino == "CH" or SimboloDeFino == "CL-ML") :
            SimboloDeGrupo = "GW-GC"

            if Parena < 15 :
                NombreDelGrupo = "Grava bien graduada con arcilla"
                
            elif Parena >= 15 :
                NombreDelGrupo = "Grava bien graduada con arcilla y arena"

            else:
                print("Error")
 
 #******
        elif (Cu < 4 or Cc < 1 or Cc > 3 ) and (SimboloDeFino == "ML" or SimboloDeFino == "MH") :
            SimboloDeGrupo = "GP-GM"

            if Parena < 15 :
                NombreDelGrupo = "Grava mal graduada con limo"
                
            elif Parena >= 15 :
                NombreDelGrupo = "Grava mal graduada con limo y arena"

            else:
                print("Error")
 
        elif (Cu < 4 or Cc < 1 or Cc > 3 ) and (SimboloDeFino == "CL" or SimboloDeFino == "CH" or SimboloDeFino == "CL-ML") :
            SimboloDeGrupo = "GP-GC"

            if Parena < 15 :
                NombreDelGrupo = "Grava mal graduada con arcilla"
                
            elif Parena >= 15 :
                NombreDelGrupo = "Grava mal graduada con arcilla y arena"

            else:
                print("Error")


    elif Pfinos > 12 :
        if SimboloDeFino == "ML" or SimboloDeFino == "MH":
            SimboloDeGrupo = "GM"

            if Parena < 15 :
                NombreDelGrupo = "Grava limosa"
                
            elif Parena >= 15 :
                NombreDelGrupo = "Grava limosa con arena"

            else:
                print("Error")


        elif SimboloDeFino == "CL" or SimboloDeFino == "CH":
            SimboloDeGrupo = "GC"

            if Parena < 15 :
                NombreDelGrupo = "Grava arcillosa"
                
            elif Parena >= 15 :
                NombreDelGrupo = "Grava arcillosa con arena"

            else:
                print("Error")


        elif SimboloDeFino == "CL-ML":
            SimboloDeGrupo = "GC-GM"

            if Parena < 15 :
                NombreDelGrupo = "Grava limoarcillosa"
                
            elif Parena >= 15 :
                NombreDelGrupo = "Grava limoarcillosa con arena"

            else:
                print("Error")

        else:
            print("error")
    else:
        print("Error")



#******** Arenas ***************
if  Parena >= Pgrava :
    TipoSuelo = "Grueso"

    if Pfinos < 5 :
        TipoSueloGrueso = "Pfinos < 5"

        if Cu >= 6 and 1 <= Cc <= 3 :
            SimboloDeGrupo = "SW"

            if Pgrava < 15 :
                NombreDelGrupo = "Arena bien graduada"
                
            elif Pgrava >= 15 :
                NombreDelGrupo = "Arena bien graduada con grava"

            else:
                print("Error")
        

            
        elif Cu < 6 or Cc < 1 or Cc > 3  :
            SimboloDeGrupo = "SP"

            if Pgrava < 15 :
                NombreDelGrupo = "Arena mal graduada"
                
            elif Pgrava >= 15 :
                NombreDelGrupo = "Arena mal graduada con grava"

            else:
                print("Error")

        else:
            print("Error")
     

    elif Pfinos >= 5 and Pfinos <= 12 :


        if (Cu >= 6 and 1 <= Cc <= 3) and (SimboloDeFino == "ML" or SimboloDeFino == "MH") :
            SimboloDeGrupo = "SW-SM"

            if Pgrava < 15 :
                NombreDelGrupo = "Arena bien graduada con limo"
                
            elif Pgrava >= 15 :
                NombreDelGrupo = "Arena bien graduada con limo y grava"

            else:
                print("Error")
 
        elif (Cu >= 6 and 1 <= Cc <= 3) and (SimboloDeFino == "CL" or SimboloDeFino == "CH" or SimboloDeFino == "CL-ML") :
            SimboloDeGrupo = "SW-SC"

            if Pgrava < 15 :
                NombreDelGrupo = "Arena bien graduada con arcilla"
                
            elif Pgrava >= 15 :
                NombreDelGrupo = "Arena bien graduada con arcilla y grava"

            else:
                print("Error")
 
#******
        elif (Cu < 6 or Cc < 1 or Cc > 3 ) and (SimboloDeFino == "ML" or SimboloDeFino == "MH") :
            SimboloDeGrupo = "SP-SM"

            if Pgrava < 15 :
                NombreDelGrupo = "Arena mal graduada con limo"
                
            elif Pgrava >= 15 :
                NombreDelGrupo = "Arena mal graduada con limo y grava"

            else:
                print("Error")
 
        elif (Cu < 6 or Cc < 1 or Cc > 3 ) and (SimboloDeFino == "CL" or SimboloDeFino == "CH" or SimboloDeFino == "CL-ML") :
            SimboloDeGrupo = "SP-SC"

            if Pgrava < 15 :
                NombreDelGrupo = "Arena mal graduada con arcilla"
                
            elif Pgrava >= 15 :
                NombreDelGrupo = "Arena mal graduada con arcilla y grava"

            else:
                print("Error")


    elif Pfinos > 12 :
        if SimboloDeFino == "ML" or SimboloDeFino == "MH":
            SimboloDeGrupo = "SM"

            if Pgrava < 15 :
                NombreDelGrupo = "Arena limosa"
                
            elif Pgrava >= 15 :
                NombreDelGrupo = "Arena limosa con grava"

            else:
                print("Error")


        elif SimboloDeFino == "CL" or SimboloDeFino == "CH":
            SimboloDeGrupo = "SC"

            if Pgrava < 15 :
                NombreDelGrupo = "Arena arcillosa"
                
            elif Pgrava >= 15 :
                NombreDelGrupo = "Arena arcillosa con grava"

            else:
                print("Error")


        elif SimboloDeFino =="CL-ML":
            SimboloDeGrupo = "SC-SM"

            if Pgrava < 15 :
                NombreDelGrupo = "Arena limoarcillosa"
                
            elif Pgrava >= 15 :
                NombreDelGrupo = "Arena limoarcillosa con grava"

            else:
                print("Error")

        else:
            print("error")




if Pgruesos > Pfinos :
	TipoSuelo = "Grueso"
 

elif Pfinos >= 50 :
    TipoSuelo = "Fino"
    SimboloDeGrupo = SimboloDeFino
    NombreDelGrupo = NombreDelFino + ApellidoDelFino

else:
    print("Error")



#**********RESULTADOS***********************************************

print("El tipo de suelo es: " + TipoSuelo)   
print("El simbolo de grupo es: " + SimboloDeGrupo)
print("El nombre de grupo es: " + NombreDelGrupo)    

print("*******************************************************************") 
print("Programado por: Nicolás Jiménez") 