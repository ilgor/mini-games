import time
from turtle import Screen, Turtle

screen = Screen()
screen.title('Snake Game')
screen.bgcolor("white")

pen = Turtle()
pen.speed(0)

step = 10
pen.width(step)
pen.hideturtle()  # Hide the turtle cursor
snake_size = 10

positions = [(0, 0)]


def draw_segment(position, color):
    pen.penup()  # Ensure the pen is up to avoid unwanted drawing
    pen.goto(position)
    pen.dot(snake_size, color)


draw_segment(positions[0], "blue")


def move_snake(color):
    head_x, head_y = positions[-1]

    if pressed_key == 'Right':
        new_head_x = head_x + step
        new_head_y = head_y
    if pressed_key == 'Left':
        new_head_x = head_x - step
        new_head_y = head_y
    if pressed_key == 'Up':
        new_head_x = head_x
        new_head_y = head_y + step
    if pressed_key == 'Down':
        new_head_x = head_x
        new_head_y = head_y - step

    positions.append((new_head_x, new_head_y))
    draw_segment(positions[-1], color=color)

    # Remove the tail segment from the list
    tail = positions.pop(0)
    draw_segment(tail, "white")


pressed_key = None


def on_key_press(key):
    global pressed_key
    pressed_key = key

    print(f"Key pressed: {pressed_key}")


screen.listen()
screen.onkey(lambda: on_key_press("Up"), "Up")
screen.onkey(lambda: on_key_press("Down"), "Down")
screen.onkey(lambda: on_key_press("Left"), "Left")
screen.onkey(lambda: on_key_press("Right"), "Right")
screen.onkey(lambda: on_key_press("q"), "q")


while pressed_key not in ['Up', 'Down', 'Left', 'Right']:
    print(pressed_key)
    pen.dot(snake_size, 'blue')
    time.sleep(0.5)
    pen.dot(snake_size, 'white')
    time.sleep(0.5)

while True:
    move_snake('red')


screen.mainloop()  # Keep the screen open
