# Proyecto-TC1028

Este proyecto es creado por María José Gaytán Gil A01706616, de la clase TC 1028

Espero les guste :)

# El torneo más prestigioso del mundo

"En la Copa Mundial Masculina de la FIFA, que se celebra cada cuatro años, 32 naciones compiten entre sí por el título. Los distintos clasificatorios continentales dan paso a una fase final de lo más emocionante, que congrega a los aficionados en torno a la pasión y el amor por el deporte rey." (FIFA, 2022) 

Este año se jugara la edición número 22 en Qatar, por ello la finalidad de este programa es determinar que tan preparado estás para ver esta copa del mundo mediante series de preguntas que determinaran en que nivel te encuentras (todas las respuestas a las preguntas son sacadas del sitio oficial de la FIFA), al final el programa arrojara tu resultado en 3 distintos niveles en los que el programa puede posicionarte en el más bajo: principiante (0-5 respuestas correctas), el intermedio: profesional (6-10 respuestas correctas), y el más alto: legendario (11-15 respuestas correctas).

Asimismo para la realización de este proyecto se ocupara la biblioteca time, la cual es una biblioteca con funciones relacionadas al tiempo, ya que haremos uso de la funcion time() la cual cuenta los segundos transcurridos de una operación, en este caso sera los segundos transcurridos desde que el usuario comience con el cuestionario hasta que lo termine. 

# Pseudocódigo

Mostrar mensaje de bienvenida al usuario

nombre_usuario: ¿Como te llamas?

Crear funciones para reutilizar codigo

Función calificadora

def compara(respuesta_usuario, respuesta_correcta, puntaje):
   
  if respuesta_usuario==respuesta_correcta:
  
  puntaje = puntaje + 1
  
  return puntaje

Función para sumatoria de calificación 

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
  
Función que guarde las respuestas del usuario en una lista

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

Importar api tiempo y contar el tiempo

import time

empiezo=time.time()

Preguntar al usuario si esta listo para empezar

comenzar: ¿Estas listo para comenzar? (sí=1, no=0)

Si comenzar es == 1:

  comenzar prueba
  
Si comenzar es == 0:

  volver a mostar la pregunta
  
Empezar con las preguntas

pregunta_1: ¿Qué día inicia el mundial 2022?

Opciones:

a: 21 de noviembre 

b: 19 de noviembre 

c: 20 de noviembre (correcta)

d: 22 de noviembre 

validar la respuesta con un ciclo 

Si pregunta_1 == c:

mandar llamar la función compara () e imprimir respuesta correcta

Sino mostar incorrecto 

pregunta_2: ¿Qué día termina la competición?

Opciones:

a: 18 de diciembre (correcta)

b: 17 de diciembre 

c: 19 de diciembre 

d: 20 de diciembre

validar la respuesta con un ciclo 

Si pregunta_2 == a:

mandar llamar la función compara () e imprimir respuesta correcta

Sino mostar incorrecto 
  
pregunta_3: ¿Cuántos grupos hay?

Opciones:

a: 8 grupos (correcta)

b: 6 grupos

c: 10 grupos

d: 12 grupos

validar la respuesta con un ciclo 

Si pregunta_3 == a:
  
mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto
  
pregunta_4: ¿Cuántas selecciones hay por grupo?

Opciones:

a: 3 selecciones

b: 4 selecciones (correcta)

c: 5 selecciones

d: 6 selecciones

validar la respuesta con un ciclo 

Si pregunta_4 == b:
  
 mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto
  
pregunta_5: ¿Quién es el actual campeón de la competición?

Opciones:

a: Inglaterra

b: Croacia

c: argentina 

d: Francia (correcta)

validar la respuesta con un ciclo 

Si pregunta_5 == d:
  
  mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto

pregunta_6: ¿Cuál es el partido que inagurara la competición?

Opciones:

a: Qatar vs Senegal

b: Argentina vs México

c: Qatar vs Ecuador (correcta)

d: Ecuador vs Senegal

validar la respuesta con un ciclo 

Si pregunta_6 == c:
  
 mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto

pregunta_7: ¿En qué estadio se disputara la final?

Opciones:

a: Al Bayt Stadium

b: Lusail de Qatar Stadium (correcta)

c: El Al Thumama Stadium

d: Ras Abu Aboud Stadium

validar la respuesta con un ciclo 

Si pregunta_7 == b:
  
 mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto

pregunta_8: ¿Cuál es la selección con más mundiales?

Opciones:

a: Francia

b: Argentina 

c: Brasil

d: Uruguay (correcta)

validar la respuesta con un ciclo 

Si pregunta_8 == d:
  
  mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto
  
pregunta_9: ¿Cuál es el jugador que ha anotado más goles en los mundiales?

Opciones:

a: Miroslav Klose (correcta)

b: Pelé

c: Maradona 

d: Lionel Messi

validar la respuesta con un ciclo 

Si pregunta_9 == a:
  
mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto

pregunta_10: ¿En que grupo esta México?

Opciones:

a: Grupo E

b: Grupo D

c: Grupo C (correcta)

d: Grupo A

validar la respuesta con un ciclo 

Si pregunta_10 == c:
  
 mandar llamar la función compara () e imprimir respuesta correcta
 
Sino mostrar incorrecto

pregunta_11: ¿Qué selección enfrentara México en su primer partido?

Opciones:

a: Polonia (correcto)

b: Argentina

c: Arabia Saudita 

validar la respuesta con un ciclo 

Si pregunta_11 == a:
  
 mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto

pregunta_12: ¿Cuántas selecciones por grupo pasan a la siguente ronda?

Opciones:

a: 1 selección y la otra va a recalificación

b: 3 selecciones 

c: 1 selección

d: 2 selecciones (correcto)

validar la respuesta con un ciclo 

Si pregunta_12 == d:
  
 mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto

pregunta_13: ¿En caso de empate en la final cuánto dura el tiempo extra?

Opciones:

a: 25 minutos

b: 30 minutos (correcta)

c: 45 minutos 

d: 20 minutos 

validar la respuesta con un ciclo 

Si pregunta_13 == b:
  
mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto

pregunta_14: ¿Cuál es el maximo de jugadores que puede llevar una selección?

Opciones:

a: 23 jugadores (correcta)

b: 22 jugadores 

c: 25 jugadores 

d: 20 jugadores 

validar la respuesta con un ciclo 

Si pregunta_14 == a:
  
 mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto

pregunta_15: ¿Cuántos partidos se juegan durante la competición?

Opciones:

a: 58 partidos

b: 52 partidos 

c: 64 partidos (correcta)

d: 60 partidos 

validar la respuesta con un ciclo 

Si pregunta_15 == c:
  
 mandar llamar la función compara () e imprimir respuesta correcta

Sino mostrar incorrecto
  
res: preguntar al nombre_usuario si desea conocer su puntuación (si=1, no=0)

Si res es == 1:

  detener el tiempo y mostrar al usuario cuanto tardo en contestarlo 
  
  mostrar resultados: 
  
   si contar_puntos <= 5:
  
   mostar al usurio el total de puntos y decirle que es un nivel principiante.
  
   si contar_puntos <= 10:
  
   mostar al usuario el total de puntos y decirle que es un nivel profesional.
  
   si contar_puntos <= 15:
   
   mostar al usurio el total de puntos y decirle que es un nivel legendario.
  
Si res es == 0:

  volver a mostar la pregunta
  
Preguntar al usuario si desea ver sus respuestas

si el usuario lo desea mandar llamar la funcion crea_lista y mostrar las respuestas

Mensaje de despedida 

# Fuentes:

https://www.fifa.com/es/tournaments/mens/worldcup
