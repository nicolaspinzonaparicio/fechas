class Dia:
  
  # una tupla
  DIAS_MES = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
  
  # contrusctor
  def __init__(self, d, m, a):
    self.__dia = d
    self.__mes = m
    self.__anio = a
  
  def esBisiesto(self):
    # nada por aca 
    pass
  
  def sonIguales(self, otroDia):
    # nada por aca
    pass
    
  def esMayor(self, otroDia):
    #ESTE ES UN COMENTARIO
    """
    ESTE ES OTRO COMENTARIO
    """
    pass
  
  def toString(self):
      return str(self.__dia) + "/"+ str(self.__mes) + "/" + str(self.__anio)
  
  # metodo set y get
 
  
  def getDia(self):
    return self.__dia
  
  def setDia(self, d):
    self.__dia = d

    # Holi my dog
    
    
# esto seria el main
print("Calculdora de fechas bienvenido")
d = Dia(11,11,2017)
print("el dia " + d.toString())



#Comparar fechas

fechaD=input("Ingrese la fecha de entrega (ddmmyyyy): ")
fechaD=fechaD.strip()
Largofecha=len(fechaD)
if(Largofecha>0 and Largofecha==8):
	ahora = time.strftime("%d-%m-%Y")
	dtfechaD=datetime.strptime(fechaD, "%d%m%Y")
	fechaFinal=dtfechaD.strftime("%d-%m-%Y")
	print(fechaFinal)
	if(fechaFinal>=ahora):
		print("si")
	else:
		print("no")
else:
	print("error: ingrese bien la fecha")
