"""
While traveling to Zortan, Louis packed lots of stuff. Let's
see if he has anything that matches your favorite color.

INFO -
------

`match` is a new operator introduced in Python 3.10
"""

fav_color = input("Enter your favorite color:  ").lower()

match fav_color:
    case "black":
        print("Louis has a BLACK T-Shirt.")
    case "red":
        print("Louis has a RED car.")
    case "yellow":
        print("Louis has a YELLOW shoes.")
    case "green":
        print("Louis has a GREEN hat.")
    case _:
        print("Louis does not own anything in {fav_color}.")
