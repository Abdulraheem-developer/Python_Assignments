playerOne = input("Player one play!: ")
playerTwo = input("Player two play!: ")

if playerOne == "rock" and playerTwo == "paper":
    print("Player 2 wins")
    
elif playerOne == "rock" and playerTwo == "scissors":
    print("Player 1 wins!")
    
 elif playerOne == "rock" and playerTwo == "rock":
    print("It's a tie!")
    
else:
        print("Invalid play!")
        
        
if playerOne == "paper" and playerTwo == "rock":
    print("Player 1 wins")
    
    
elif playerOne == "paper" and playerTwo == "scissors":
    print("Player 1 wins")
    
elif playerOne == "paper" and playerTwo == "scissors":
    print("It's a tie!")
    
else: 
    print("Invalid play!")
    
    
if playerOne == "scissors" and playerTwo == "rock":
    print("Player 2 wins!")
    
elif playerOne == "scissors" and playerTwo == "paper":
    print("Player 1 wins")
    
elif playerOne == "scissors" and playerTwo == "scissors":
    print("It's a tie")
    
else: 
    print("It's a tie!")
