import random
play="Yes"
while play=="Yes":
    user_choice=input("Enter your choice:(Rock Paper Scissors)")
    choices=["Rock","Paper","Scissors"]
    if(user_choice not in choices):
        print("Invalid Choice!\nChoose again.")
        break
    comp_choice=random.choice(choices)
    print("Your choice:" ,user_choice,"\nComputer choice:",comp_choice)
    if(user_choice==comp_choice):
        print("It's a tie.")
    elif(user_choice=="Rock" ):
        if (comp_choice=="Scissors"):
            print("You Win!")
        else:
            print("You Lose!")
    elif(user_choice=="Paper" ):
        if (comp_choice=="Rock"):
            print("You Win!")
        else:
            print("You Lose!")
    elif(user_choice=="Scissors" ):
        if (comp_choice=="Paper"):
            print("You Win!")
        else:
            print("You Lose!")
    play=input("Do you want to play again? Yes/No:")
    



    

