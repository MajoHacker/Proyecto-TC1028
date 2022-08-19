# Proyecto-TC1028

Este proyecto es creado por María José Gaytán Gil A01706616, de la clase TC 1028

Espero les guste :)

# El torneo más prestigioso del mundo

"En la Copa Mundial Masculina de la FIFA, que se celebra cada cuatro años, 32 naciones compiten entre sí por el título. Los distintos clasificatorios continentales dan paso a una fase final de lo más emocionante, que congrega a los aficionados en torno a la pasión y el amor por el deporte rey." (FIFA, 2022) 

Este año se jugara la edición número 22 en Qatar, por ello la finalidad de este programa es determinar que tan preparado estás para ver esta copa del mundo mediante series de preguntas que determinaran en que nivel te encuentras (todas las respuestas a las preguntas son sacadas del sitio oficial de la FIFA), al final el programa arrojara tu resultado en 3 distintos niveles en los que el programa puede posicionarte en el más bajo: principiante (0-5 respuestas correctas), el intermedio: profesional (6-10 respuestas correctas), y el más alto: legendario (11-15 respuestas correctas).


# Pseudocódigo

Mostrar mensaje de bienvenida al usuario

nombre_usuario: ¿Como te llamas?

comenzar: ¿Estas listo para comenzar? (sí=1, no=0)

Si comenzar es == 1:

  comenzar prueba
  
Si comenzar es == 0:

  volver a mostar la pregunta
  
contar_puntos: 0 (variable que contara nuestros puntos)

pregunta_1: ¿Qué día inicia el mundial 2022?

Opciones:

a: 21 de noviembre 

b: 19 de noviembre 

c: 20 de noviembre (correcta)

d: 22 de noviembre 

Si pregunta_1 == c:
  
  contar_puntos + 1
  
  mostrar correcto

Sino mostrar incorrecto
  
 pregunta_2: ¿Qué dia termina la competición?

Opciones:

a: 18 de diciembre (correcta)

b: 17 de diciembre 

c: 19 de diciembre 

d: 20 de diciembre

Si pregunta_2 == a:
  
  contar_puntos + 1
  
  mostrar correcto

Sino mostrar incorrecto
  
pregunta_3: ¿Cuántos grupos hay?

Opciones:

a: 8 grupos (correcta)

b: 6 grupos

c: 10 grupos

d: 12 grupos

Si pregunta_3 == a:
  
  contar_puntos + 1
  
  mostrar correcto

Sino mostrar incorrecto
  
pregunta_4: ¿Cuántas selecciones hay por grupo?

Opciones:

a: 3 selecciones

b: 4 selecciones (correcta)

c: 5 selecciones

d: 6 selecciones

Si pregunta_4 == b:
  
  contar_puntos + 1
  
  mostrar correcto

Sino mostrar incorrecto
  
pregunta_5: ¿Quién es el actual campeón de la competición?

Opciones:

a: Inglaterra

b: Croacia

c: argentina 

d: Francia (correcta)

Si pregunta_5 == d:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto

pregunta_6: ¿Cuál es el partido que inagurara la competición?

Opciones:

a: Qatar vs Senegal

b: Argentina vs México

c: Qatar vs Ecuador (correcta)

d: Ecuador vs Senegal

Si pregunta_6 == c:
  
  contar_puntos + 1
  
  mostrar correcto

Sino mostrar incorrecto

pregunta_7: ¿En qué estadio se disputara la final?

Opciones:

a: Al Bayt Stadium

b: Lusail de Qatar Stadium (correcta)

c: El Al Thumama Stadium

d: Ras Abu Aboud Stadium

Si pregunta_7 == b:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto

pregunta_8: ¿Cuál es la selección con más mundiales?

Opciones:

a: Francia

b: Argentina 

c: Brasil

d: Uruguay (correcta)

Si pregunta_8 == d:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto
  
pregunta_9: ¿Cuál es el jugador que ha anotado más goles en los mundiales?

Opciones:

a: Miroslav Klose (correcta)

b: Pelé

c: Maradona 

d: Lionel Messi

Si pregunta_9 == a:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto

pregunta_10: ¿En que grupo esta México?

Opciones:

a: Grupo E

b: Grupo D

c: Grupo C (correcta)

d: Grupo A

Si pregunta_10 == c:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto

pregunta_11: ¿Qué selección enfrentara México en su primer partido?

Opciones:

a: Polonia (correcto)

b: Argentina

c: Arabia Saudita 

Si pregunta_11 == a:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto

pregunta_12: ¿Cuántas selecciones por grupo pasan a la siguente ronda?

Opciones:

a: 1 selección y la otra va a recalificación

b: 3 selecciones 

c: 1 selección

d: 2 selecciones (correcto)

Si pregunta_12 == d:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto

pregunta_13: ¿En caso de empate en la final cuánto dura el tiempo extra?

Opciones:

a: 25 minutos

b: 30 minutos (correcta)

c: 45 minutos 

d: 20 minutos 

Si pregunta_13 == b:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto

pregunta_14: ¿Cuál es el maximo de jugadores que puede llevar una selección?

Opciones:

a: 23 jugadores (correcta)

b: 22 jugadores 

c: 25 jugadores 

d: 20 jugadores 

Si pregunta_14 == a:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto

pregunta_15: ¿Cuántos partidos se juegan durante la competición?

Opciones:

a: 58 partidos

b: 52 partidos 

c: 64 partidos (correcta)

d: 60 partidos 

Si pregunta_15 == c:
  
  contar_puntos + 1

  mostrar correcto

Sino mostrar incorrecto
  
res: preguntar al nombre_usuario si desea conocer su puntuación (si=1, no=0)

Si res es == 1:

  mostrar resultados: 
  
   si contar_puntos <= 5:
  
   mostar al usurio el total de puntos y decirle que es un nivel principiante.
  
   si contar_puntos <= 10:
  
   mostar al usuario el total de puntos y decirle que es un nivel profesional.
  
   si contar_puntos <= 15:
   
   mostar al usurio el total de puntos y decirle que es un nivel legendario.
  
Si res es == 0:

  volver a mostar la pregunta

Mensaje de despedida 





# Fuentes:

https://www.fifa.com/es/tournaments/mens/worldcup
