# María José Gaytán Gil A01706616
# Mensaje de bienvenida 
print("Bienvenid@ a ¿Qué tán preparado estas para el mundial Qatar 2022?\n")
# Preguntarle al usuario su nombre y guardar la variable como nombre_usuario
nombre_usuario=input("¿Cuál es tu nombre?\n")
# Pregunatar si el usuario esta listo para comenzar la prueba
comenzar = int(input("\n¿Deseas comenzar con la prueba?\n sí=1  no=0\n"))
# Condición para validar la respuesta del usuario
if comenzar ==1:
  print("\nPerfecto", nombre_usuario, "comencemos con la prueba:")
while comenzar ==0:
  comenzar = int(input("\n¿Deseas comenzar con la prueba?\n sí=1  no=0\n"))
  if comenzar ==1:
    print("\nPerfecto", nombre_usuario, "comencemos con la prueba:")
# Definir variable contadora
cp=0
# Definir a, b, c y d 
a=0
b=0
c=0
d=0
# Comenzar con la pregunta 1
pregunta_1=str(input("\n1.-¿Qué día inicia el mundial 2022?\n\na: 21 de noviembre\nb: 19 de noviembre\nc: 20 de noviembre \nd: 22 de noviembre\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_1 == "c":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
# Realizar la pregunta 2
pregunta_2=str(input("\n2.-¿Qué día termina la competición?\n\na: 18 de diciembre\nb: 17 de diciembre\nc: 19 de diciembre\nd: 20 de diciembre\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_2 == "a":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 3
pregunta_3=str(input("\n3.-¿Cuántos grupos hay?\na: 8 grupos\nb: 6 grupos\nc: 10 grupos\nd: 12 grupos\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_3 == "a":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 4
pregunta_4=str(input("\n4.-¿Cuántas selecciones hay por grupo?\na: 3 selecciones\nb: 4 selecciones\nc: 5 selecciones\nd: 6 selecciones\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_4 == "b":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la b")
# Realizar la pregunta 5
pregunta_5=str(input("\n5.-¿Quién es el actual campeón?\na: Inglaterra\nb: Croacia\nc: Argentina\nd: Francia\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_5 == "d":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la d")
# Realizar la pregunta 6
pregunta_6=str(input("\n6.-¿Cuál es el partido que inagurara la competición?\na: Qatar vs Senegal\nb: Argentina vs México\nc: Qatar vs Ecuador\nd: Ecuador vs Senegal\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_6 == "c":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
# Realizar la pregunta 7
pregunta_7=str(input("\n7.-¿En qué estadio se disputara la final?\na: Al Bayt Stadium\nb: Lusail de Qatar Stadium\nc: El Al Thumama Stadium\nd: Ras Abu Aboud Stadium\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_7 == "b":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la b")
# Realizar la pregunta 8
pregunta_8=str(input("\n8.-¿Cuál es la selección con más mundiales?\na: Francia\nb: Argentina\nc: Brasil\nd: Uruguay\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_8 == "d":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la d")
# Realizar la pregunta 9
pregunta_9=str(input("\n9.-¿Cuál es el jugador que ha anotado más goles en los mundiales?\na: Miroslav Klose\nb: Pelé\nc: Maradona\nd: Messi\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_9 == "a":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 10
pregunta_10=str(input("\n10.-¿En que grupo esta México?\na: Grupo E\nb: Grupo D\nc: Grupo C\nd: Grupo A\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_10 == "c":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
# Realizar la pregunta 11
pregunta_11=str(input("\n11.-¿Qué selección enfrentara México en su primer partido?\na: Polonia\nb: Argentina\nc: Arabia Saudita\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_11 == "a":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 12
pregunta_12=str(input("\n12.-¿Cuántas selecciones por grupo pasan a la siguente ronda?\na: 1 selección y la otra va a recalificación\nb: 3 selecciones\nc: 1 selección\nd: 2 selecciones\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_12 == "d":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la d")
# Realizar la pregunta 13
pregunta_13=str(input("\n13.-¿En caso de empate en la final cuánto dura el tiempo extra?\na: 25 minutos\nb: 30 minutos\nc: 45 minutos\nd: 20 minutos\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_13 == "b":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la b")
# Realizar la pregunta 14
pregunta_14=str(input("\n14.-¿¿Cuál es el maximo de jugadores que puede llevar una selección??\na: 23 jugadores\nb: 22 jugadores\nc: 25 jugadores\nd: 20 jugadores\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_14 == "a":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la a")
# Realizar la pregunta 15
pregunta_15=str(input("\n15.-¿Cuántos partidos se juegan durante la competición?\na: 58 partidos\nb: 52 partidos\nc: 64 partidos\nd: 60 partidos\n"))
# Condición para validar si la respuesta del usuario fue correcta y si asi lo es sumarle un punto
if pregunta_15 == "c":
 cp=cp+1
 print("Respuesta correcta")
else:
 print("Respuesta incorrecta, la respuesta correcta es la c")
# Decirle al usuario que ha llegado al fin del programa que si desea saber sus resultados 
fin=int(input("\nAcabaste la prueba, ¿Deseas conocer tus resultados?\nsí=1  no=0\n"))
# Condición para validar la respuesta del usuario
if fin ==1:
  print("\nPerfecto", nombre_usuario, "tus resultados son los siguentes:\n")
while fin ==0:
  fin=int(input("\nAcabaste la prueba, ¿Deseas conocer tus resultados?\nsí=1  no=0\n"))
  if fin ==1:
    print("\nPerfecto", nombre_usuario, "tus resultados son los siguentes:\n")
#Crear condiciones dependiendo la cantidad de puntos obtenidos por el usuario
if cp <= 5:
  print("Tu nivel rumbo a Qatar 2022 es principiante", nombre_usuario, "ya que de 15 puntos posibles, solo obtuviste", cp, "\n")
elif cp >= 5 and cp <=10:
  print("Tu nivel rumbo a Qatar 2022 es profesional", nombre_usuario, "ya que de 15 puntos posibles, obtuviste", cp, "\n")
elif cp >= 10:
  print("Tu nivel rumbo a Qatar 2022 es legendario", nombre_usuario, "ya que de 15 puntos posibles, obtuviste", cp, "\n")
# Mostar un mensaje de despedida al usuario
ListaDespedida=["G","R","A","C","I","A","S"]
for x in ListaDespedida:
  print(x)
# FIN