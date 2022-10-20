"""
María José Gaytán Gil A01706616
"""

""""
Importar la biblioteca time que  contiene una serie de funciones relacionadas
con la medición del tiempo.
Utilizaremos la función time que devuelve el número de segundos transcurridos.
"""
import time

"""
================== funciones de preguntas  =====================================
"""

def compara(respuesta_usuario, respuesta_correcta, puntaje):
  """
  Función que recibe la respuesta del usuario y la compara
  con la respuesta correcta
  """
  if respuesta_usuario==respuesta_correcta:
   puntaje = puntaje + 1
  return puntaje

def calificacionfinal(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15):
  """
  Función auxiliar para manejar calificación. Comprueba la respuesta, 
  si el usario respondio lo mismo que la computadora  se le suma 1 punto 
  a su calificación
  """
  r1=compara(p1,"c",0)
  r2=compara(p2,"a",0)
  r3=compara(p3,"a",0)
  r4=compara(p4,"b",0)
  r5=compara(p5,"d",0)
  r6=compara(p6,"c",0)
  r7=compara(p7,"b",0)
  r8=compara(p8,"d",0)
  r9=compara(p9,"a",0)
  r10=compara(p10,"c",0)
  r11=compara(p11,"a",0)
  r12=compara(p12,"d",0)
  r13=compara(p13,"b",0)
  r14=compara(p14,"a",0)
  r15=compara(p15,"c",0)
  final=r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r13+r14+r15
  return final

def crea_lista (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15):
  """
  Función que guarda las respuesta del usuario en una lista
  """
  lista=[]
  lista.append(p1)
  lista.append(p2)
  lista.append(p3)
  lista.append(p4)
  lista.append(p5)
  lista.append(p6)
  lista.append(p7)
  lista.append(p8)
  lista.append(p9)
  lista.append(p10)
  lista.append(p11)
  lista.append(p12)
  lista.append(p13)
  lista.append(p14)
  lista.append(p15)
  return lista

def ciclo (respuesta_usuario, numero_pregunta):
  """
  Función que verifica que el usuario ingresa una letra válida
  """
  while respuesta_usuario != "a" and respuesta_usuario != "b" and\
  respuesta_usuario != "c"and respuesta_usuario !="d":
    print("La letra ingresada es invalida, intentalo de nuevo\n")
    respuesta_usuario=str(input(numero_pregunta))
   
"""
========  guardar las preguntas del programa ==================================
"""

prg1= "\n1.-¿Qué día inicia el mundial 2022?\na: 21 de noviembre \nb: 19\
de noviembre \nc: 20 de noviembre \nd: 22 de noviembre\n"

prg2= "\n2.-¿Qué día termina la competición?\n\na: 18 de diciembre\
\nb: 17 de diciembre\nc: 19 de diciembre\nd: 20 de diciembre\n"

prg3="\n3.-¿Cuántos grupos hay?\na: 8 grupos\nb: 6 grupos\nc: 10\
grupos\nd: 12 grupos\n"

prg4="\n4.-¿Cuántas selecciones hay por grupo?\na: 3 selecciones\
\nb: 4 selecciones\nc: 5 selecciones\nd: 6 selecciones\n"

prg5="\n5.-¿Quién es el actual campeón?\na: Inglaterra\nb: Croacia\
\nc: Argentina\nd: Francia\n"

prg6="\n6.-¿Cuál es el partido que inagurara la competición?\na: Qatar\
vs Senegal\nb: Argentina vs México\nc: Qatar vs Ecuador\nd: Ecuador vs Senegal\n"

prg7="\n7.-¿En qué estadio se disputara la final?\na: Al Bayt Stadium\
\nb: Lusail de Qatar Stadium\nc: El Al Thumama Stadium\nd: Ras Abu Aboud Stadium\n"

prg8="\n8.-¿Cuál es la selección con más mundiales?\na: Francia\
\nb: Argentina\nc: Brasil\nd: Uruguay\n"

prg9="\n9.-¿Cuál es el jugador que ha anotado más goles en los\
mundiales?\na: Miroslav Klose\nb: Pelé\nc: Maradona\nd: Messi\n"

