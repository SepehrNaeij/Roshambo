import random
from datetime import datetime
import os
import sqlite3
from result import Result

sql = sqlite3.connect('result.db')
r = sql.cursor()

# **************to making table for our database********
# -----------------------------------------------------------
#r.execute("""CREATE TABLE gameresults (       
#      p1 text,
#      p2 text,
#      win_p1 integer,
#      win_p2 integer,
#      draw integer
# -----------------------------------------------------------
#)""")

def help():
    print("\n    ***All Commands***")
    print("""
    play---------> to start the game.
    show---------> to show the result of all the saved game.
    help---------> to help you how work with this program.
    exit---------> to close the game.
    """)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')    

def choice():
    selection = random.choice(choices)
    return selection

def winner(player1, player2):
    if player1 == "Rock" and player2 == "Rock":
        result = "Draw\n______________\n"
    elif player1 == "Rock" and player2 == "Paper":
        result = Player2 + " wins\n______________\n"
    elif player1 == "Rock" and player2 == "Scissors":
        result = Player1 + " wins\n______________\n"
    elif player1 == "Paper" and player2 == "Paper":
        result = "Draw\n______________\n"
    elif player1 == "Paper" and player2 == "Rock":
        result = Player1 + " wins\n______________\n"
    elif player1 == "Paper" and player2 == "Scissors":
        result = Player2 + " wins\n______________\n"
    elif player1 == "Scissors" and player2 == "Scissors":
        result = "Draw\n______________\n"
    elif player1 == "Scissors" and player2 == "Rock":
        result = Player2 + " wins\n______________\n"
    elif player1 == "Scissors" and player2 == "Paper":
        result = Player1 + " wins\n______________\n"
    return result


clear()

while True:

    help()
    print("Enter a command:")
    message = input()

    if message == "play":

        clear()
        date=datetime.now()
        choices = ["Rock", "Paper", "Scissors"]

        print("Enter the name of player1:")
        Player1=input()
        print("Enter the name of player2:")
        Player2=input()
        print("Enter the number of times of games between them:")
        number_game=int(input())
        print("\n")
        clear()
        print("\n")

        player_1_wins = 0
        player_2_wins = 0
        number=0        
        while number<number_game :
            number=number+1
            player_1 = choice()
            player_2 = choice()
            check_wins = winner(player_1, player_2)
            print(Player1  + " plays %s" % player_1)
            print(Player2  + " plays %s" % player_2) 
            print(check_wins)
            # Here's where we'll overwrite the counts of the wins
            if check_wins == Player1 + " wins\n______________\n":
                player_1_wins = player_1_wins + 1
            elif check_wins == Player2 + " wins\n______________\n":
                player_2_wins = player_2_wins + 1 
            else:
                pass

        number_draw = number_game - player_1_wins - player_2_wins
      
        print("\n********  Result of the match  ********\n")
        print(Player1 + " total wins: %i" % player_1_wins)
        print(Player2 + " total wins: %i" % player_2_wins)
        print("Numbers of Draw: %i" % number_draw )
        print("\nDo you want to save this game???\n 1.yes   2.No\n\nEnter a number(1 or 2):")

        answer=input()

        if answer=="1":
            mr = Result(Player1, Player2, player_1_wins, player_2_wins, number_draw)
            r.execute("INSERT INTO gameresults VALUES (?, ?, ?, ?, ?)" , (mr.p1, mr.p2, mr.p1_wins, mr.p2_wins, mr.draw))
            sql.commit()
            print("your game is successfully saved in : " + str(date) )
            break
        elif answer=="2":
            print("OK,Thanks for using us.")
            break

    elif message == "show":
        clear()
        print("How do you want the results to be show???\n1.All results   2.Some result\n\nEnter a number(1 or 2):")
        in1=input()
        if ( in1=="1"):
            r.execute("SELECT * FROM gameresults")
            print(r.fetchall())
            sql.commit()
        elif ( in1=="2"):                
            print("Enter the players name to find it file:")
            in2=input()
            in3=input()
            r.execute("SELECT * FROM gameresults WHERE p1=? OR p2=?", (in2, in3))
            if r.fetchall()==[]:
                print("There isn't any player with this name in saved game list!!!")
            else:    
                r.execute("SELECT * FROM gameresults WHERE p1=? OR p2=?", (in2, in3))
                print(r.fetchall())
                sql.commit()

    elif message == "exit":
            clear()
            print("Goodbye.")
            break

    elif message == "help":
            clear()
            help()

    else:
        clear()
        print("Invalid input!!!")                
        help()

sql.close()
