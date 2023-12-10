import random

slovar_drzav = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid","Slovenia": "Ljubljana", "Italy": "Rome"}

#program naključno izbere državo: key in ga shrani v 'random_key'. 
while True:
 random_key=random.choice(list(slovar_drzav.keys()))

 while True:
    user_input=input(f"Navedi prestolnico države {random_key}:")
    if user_input.lower() == slovar_drzav[random_key].lower(): #z lower fukcijo pretvori vse v male črke
        print("Bravo, uganil si")
        break
    else:
        print(f"Narobe")
        
        