prg10="\n10.-¿En que grupo esta México?\na: Grupo E\nb: Grupo D\
\nc: Grupo C\nd: Grupo A\n"

prg11="\n11.-¿Qué selección enfrentara México en su primer \
partido?\na: Polonia\nb: Argentina\nc: Arabia Saudita\n"

prg12="\n12.-¿Cuántas selecciones por grupo pasan a la \
siguente ronda?\na: 1 selección y la otra va a recalificación\nb: \
3 selecciones\nc: 1 selección\nd: 2 selecciones\n"

prg13="\n13.-¿En caso de empate en la final cuánto dura el\
tiempo extra?\na: 25 minutos\nb: 30 minutos\nc: 45 minutos\nd: 20 minutos\n"

prg14="\n14.-¿Cuál es el maximo de jugadores que puede llevar\
una selección?\na: 23 jugadores\nb: 22 jugadores\nc: 25 jugadores\nd:\
20 jugadores\n"

prg15="\n15.-¿Cuántos partidos se juegan durante la\
competición?\na: 58 partidos\nb: 52 partidos\nc: 64 partidos\nd:\
60 partidos\n"

"""
========  parte principal del programa ========================================
"""

# Mensaje de bienvenida 
print("Bienvenid@ a ¿Qué tán preparado estas para el mundial Qatar 2022?\n")

#Preguntarle al usuario su nombre y guardar la variable como nombre_usuario
nombre_usuario=input("¿Cuál es tu nombre?\n")

#Pregunatar si el usuario esta listo para comenzar la prueba
comenzar = str(input("\n¿Deseas comenzar con la prueba?\n sí=1  no=0\n"))

# Condición para validar la respuesta del usuario
if comenzar == "1":
  print("\nPerfecto", nombre_usuario, "comencemos con la prueba:")
  
while comenzar != "1":
  comenzar = str(input("\n¿Deseas comenzar con la prueba?\n sí=1  no=0\n"))
  
  if comenzar == "1":
    print("\nPerfecto", nombre_usuario, "comencemos con la prueba:")

# Empezar a contar los segundos con la función time()
empiezo=time.time()

# Comenzar con las preguntas 
pregunta_1=str(input(prg1))

# Llamar la función ciclo para validar la letra
ciclo(pregunta_1,prg1)

# Verificar la respuesta de usuario 
if pregunta_1=="c":
  
  # Llamar la función compara
  compara(pregunta_1,"c",0)
  
  # Imprimir el resultado 
  print("Respuesta correcta")
  
# Imprimir "resultado erroneo" 
else: 
  print("Respuesta incorrecta, la respuesta correcta es la c")
  
# Realizar pregunta 2 
pregunta_2=str(input(prg2))

# Llamar la función ciclo para validar la letra
ciclo(pregunta_2,prg2)

# Verificar la respuesta del usuario
if pregunta_2 == "a":

  # llamar la función compara
 compara(pregunta_2,"a",0)
  
  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo" 
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
  
# Realizar la pregunta 3
pregunta_3=str(input(prg3))

# Llamar la función ciclo para validar la letra 
ciclo (pregunta_3,prg3)

# Verificar respuesta del usuario
if pregunta_3 == "a":
  
  # Llamar la función compara
 compara(pregunta_3,"a",0)

  # Imprimir el resultado
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
  
# Realizar la pregunta 4
pregunta_4=str(input(prg4))

# Llamar la función ciclo para validar letra
ciclo(pregunta_4,prg4)

# Verificar respuesta del usuario
if pregunta_4 == "b":

  # llamar la función compara
 compara(pregunta_4,"b",0)

  # Imprimir el resultado
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la b")
  
# Realizar la pregunta 5
pregunta_5=str(input(prg5))

# llamar la función ciclo para validar letra 
ciclo(pregunta_5,prg5)

# Verificar la respuesta del usuario
if pregunta_5 == "d":

  # llamar la función compara
 compara(pregunta_5,"d",0)

  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la d")

