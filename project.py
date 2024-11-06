import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Play initial sound once
try:
    pygame.mixer.music.load("WhatsApp Audio 2023-01-08 at 13.56.05.mp3")
    pygame.mixer.music.play()
except:
    print("Initial audio file not found or failed to play.")

# FERRARI(F) LAMBORGHINI(L) or MERCEDES(M)
def gameWin(comp, you):
    if comp == you:
        return None
    elif (comp == 'F' and you == 'M') or (comp == 'L' and you == 'F') or (comp == 'M' and you == 'L'):
        return True
    else:
        return False

while True:
    print("Comp Turn: FERRARI(F) LAMBORGHINI(L) or MERCEDES(M)?")
    randNo = random.randint(1, 3)
    comp = 'F' if randNo == 1 else 'L' if randNo == 2 else 'M'

    # Get user input and validate
    you = input("Your Turn: FERRARI(F) LAMBORGHINI(L) or MERCEDES(M)?").upper()
    if you not in ['F', 'L', 'M']:
        print("Invalid input! Choose F, L, or M.")
    else:
        a = gameWin(comp, you)

        print(f"Computer chose {comp}")
        print(f"You chose {you}")

        if a is None:
            print("The game is a tie!")
        elif a:
            print("You Win!")
            # Play winning sound
            try:
                pygame.mixer.music.load("dhoooom.wav")
                pygame.mixer.music.play()
            except:
                print("Winning audio file not found or failed to play.")
        else:
            print("You Lose!")
