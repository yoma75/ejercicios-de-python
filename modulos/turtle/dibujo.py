import turtle

turtle.setup(600, 600)  # tamaño de la ventana
turtle.bgcolor('black') # color de fondo
turtle.color('white')  # color de linea 
turtle.speed(0)  # velocidad
turtle.width(6)  # ancho de linea

for i in range(110):
  turtle.forward(i * 5)  # mover hacia adelante
  turtle.right(90)  # girar 90º hacia la derecha

turtle.Screen().exitonclick()  # mantener la ventana abierta