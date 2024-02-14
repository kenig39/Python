# import os
import random

import turtle
#requared by macOS to show window
turtle.fd(0)
# Set the animation speed to max
turtle.speed(0)
# Change the bg
turtle.bgcolor("blue")
turtle.ht()
# this save memory
turtle.setundobuffer(1)
# this speed up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
      self.fd(self.speed)

# Boundary detection
      if self.xcor() > 290:
          self.setx(290)
          self.rt(60)

      if self.xcor() < -290:
          self.setx(-290)
          self.rt(60)

      if self.ycor() > 290:
          self.sety(290)
          self.rt(60)

      if self.ycor() < -290:
          self.sety(-290)
          self.rt(60)

    def is_collision(self, other):
      if (self.xcor() >= (other.xcor() - 20)) and \
      (self.xcor() <= (other.xcor() + 20)) and \
      (self.ycor() >= (other.ycor() - 20)) and \
      (self.ycor() <= (other.ycor() + 20)):
             return True
      else:
             return False

class Player(Sprite):
    def __init__(self, spiteshape, color, startx, starty ):
        Sprite.__init__(self,spiteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.left(45)

    def turn_right(self):
        self.right(45)

    def accelerate(self):
        self.speed += 1
    def decelerate(self):
        self.speed -= 1

# Create enemy
class Enemy(Sprite):
    def __init__(self, spiteshape, color, startx, starty ):
        Sprite.__init__(self,spiteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0,360))

class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
#         draw border
         self.pen.speed(0)
         self.pen.color("green")
         self.pen.pensize(3)
         self.pen.penup()
         self.pen.goto(-300, 300)
         self.pen.pendown()
         for side in range(4):
             self.pen.fd(600)
             self.pen.rt(90)
         self.pen.penup()
         # self.pen.ht

# create game object
game = Game()

# draw the game object
game.draw_border()

#Create my spites
player = Player("triangle", "white", 0, 0)
enemy = Enemy("circle", "red", -100, 0)

#Keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()
# main game loop
while True:
    player.move()
    enemy.move()

# check is collision
    if player.is_collision(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x,y)

