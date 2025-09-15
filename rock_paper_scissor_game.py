import random
choice=["rock","scissor","paper","Rock","Scissor","Paper","r","s","p",]
win=0
rounds=0
lose=0
tie=0
print("Welcome to Rock, Paper, Scissor Game!")
while True:
    print("Enter your choice: rock, paper, scissor,(or q to quit)")
    user_input=input()
    rounds+=1
    if user_input  in  ["q","quit","Quit","Q"]:
        print("👋 Thanks for playing!")
        break
    if user_input not in choice:
        print("------Invalid_input-----")
        continue
    computer_choice=random.choice(choice)
    print(f"Computer choice: {computer_choice}")
    if user_input == computer_choice:
      print("----It is a tie---")
      tie+=1
    elif user_input in ["rock","Rock","r"] and computer_choice in ["scissor","Scissor","s"]:
        print("----You win---") 
        win+=1
    elif user_input in ["paper","Paper","p"] and computer_choice in ["rock","Rock","r"]:
        print("----You win---")
        win+=1
    elif user_input in ["scissor","Scissor","s"] and computer_choice in ["paper","Paper","p"]:
        print("----You win---")
        win+=1
    else:
        print("----You lose---")
        lose+=1
        
# Final Summary
print("\nGame Over!")
print(f"Total rounds played: {rounds}")
print(f"You won: {win} times")
print(f"You lost: {lose} times")
print(f"Ties: {tie} times")


