import string
from random import choice

print("""
  _____       _           _     __  __ _         _ _      
 |  __ \     | |         | |   |  \/  (_)       (_) |     
 | |__) |___ | |__   ___ | |_  | \  / |_ ___ ___ _| | ___ 
 |  _  // _ \| '_ \ / _ \| __| | |\/| | / __/ __| | |/ _ \.
 | | \ \ (_) | |_) | (_) | |_  | |  | | \__ \__ \ | |  __/
 |_|  \_\___/|_.__/ \___/ \__| |_|  |_|_|___/___/_|_|\___|                                                   
         __
 _(\    |@@|                   
(__/\__ \--/ __
   \___|----|  |   __
       \ }{ /\ )_ / _\.
       /\__/\ \__O (__   
      (--/\--)    \__/
      _)(  )(_
     `---''---`
""")
print("Digite o código correto | Letra de A-Z")
print("DESARME O MÍSSIL. Você tem 4 chances\n")

codigo = choice(string.ascii_uppercase)
chances = 4

for _ in range(chances):
    print(f"Chances restantes: {chances}")
    chute = str(input("Tente adivinhar o código: ")).upper()
    chances -= 1
    if chute == codigo:
        print("TICK...FZZZZ...CLICK...\nVocê conseguiu!")
        break
    elif ord(chute) < ord(codigo):
        print(f"DEPOIS DE {chute}")
    elif ord(chute) > ord(codigo):
        print(f"ANTES DE {chute}")

if chances == 0:
    print(f"BOOOOOOOOOOOOMMM....\nVirou churrasquinho!\nO código correto era {codigo}")
