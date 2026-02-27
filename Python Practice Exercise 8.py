#8:Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, #print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:

 #   Rock beats scissors
 #   Scissors beats paper
 #   Paper beats rock

while True:

    A=input("Player A: Rock/Paper/Scissors?")
    B=input("Player B: Rock/Paper/Scissors?")

    if A not in ["Rock", "Paper", "Scissors"] or B not in ["Rock", "Paper", "Scissors"]:
        print("Try again")
        continue
    
    elif A == B:
        print("draw") 

    elif A == "Rock":
        if B == "Scissors":
            print ("A wins!")
        elif B == "Paper":
            print ("B wins!")
    
    elif A == "Paper":
        if B == "Rock":
            print ("A wins!")
        elif B == ("Scissors"):
            print ("B Wins!")
    
    elif A == "Scissors":
        if B == "Paper":
            print ("A wins!")
        elif B == "Rock":
            print ("B Wins")

    

    x=input("Do you want to play again? y/n? ")
    if x =="y":
        continue
    else:
        break


