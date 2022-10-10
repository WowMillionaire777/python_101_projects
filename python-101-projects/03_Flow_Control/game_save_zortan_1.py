"""
Zortan is under attack!!! Thanos has arrived!
---------------------------------------------

Since Zortan is under attack, Louis calls his Avenger friends from earth.
Avengers receive his call and sends 4 avengers to save Zortan.

1. Ironman
4. Black Widow
2. Spiderman
3. Hulk

Each avenger has its attacking power and they have to fight Thanos
to save Zortan.

Avengers can attack only in pairs and get only 3 chances to kill Thanos,
or else Thanos will kill avengers and we loose the game.
"""

from typing import Final

IRONMAN_ATTACK_POWER: Final[int] = 300
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 400

thanos_life: int = 1500
choice = 0
attack_num: int = 0

# declare helper messages
WIN_MSG: Final[str] = "You successfully saved Zortan!!! ✨ ✨ ✨"
LOST_MSG: Final[str] = "Thanos killed the Avengers and captured Zortan!! 💀 💀 💀"
MSG = f"""
---------------------------------------------------------------------
Zortan is under attack, choose the pairs no. that will attack Thanos

1) Ironman & Black Widow
2) Black Widow & Spiderman
3) Spiderman & Hulk
4) Hulk & Ironman
---------------------------------------------------------------------
Thanos has {thanos_life} left.
"""

while True:

    # win / lose
    if thanos_life <= 0 and attack_num <= 3:
        # win
        print(WIN_MSG)
        break
    elif attack_num >= 3:
        # lose
        print(LOST_MSG)
        break

    # enter the game
    print(MSG)
    choice = int(input("Enter your pair no >>> "))

    if choice == 1:
        print("Ironman & Black Widow are attacking Thanos....")
        print(f"Thanos' Life has: {thanos_life} left.")
        thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 2:
        print("Black Widow & Spiderman are attacking Thanos....")
        print(f"Thanos' Life has: {thanos_life} left.")
        thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 3:
        print("Spiderman & Hulk are attacking Thanos....")
        print(f"Thanos' Life has: {thanos_life} left.")
        thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 4:
        print("Hulk & Ironman are attacking Thanos....")
        print(f"Thanos' Life has: {thanos_life} left.")
        thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER
        attack_num = attack_num + 1