# Realizar la pregunta 6
pregunta_6=str(input(prg6))

# Llamar la función ciclo para validar letra 
ciclo(pregunta_6,prg6)

# Verificar la respuesta del usuario
if pregunta_6 == "c":

  # llamar la función compara
 compara(pregunta_6,"c",0)

  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
  
# Realizar la pregunta 7
pregunta_7=str(input(prg7))

# llamar la función ciclo para validar letra
ciclo(pregunta_7,prg7)

# Verifica la respuesta del usuario
if pregunta_7 == "b":

  # Llamar la función compara 
 compara(pregunta_7,"b",0)

  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la b")
  
# Realizar la pregunta 8
pregunta_8=str(input(prg8))

# Llamar la función ciclo para validar letra
ciclo(pregunta_8,prg8)

# Verifica la respuesta del usuario
if pregunta_8 == "d":

  # Llamar la función compara
 compara(pregunta_8,"d",0)

  # Imprimir el resultado
 print("Respuesta correcta")

# Imprimir el "resultado erroneo" 
else:
 print("Respuesta incorrecta, la respuesta correcta es la d")
  
# Realizar la pregunta 9
pregunta_9=str(input(prg9))

# Llamar la función ciclo para validar letra
ciclo(pregunta_9,prg9)

# Verifica la respuesta del usuario
if pregunta_9 == "a":

  # llamar la función compara 
 compara(pregunta_9,"a",0)

  # Imprimir el resultado
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
  
# Realizar la pregunta 10
pregunta_10=str(input(prg10))

# llamar la función ciclo para validar letra
ciclo(pregunta_10,prg10)

# Verifica la respuesta del usuario
if pregunta_10 == "c":

  # llamar la función compara 
 compara(pregunta_10,"c",0)

  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
  
# Realizar la pregunta 11
pregunta_11=str(input(prg11))

# llamar la función ciclo para validar letra
ciclo(pregunta_11,prg11)

# Verifica la respuesta del usuario
if pregunta_11 == "a":

  # llamar la función compara
 compara(pregunta_11,"a",0)

  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
  
# Realizar la pregunta 12
pregunta_12=str(input(prg12))

# llamar la función ciclo para validar letra
ciclo(pregunta_12,prg12)

# Verifica la respuesta del usuario
if pregunta_12 == "d":

  # llamar la función compara 
 compara(pregunta_12,"d",0)

  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la d")
  
# Realizar la pregunta 13
pregunta_13=str(input(prg13))

# llamar la función ciclo para validar letra 
ciclo(pregunta_13,prg13)

# Verifica la respuesta del usuario
if pregunta_13 == "b":

  # llamar la función compara
 compara(pregunta_13,"b",0)

  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la b")
  
# Realizar la pregunta 14
pregunta_14=str(input(prg14))

# llamar la función ciclo para validar letra
ciclo(pregunta_14,prg14)

# Verifica la respuesta del usuario
if pregunta_14 == "a":

  # llamar la función compara 
 compara(pregunta_14,"a",0)

  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
  
# Realizar la pregunta 15
pregunta_15=str(input(prg15))

# llamar la funcion ciclo para validar letra 
ciclo(pregunta_15,prg15)

# Verifica la respuesta del usuario
if pregunta_15 == "c":

  # Llamar la función compara 
 compara(pregunta_15,"c",0)

  # Imprimir el resultado 
 print("Respuesta correcta")

# Imprimir el "resultado erroneo"
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
  
# Decirle al usuario que ha llegado al fin del programa 
fin=str(input("\nAcabaste la prueba, ¿Deseas conocer tus resultados?\
\nsí=1  no=0\n"))

# Condición para validar la respuesta del usuario
if fin == "1":
  print("\nPerfecto", nombre_usuario, "tus resultados \
son los siguentes:\n")

  # teminar de contar los segundos
  termino = time.time()
  print("\nTardaste:", termino-empiezo,"segundos")

