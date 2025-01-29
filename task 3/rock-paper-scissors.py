import random

def game():
    total_win=0
    total_lose=0
    while True:
        print("-------------------- Rock Paper Scissor --------------------")

        user_choice=int(input("Enter Your choice -\n---------------1 for Rock...\n------------------2 for Paper...\n-------------------3 for Scissor...\n----------------4 to display Total wins or loses...\n-----------------5 to (exit or END) the game :-"))
        comp_choice=random.randint(0,2)
        print(f"Your Choice : {user_choice}")
        print(f"Computer Choice : {comp_choice}")

        if user_choice==comp_choice:
            print("Its a DRAW...")
        elif user_choice==5:
            break
        elif user_choice==0 and comp_choice==2:
            print("You WIN...")
            total_win+=1
        elif user_choice==2 and comp_choice==0:
            print("You LOSE...")
            total_lose+=1
        elif comp_choice>user_choice:
            print("You LOSE...")
            total_lose+=1
        elif comp_choice<user_choice and user_choice<=3:
            print("You WIN...")
            total_win+=1
        elif user_choice==4:
            print(f"Total Wins : {total_win}")          
            print(f"Total Loses : {total_lose}")          
        else:
            print("Invalid Input...!!\nPlease Try Again...!!")
        
game()

        
        
        