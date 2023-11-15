''' JEU DE COMBAT '''

import random

ME = 50 # Chaque attaque inflige un dégâts de vie aléatoire entre 5 et 10 à l'ennemi
ENNEMI = 50 # Chaque attaque de l'ennemi m'inflige un dégâts de vie aléatoire compris entre 5 et 15 

MY_POTION = 3 # Chaque potion permet de récuperer un point de vie entre 15 et 50 (Aléatoire)
              # Lorsque j'utilise une potion, je passe le prochain tour

while True:

  # Mon attaque
  while True:
    FPHRASE = input("👉Souhaitez-vous attaquer(1) ou utiliser une potion (2) ?  ")
    if not FPHRASE.isdigit(): # Verifier si la valeur n'est pas un digit
      print("⚠️ Veuillez entrer 1 ou 2 ")
      continue
    elif FPHRASE.isdigit(): # Verifier si la valeur est un digit
      try:  # Si oui éxecuter le code dans le try
        FPHRASE = int(FPHRASE)
        if FPHRASE == 1:  # Attaquer l'ennemi
          coup_epe = random.randint(5, 10)
          ENNEMI -= coup_epe
          print(f"Vous avez infligé {coup_epe} points de dégâts à l'ennemi ⚔️")
          break
        elif FPHRASE == 2:  # Utiliser une potion
            if MY_POTION > 0:
              potion = random.randint(15, 50)
              ME += potion
              MY_POTION -= 1
              print(f"Vous avez recupéré {potion} points de vie en utilisant une potion")
              print(f"Il vous reste {MY_POTION} potion{'s' if MY_POTION > 1 else ''} ⚗️🧪💊")
            elif MY_POTION <= 0:
              print("Oups ⚠️ !!!!")
              continue
            break
      except TypeError: # Si le transtypage est un échec et renvoie une TypeError on remonte au début de la boucle
        print("Oups ⚠️ !!!!")
        continue
    
  # L'attaque de l'ennemi
  coup_epe2= random.randint(5, 15)
  ME -= coup_epe2
  print(f"L'ennemi vous a infligé {coup_epe2} points de dégâts ⚔️\n")
  print(f"Il vous reste {ME} points de vie . ") if ME > 0 else print("Il vous reste 0 point de vie")
  print(f"Il reste {ENNEMI} points de vie à l'ennemi 👹. ") if ENNEMI > 0 else print("Il rest 0 point de vie à l'ennemi")
  print("-"*70)
  if ME > 0 and ENNEMI > 0:
   continue
  elif ME <= 0 or ENNEMI <= 0: # Fin de jeu
      if ME <= 0 and ENNEMI > 0:   # J'ai perdu
        print("Vous avez perdu le jeu 😵😣")
      elif ME > 0 and ENNEMI <= 0:
          print("YOUPIIIIII Vous avez gagné 🥳")
      elif ME == ENNEMI:
          print("Vous êtes à égalité")
      
  break