# Ciclo para validar respuesta del usuario
while fin != "1":
  fin=str(input("\nAcabaste la prueba, ¿Deseas conocer tus\
resultados?\nsí=1  no=0\n"))
  if fin == "1":
    print("\nPerfecto", nombre_usuario, "tus resultados son \
los siguentes:\n")

    # teminar de contar los segundos
    termino = time.time()
    print("\nTardaste:", termino-empiezo,"segundos")
    
#Crear condiciones dependiendo la cantidad de puntos obtenidos por el usuario
if calificacionfinal(pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5,\
                     pregunta_6,pregunta_7,pregunta_8,pregunta_9,pregunta_10,\
                     pregunta_11,pregunta_12,pregunta_13,pregunta_14,\
                     pregunta_15) <= 5:
  print("Tu nivel rumbo a Qatar 2022 es principiante", nombre_usuario, "ya que\
de 15 puntos posibles, solo obtuviste", calificacionfinal\
        (pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5,pregunta_6\
         ,pregunta_7,pregunta_8,pregunta_9,pregunta_10,pregunta_11,pregunta_12\
         ,pregunta_13,pregunta_14,pregunta_15), "\n")
                       
elif calificacionfinal(pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5\
                       ,pregunta_6,pregunta_7,pregunta_8,pregunta_9,\
                       pregunta_10,pregunta_11,pregunta_12,pregunta_13,pregunta_14\
                       ,pregunta_15) >= 5 and calificacionfinal\
                       (pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5\
                        ,pregunta_6,pregunta_7,pregunta_8,pregunta_9,pregunta_10\
                        ,pregunta_11,pregunta_12,pregunta_13,pregunta_14,pregunta_15)\
                        <=10:
  print("Tu nivel rumbo a Qatar 2022 es profesional", nombre_usuario, "ya que de 15\
puntos posibles, obtuviste", calificacionfinal\
        (pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5,pregunta_6,pregunta_7\
         ,pregunta_8,pregunta_9,pregunta_10,pregunta_11,pregunta_12,pregunta_13\
         ,pregunta_14,pregunta_15), "\n")
                          
elif calificacionfinal(pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5\
                       ,pregunta_6,pregunta_7,pregunta_8,pregunta_9,pregunta_10\
                       ,pregunta_11,pregunta_12,pregunta_13,pregunta_14,pregunta_15) \
                       >= 10:
  print("Tu nivel rumbo a Qatar 2022 es legendario", nombre_usuario, "ya que de 15 \
puntos posibles, obtuviste", calificacionfinal\
        (pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5,pregunta_6,pregunta_7\
         ,pregunta_8,pregunta_9,pregunta_10,pregunta_11,pregunta_12,pregunta_13\
         ,pregunta_14,pregunta_15), "\n")
                         
# Preguntar al usuario si desea ver sus respuestas 
lista_respuesta=str(input("\n¿Deseas ver tus respuestas?\n sí=1  no=0\n"))
if lista_respuesta=="1":
  lista_re=crea_lista(pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5,pregunta_6\
                      ,pregunta_7,pregunta_8,pregunta_9,pregunta_10,pregunta_11,pregunta_12\
                      ,pregunta_13,pregunta_14,pregunta_15)
  print("Ok tus respuestas fueron:\n", lista_re, "\n")
  
elif lista_respuesta=="0":
  print("\nOk\n")
  
# Ciclo para validar la respuesta
while lista_respuesta != "1" and lista_respuesta!= "0":
  lista_respuesta=str(input("\n¿Deseas ver tus respuestas?\n sí=1  no=0\n"))
  if lista_respuesta=="1":
    lista_re=crea_lista(pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5\
                        ,pregunta_6,pregunta_7,pregunta_8,pregunta_9,pregunta_10\
                        ,pregunta_11,pregunta_12,pregunta_13,pregunta_14,pregunta_15)
    print("Ok tus respuestas fueron:\n", lista_re, "\n")
  elif lista_respuesta=="0":
    print("\nOk\n")
    
# Mostar un mensaje de despedida al usuario
ListaDespedida=["G","R","A","C","I","A","S"]
for x in ListaDespedida:
  print(x)
# FIN
