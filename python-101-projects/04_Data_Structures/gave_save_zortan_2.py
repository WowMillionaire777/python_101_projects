"""
Save Zortan:
------------

The war has just intensified, Thanos army has reach Zortan and are going to
fight along with him. With his army, this time Thanos is going to attach Avengers
and the battle is going to be intense!!!

Since, everything is going in real-time, we don't have control over characters,
instead our characters will choose their own fight.

This time each character gets it own structure and defined parameters, so as you
can see our code is getting better and certainly we are going to make is awesome
as we progress with future modules.
"""

# we need this for generating random nos.
from random import randint
from typing import Final


# -------------------------------------------------------------------------
# TYPE ALIAS:
# ===========
# Each time typing type as dict[str, str | int] is so boring, so we instead
# create a type alias and make our lives simpler.
# -------------------------------------------------------------------------

Character = dict[str, str | int]

# Declare Avengers
IRONMAN: Final[Character] = {"name": "Ironman", "attack_power": 250, "life": 1000}
BLACKWIDOW: Final[Character] = {"name": "Black Widow", "attack_power": 180, "life": 800}
SPIDERMAN: Final[Character] = {"name": "Spiderman", "attack_power": 190, "life": 700}
HULK: Final[Character] = {"name": "Incredible Hulk", "attack_power": 300, "life": 1100}

# Declare Super Villians
THANOS: Final[Character] = {"name": "Thanos", "attack_power": 1500, "life": 1500}
REDSKULL: Final[Character] = {"name": "Redskull", "attack_power": 300, "life": 800}
PROXIMA: Final[Character] = {"name": "Proxima", "attack_power": 320, "life": 800}

# List of Avengers and Super Villians
avengers: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
supervillains: list[Character] = [THANOS, REDSKULL, PROXIMA]

# Helper variables
avenger_life = 0
villain_life = 0

# declare helper messages
WIN_MSG: Final[str] = "You successfully saved Zortan!!! ✨ ✨ ✨"
LOST_MSG: Final[str] = "Thanos killed the Avengers and captured Zortan!! 💀 💀 💀"

# Attack
for attack in range(3):
    # each iteration get a new hero & villian
    hero_index1 = randint(0, 3)
    hero_index2 = randint(0, 3)
    hero_index3 = randint(0, 3)
    villain_index1 = randint(0, 2)
    villain_index2 = randint(0, 2)
    # help variables
    first_avenger = avengers[hero_index1]
    second_avenger = avengers[hero_index2]
    third_avenger = avengers[hero_index3]
    first_villain = supervillains[villain_index1]
    second_villain = supervillains[villain_index2]
    # Total life
    avengers_life = (
        first_avenger["life"] + second_avenger["life"] + third_avenger["life"]
    )
    villains_life = first_villain["life"] + second_villain["life"]
    # Total Attack Power
    avengers_atk_power = (
        first_avenger["attack_power"]
        + second_avenger["attack_power"]
        + third_avenger["attack_power"]
    )
    villains_atk_power = first_villain["attack_power"] + second_villain["attack_power"]
    # attack
    avengers_life -= villains_atk_power
    villains_life -= avengers_atk_power

    print(
        f"""
Attack: {attack + 1} => {first_avenger['name']} & {second_avenger['name']} & {third_avenger['name']} battles {first_villain['name']} & {second_villain['name']}!"""
    )
    print("=" * 70)
    print(
        f"Avengers' Attack Power: {avengers_atk_power}  Villains' Attack Power: {villains_atk_power}!!!"
    )
    print(f"Avengers' Life: {avengers_life}  Villains' Life: {villains_life}!!!")


# Print a nice separating line
print("=" * 70)

# win / lose
if villains_life == 0 or avengers_life > villains_life:
    print(WIN_MSG)
else:
    print(LOST_MSG)

# while True:

#     #
#     if thanos_life <= 0 and attack_num <= 3:
#         # win
#
#         break
#     elif attack_num >= 3:
#         # lose
#         print(LOST_MSG)
#         break

#     # enter the game
#     print(MSG)
#     choice = int(input("Enter your pair no >>> "))

#     if choice == 1:
#         print("Ironman & Black Widow are attacking Thanos....")
#         print(f"Thanos' Life has: {thanos_life} left.")
#         thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
#         attack_num = attack_num + 1
#     elif choice == 2:
#         print("Black Widow & Spiderman are attacking Thanos....")
#         print(f"Thanos' Life has: {thanos_life} left.")
#         thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
#         attack_num = attack_num + 1
#     elif choice == 3:
#         print("Spiderman & Hulk are attacking Thanos....")
#         print(f"Thanos' Life has: {thanos_life} left.")
#         thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
#         attack_num = attack_num + 1
#     elif choice == 4:
#         print("Hulk & Ironman are attacking Thanos....")
#         print(f"Thanos' Life has: {thanos_life} left.")
#         thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER
#         attack_num = attack_num + 1
