from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width = 500 , height = 500)
colors = ["red", "orange", "yellow","green", "blue", "purple"]

player_one = Turtle("turtle")   
player_one.penup()
player_one.goto(x=-230, y= 100)
player_one.color("red")
player_two = Turtle("turtle")      #tim.shape(turtle)
player_two.penup()
player_two.goto(x=-230, y= -100)
player_two.color("green")

for i in range(20):
    player_one_turn = input("Press 'Enter' to roll the die ")
    die_outcome = random.randint(1,6)
    print("The result of the die roll is: ")
    print(die_outcome)
    print("The number of steps will be: ")
    print(20*die_outcome)
    player_one.fd(20*die_outcome)
    if player_one.xcor() > 230:
            print("Player One Wins!")
            break
    player_two_turn = input("Press 'Enter' to roll the die ")
    die_outcome = random.randint(1,6)
    print("The result of the die roll is: ")
    print(die_outcome)
    print("The number of steps will be: ")
    print(20*die_outcome)
    player_two.fd(20*die_outcome)
    if player_two.xcor() > 230:
            print("Player Two Wins!")
            break
            
