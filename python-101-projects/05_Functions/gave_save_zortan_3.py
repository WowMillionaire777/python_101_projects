"""
Save Zortan:
------------

Let's convert the game logic into small functions.

Principles:
-----------

1. DRY - Don't Repeat Yourself -
================================
Try to keep your code as DRY as possible, group common functionality into
individual functions.

2. SRP - Single Responsibility Principle -
==========================================
Ideally one function should be responsible for only one operation.

Note:
-----
We will also learn about global & local scope of variables (Using scratch pad)
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

# ---------------------------- Life -------------------------------

# Helper Variables
avengers_life = 0
villains_life = 0


def inc_avengers_life(life: int) -> None:
    """Increases Hero Life"""
    global avengers_life
    avengers_life += life


def dec_avengers_life(life: int) -> None:
    """Decreases Hero Life"""
    global avengers_life
    avengers_life -= life


def inc_villains_life(life: int) -> None:
    """Increases Villain Life"""
    global villains_life
    villains_life += life


def dec_villains_life(life: int) -> None:
    """Decreases Villain Life"""
    global villains_life
    villains_life -= life

# ---------------------------- Attack Power -------------------------------

# Helper Variables
avengers_life = 0
villains_life = 0


def inc_avengers_life(life: int) -> None:
    """Increases Hero Life"""
    global avengers_life
    avengers_life += life


def dec_avengers_life(life: int) -> None:
    """Decreases Hero Life"""
    global avengers_life
    avengers_life -= life


def inc_villains_life(life: int) -> None:
    """Increases Villain Life"""
    global villains_life
    villains_life += life


def dec_villains_life(life: int) -> None:
    """Decreases Villain Life"""
    global villains_life
    villains_life -= life


# ---------------------------- Superheros -------------------------------


def get_all_avengers() -> list[Character]:
    IRONMAN: Final[Character] = {"name": "Ironman", "attack_power": 250, "life": 1000}
    BLACKWIDOW: Character = {"name": "Black Widow", "attack_power": 180, "life": 800}
    SPIDERMAN: Character = {"name": "Spiderman", "attack_power": 190, "life": 700}
    HULK: Character = {"name": "Incredible Hulk", "attack_power": 300, "life": 1100}

    # List of Avengers
    avengers: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
    return avengers


def get_avenger(index: int) -> Character | None:
    """Returns an Avenger from the given index"""

    avengers = get_all_avengers()
    if index < len(avengers):
        return avengers[index]
    else:
        return None


# ---------------------------- Villains -------------------------------


def get_all_villains() -> list[Character]:
    THANOS: Final[Character] = {"name": "Thanos", "attack_power": 1500, "life": 1500}
    REDSKULL: Character = {"name": "Redskull", "attack_power": 300, "life": 800}
    PROXIMA: Character = {"name": "Proxima", "attack_power": 320, "life": 800}

    # List of Super Villians
    supervillains: list[Character] = [THANOS, REDSKULL, PROXIMA]
    return supervillains


def get_super_villain(index: int) -> Character | None:
    """Returns a villain from the given index"""

    supervillains = get_all_villains()
    if index < len(supervillains):
        return supervillains[index]
    else:
        return None


# Helper variables
avenger_life = 0
villain_life = 0

# declare helper messages
WIN_MSG: Final[str] = "You successfully saved Zortan!!! ✨ ✨ ✨"
LOST_MSG: Final[str] = "Thanos killed the Avengers and captured Zortan!! 💀 💀 💀"


def attack() -> None:
    # Attack
    for attack_num in range(3):
        # each iteration get a new hero & villian
        hero_index1 = randint(0, 3)
        hero_index2 = randint(0, 3)
        hero_index3 = randint(0, 3)
        villain_index1 = randint(0, 2)
        villain_index2 = randint(0, 2)
        # help variables
        first_avenger = get_avenger[hero_index1]
        second_avenger = get_avenger[hero_index2]
        third_avenger = get_avenger[hero_index3]
        first_villain = get_super_villain[villain_index1]
        second_villain = get_super_villain[villain_index2]

        if (
            first_avenger
            or second_avenger
            or third_avenger
            and first_villain
            or second_villain
        ):
            simulate_attack(
                attack_num,
                first_avenger,
                second_avenger,
                third_avenger,
                first_villain,
                second_villain,
            )
        else:
            print("Error! No avengers or villains show up for the fight!!!")


def simulate_attack(
    attack_num,
    first_avenger,
    second_avenger,
    third_avenger,
    first_villain,
    second_villain,
):
    """Simulate the actual attack"""

    # Total life of Avengers and Super Villains
    avengers_life: int = (
        first_avenger["life"] + second_avenger["life"] + third_avenger["life"]
    )
    villains_life = first_villain["life"] + second_villain["life"]
    # Total Attack Power of Avengers and Super Villains
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
        Attack: {attack_num + 1} => {first_avenger['name']} & {second_avenger['name']} & {third_avenger['name']} battles {first_villain['name']} & {second_villain['name']}!"""
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
