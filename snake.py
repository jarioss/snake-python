import turtle
import time
import random

delay = 0.1
snake_body_segment = []
score = 0
high_score = 0

#windows
wn = turtle.Screen()
#title
wn.title('JUEGO DE LA CULEBRITA')
#windows size
wn.setup(width=600, height=600 )
#background color
wn.bgcolor('lightgreen')

#Head settings
head = turtle.Turtle()
#hacerlo estatico
head.speed(0)
#shape
head.shape('square')
#head color
head.color('green')
#no dibujar el rastro
head.penup()
# fijar centro en 0,0
head.goto(0,0)
#head direction como es una propiedad se pone con la igualdad
head.direction = 'stop'

#food settings
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)
food.direction = 'stop'

#score settings
text = turtle.Turtle()
text.speed(0)
text.color('black')
text.penup()
text.hideturtle()
text.goto(0,260)
text.write('Score: 0 High Score: 0', align='center', font=('Courier', 24, 'normal'))

def mov():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 10)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 10)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 10)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 10)

def go_up():
    head.direction = 'up'

def go_down():
    head.direction = 'down'

def do_rigth():
    head.direction = 'right'

def do_left():
    head.direction = 'left'


#conectar teclado
wn.listen()
#evento de teclado
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(do_rigth, 'Right')
wn.onkeypress(do_left, 'Left')

while True:
    wn.update()
    #colisiones con las paredes
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        #Esconder segmentos
        for segment in snake_body_segment:
            segment.goto(1000, 1000)

        snake_body_segment.clear()

        score = 0
        text.clear()
        text.write('Score: {} High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))


    #colision con la food
    if head.distance(food) < 20:
        x = random.randint(-208,280)
        y = random.randint(-208,280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('blue')
        new_segment.penup()

        snake_body_segment.append(new_segment)
        delay -= 0.01
        score += 10
        if score > high_score:
            high_score = score
        text.clear()
        text.write('Score: {} High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))

    total_segments = len(snake_body_segment)

    for i in range(total_segments - 1, 0, -1):
        x = snake_body_segment[i - 1].xcor()
        y = snake_body_segment[i - 1].ycor()
        snake_body_segment[i].goto(x, y)


    if total_segments > 0:
        x = head.xcor()
        y = head.ycor()
        snake_body_segment[0].goto(x, y)

    mov()
    #colisiones con el cuerpo
    for segment in snake_body_segment:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            for segment in snake_body_segment:
                segment.goto(1000, 1000)

            snake_body_segment.clear()

            score = 0
            text.clear()
            text.write('Score: {} High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))

        


    time.sleep(delay)


turtle.done()

