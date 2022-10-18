"""
María José Gaytán Gil A01706616
Mensaje de bienvenida
"""
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
"""
Crear funcinciones para reutilizar codigo
Funcion calificadora
"""
def compara(respuesta_usuario, respuesta_correcta, puntaje):
  if respuesta_usuario==respuesta_correcta:
   puntaje = puntaje + 1
  return puntaje
# Función para sumatoria de calificación 
def calificacionfinal(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15):
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
# Función que guarde las respuestas del usuario en una lista
def crea_lista (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15):
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
"""
Importar la biblioteca time que  contiene una serie de funciones relacionadas
con la medición del tiempo.
Utilizaremos la función time que devuelve el número de segundos transcurridos.
"""
import time
empiezo=time.time()
# Comenzar con las preguntas 
pregunta_1=str(input("\n1.-¿Qué día inicia el mundial 2022?\na: 21 de noviembre\
\nb: 19 de noviembre\nc: 20 de noviembre \nd: 22 de noviembre\n"))
# Ciclo para validar la letra
while pregunta_1 != "a" and pregunta_1 != "b" and pregunta_1 != "c"and pregunta_1\
      !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_1=str(input("\n1.-¿Qué día inicia el mundial 2022?\na:\
21 de noviembre\nb: 19 de noviembre\nc: 20 de noviembre \nd: 22 de\
noviembre\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_1=="c":
  compara(pregunta_1,"c",0)
  print("Respuesta correcta")
else: 
  print("Respuesta incorrecta, la respuesta correcta es la c")
# Realizar pregunta 2 
pregunta_2=str(input("\n2.-¿Qué día termina la competición?\n\na: 18 de diciembre\
\nb: 17 de diciembre\nc: 19 de diciembre\nd: 20 de diciembre\n"))
# Ciclo para validar la letra
while pregunta_2 != "a" and pregunta_2 != "b" and pregunta_2 != "c"and pregunta_2\
      !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_2=str(input("\n2.-¿Qué día termina la competición?\n\na: 18 de diciembre\
\nb: 17 de diciembre\nc: 19 de diciembre\nd: 20 de diciembre\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_2 == "a":
 compara(pregunta_2,"a",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 3
pregunta_3=str(input("\n3.-¿Cuántos grupos hay?\na: 8 grupos\nb: 6 grupos\nc: 10\
grupos\nd: 12 grupos\n"))
# Ciclo para validar la letra
while pregunta_3 != "a" and pregunta_3 != "b" and pregunta_3 != "c"and pregunta_3\
      !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_3=str(input("\n3.-¿Cuántos grupos hay?\na: 8 grupos\nb: 6 grupos\nc:\
10 grupos\nd: 12 grupos\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_3 == "a":
 compara(pregunta_3,"a",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 4
pregunta_4=str(input("\n4.-¿Cuántas selecciones hay por grupo?\na: 3 selecciones\
\nb: 4 selecciones\nc: 5 selecciones\nd: 6 selecciones\n"))
# Ciclo para validar la letra
while pregunta_4 != "a" and pregunta_4 != "b" and pregunta_4 != "c"and pregunta_4\
      !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_4=str(input("\n4.-¿Cuántas selecciones hay por grupo?\na: 3 selecciones\
\nb:4 selecciones\nc: 5 selecciones\nd: 6 selecciones\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_4 == "b":
 compara(pregunta_4,"b",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la b")
# Realizar la pregunta 5
pregunta_5=str(input("\n5.-¿Quién es el actual campeón?\na: Inglaterra\nb: Croacia\
\nc: Argentina\nd: Francia\n"))
# Ciclo para validar la letra
while pregunta_5 != "a" and pregunta_5 != "b" and pregunta_5 != "c"and pregunta_5\
      !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_5=str(input("\n5.-¿Quién es el actual campeón?\na: Inglaterra\nb: Croacia\
\nc: Argentina\nd: Francia\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_5 == "d":
 compara(pregunta_5,"d",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la d")
# Realizar la pregunta 6
pregunta_6=str(input("\n6.-¿Cuál es el partido que inagurara la competición?\na: Qatar\
vs Senegal\nb: Argentina vs México\nc: Qatar vs Ecuador\nd: Ecuador vs Senegal\n"))
# Ciclo para validar la letra
while pregunta_6 != "a" and pregunta_6 != "b" and pregunta_6 != "c"and pregunta_6 !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_6=str(input("\n6.-¿Cuál es el partido que inagurara la competición?\na:\
Qatar vs Senegal\nb: Argentina vs México\nc: Qatar vs Ecuador\nd: Ecuador vs Senegal\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_6 == "c":
 compara(pregunta_6,"c",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
# Realizar la pregunta 7
pregunta_7=str(input("\n7.-¿En qué estadio se disputara la final?\na: Al Bayt Stadium\
\nb: Lusail de Qatar Stadium\nc: El Al Thumama Stadium\nd: Ras Abu Aboud Stadium\n"))
# Ciclo para validar la letra
while pregunta_7 != "a" and pregunta_7 != "b" and pregunta_7 != "c"and pregunta_7\
      !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_7=str(input("\n7.-¿En qué estadio se disputara la final?\na: Al Bayt Stadium\
\nb: Lusail de Qatar Stadium\nc: El Al Thumama Stadium\nd: Ras Abu Aboud Stadium\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_7 == "b":
 compara(pregunta_7,"b",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la b")
# Realizar la pregunta 8
pregunta_8=str(input("\n8.-¿Cuál es la selección con más mundiales?\na: Francia\
\nb: Argentina\nc: Brasil\nd: Uruguay\n"))
# Ciclo para validar la letra
while pregunta_8 != "a" and pregunta_8 != "b" and pregunta_8 != "c"and pregunta_8\
      !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_8=str(input("\n8.-¿Cuál es la selección con más mundiales?\na: Francia\
\nb: Argentina\nc: Brasil\nd: Uruguay\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_8 == "d":
 compara(pregunta_8,"d",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la d")
# Realizar la pregunta 9
pregunta_9=str(input("\n9.-¿Cuál es el jugador que ha anotado más goles en los\
mundiales?\na: Miroslav Klose\nb: Pelé\nc: Maradona\nd: Messi\n"))
# Ciclo para validar la letra
while pregunta_9 != "a" and pregunta_9 != "b" and pregunta_9 != "c"and\
      pregunta_9 !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_9=str(input("\n9.-¿Cuál es el jugador que ha anotado más goles en los\
mundiales?\na: Miroslav Klose\nb: Pelé\nc: Maradona\nd: Messi\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_9 == "a":
 compara(pregunta_9,"a",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 10
pregunta_10=str(input("\n10.-¿En que grupo esta México?\na: Grupo E\nb: Grupo D\
\nc: Grupo C\nd: Grupo A\n"))
# Ciclo para validar la letra
while pregunta_10 != "a" and pregunta_10 != "b" and pregunta_10 != "c"and \
      pregunta_10 !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_10=str(input("\n10.-¿En que grupo esta México?\na: Grupo E\nb: \
Grupo D\nc: Grupo C\nd: Grupo A\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_10 == "c":
 compara(pregunta_10,"c",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
# Realizar la pregunta 11
pregunta_11=str(input("\n11.-¿Qué selección enfrentara México en su primer \
partido?\na: Polonia\nb: Argentina\nc: Arabia Saudita\n"))
# Ciclo para validar la letra
while pregunta_11 != "a" and pregunta_11 != "b" and pregunta_11\
      != "c":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_11=str(input("\n11.-¿Qué selección enfrentara México en su primer\
partido?\na: Polonia\nb: Argentina\nc: Arabia Saudita\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_11 == "a":
 compara(pregunta_11,"a",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 12
pregunta_12=str(input("\n12.-¿Cuántas selecciones por grupo pasan a la \
siguente ronda?\na: 1 selección y la otra va a recalificación\nb: \
3 selecciones\nc: 1 selección\nd: 2 selecciones\n"))
# Ciclo para validar la letra
while pregunta_12 != "a" and pregunta_12 != "b" and pregunta_12 != "c"and\
      pregunta_12 !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_12=str(input("\n12.-¿Cuántas selecciones por grupo pasan a la\
siguente ronda?\na: 1 selección y la otra va a recalificación\nb:\
3 selecciones\nc: 1 selección\nd: 2 selecciones\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_12 == "d":
 compara(pregunta_12,"d",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la d")
# Realizar la pregunta 13
pregunta_13=str(input("\n13.-¿En caso de empate en la final cuánto dura el\
tiempo extra?\na: 25 minutos\nb: 30 minutos\nc: 45 minutos\nd: 20 minutos\n"))
# Ciclo para validar la letra
while pregunta_13 != "a" and pregunta_13 != "b" and pregunta_13 != "c"and\
      pregunta_13 !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_13=str(input("\n13.-¿En caso de empate en la final cuánto dura el\
tiempo extra?\na: 25 minutos\nb: 30 minutos\nc: 45 minutos\nd: 20 minutos\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_13 == "b":
 compara(pregunta_13,"b",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la b")
# Realizar la pregunta 14
pregunta_14=str(input("\n14.-¿Cuál es el maximo de jugadores que puede llevar\
una selección?\na: 23 jugadores\nb: 22 jugadores\nc: 25 jugadores\nd:\
20 jugadores\n"))
# Ciclo para validar la letra
while pregunta_14 != "a" and pregunta_14 != "b" and pregunta_14 != "c"and \
      pregunta_14 !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_14=str(input("\n14.-¿Cuál es el maximo de jugadores que puede\
llevar una selección?\na: 23 jugadores\nb: 22 jugadores\nc: 25 jugadores\nd:\
20 jugadores\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_14 == "a":
 compara(pregunta_14,"a",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 15
pregunta_15=str(input("\n15.-¿Cuántos partidos se juegan durante la\
competición?\na: 58 partidos\nb: 52 partidos\nc: 64 partidos\nd:\
60 partidos\n"))
# Ciclo para validar la letra
while pregunta_15 != "a" and pregunta_15 != "b" and pregunta_15 != "c"\
      and pregunta_15 !="d":
  print("La letra ingresada es invalida, intentalo de nuevo\n")
  pregunta_15=str(input("\n15.-¿Cuántos partidos se juegan durante la \
competición?\na: 58 partidos\nb: 52 partidos\nc: 64 partidos\nd:\
60 partidos\n"))
"""
Condición para validar si la respuesta del usuario fue correcta
si asi lo es sumarle un punto con la función compara
"""
if pregunta_15 == "c":
 compara(pregunta_15,"c",0)
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
# Decirle al usuario que ha llegado al fin del programa 
fin=str(input("\nAcabaste la prueba, ¿Deseas conocer tus resultados?\
\nsí=1  no=0\n"))
# Condición para validar la respuesta del usuario
if fin == "1":
  print("\nPerfecto", nombre_usuario, "tus resultados \
son los siguentes:\n")
  termino = time.time()
  print("\nTardaste:", termino-empiezo,"segundos")
while fin != "1":
  fin=str(input("\nAcabaste la prueba, ¿Deseas conocer tus\
resultados?\nsí=1  no=0\n"))
  if fin == "1":
    print("\nPerfecto", nombre_usuario, "tus resultados son \
los siguentes:\n")
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
