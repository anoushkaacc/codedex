import random

def play():
    print("================================\nRock Paper Scissors Lizard Spock\n================================")
    game_elements = ['✊', '✋', '✌️', '🦎', '🖖']
    print("1) ✊ (Rock)\n2) ✋ (Paper)\n3) ✌️ (Scissors)\n4) 🦎 (Lizard)\n5) 🖖 (Spock)")
    user_choice = int(input("Pick a number: ")) - 1
    computer_choice = random.randint(0, 4)

    print(f"\nYou chose: {game_elements[user_choice]}")
    print(f"CPU chose: {game_elements[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice==0 and computer_choice==2) or (user_choice==0 and computer_choice==3) :
        print("You win")
    elif (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==4):
        print("you win")      
    elif (user_choice==2 and computer_choice==1) or (user_choice==3 and computer_choice==3):
        print("you win")
    elif(user_choice==3 and computer_choice==1) or (user_choice==3 and computer_choice==4):
        print("you win")
    elif (user_choice==4 and computer_choice==0) or (user_choice==5 and computer_choice==2):
        print("you win")
    else:
      print("cpu wins")                



times = int(input("how many time you want to play? "))
while times > 0:
    play()
    times -= 1
