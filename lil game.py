def winning_screen1():
    while True:
        text = input("Do you heal your hand or run?").lower()
        if "heal" in text:
            print("You wait to long trying to heal your hand and fall unconscious again!")
            return right_building()
        elif "run" in text:
            print("You run away as fast as you can!")
            return alley()
def jail():
    print("You are now in jail.")
    while True:
        text = input("Do you do your time or try to escape?").lower()
        if "time" in text:
            print("You sit in your cell for God knows how long, until you are finally released where you return to the scene of the crime.")
            return left_building()
        elif "escape" in text:
            print("You break through your cell and escape!")
            return "You live the rest of your life as a fugitive. Good luck."
def winning_screen2():
    print ("Congrats you have made friends with Raini as you decide how to respond to her generous offer!")
    while True:
        text = input("Will you accept, deny, or call the cops?").lower()
        if "accept" in text:
            print ("You smoke a J with Raini Rodriguez and have an awesome time!")
            return "You really win!"
        elif "deny" in text:
            print ("Raini is confused as to why you denied her offer, but passes no judgement.")
            return "You win!"
        elif "call" in text:
            print("Raini is offended and calls the president. The ensuing cops arrest you instead!")
            return jail()

def left_building():
    print ("As you gather your senses you see a floor littered with beanbags and drug \n paraphernalia. A woman approaches who you recognize to be Disney star Raini Rodriguez!")
    while True:
        text = input("Will you question, embrace, or fight her?").lower()
        if "question" in text:
            print("You ask Raini what she is doing, and she responds by offering you what seems to be a \n joint!")
            return winning_screen2()
        elif "leave" in text:
            print("You return to the alley.")
            return alley()
        elif "fight" in text:
            print("You attack Raini. Big mistake.")
            return "Raini literally kills you. You lose."
        elif "embrace" in text:
            print("You have crossed Raini's boundries and she asks you to leave.")
            return alley()
def right_building():
    print("You wake up chained to a pole.")
    while True:
        text = input("Do you scream, cry, or break free?").lower()
        if "scream" in text:
            print("You scream for an hour until a man finally enters.")
            return stranger()
        elif "cry" in text:
            print("You cry, but to no avail.")
            return "You are left chained to the pole forever."
        elif "break" in text:
            print("You smash the handcuffs at the cost of your own hand!")
            return winning_screen1()
def rat_friend():
    print ("Congrats you have made friends with the king!")
    while True:
        text = input("Do you wish to rule the world or live in peace?").lower()
        if "peace" in text:
            print ("You show mercy on the world and live a peaceful life with your new ally!")
            return "You win!"
        elif "rule" in text:
            print ("The king takes you to his nest where you press a button to destroy the world!")
            return "You were tricked by the king! But I guess you win. Pretty cool destroying the world or whatever."    
def rat_king():
    while True:
        text = input("Do you attempt to fight it or tame it?").lower()
        if "tame" in text:
            print("You hand the rat king some spare sandwich meat and he befriends you.")
            return rat_friend()
        elif "fight" in text:
            print("You are eaten alive by the rat king! What were you thinking?!")
            print("GAME OVER")

def sewer():
    print ("As you gather your senses you realize there is an awful smell!")
    while True:
        text = input("Do you investigate or leave?").lower()
        if "leave" in text:
            print("You return to the alley.")
            return alley()
        elif "investigate" in text:
            print("You move further into the sewers and discover a rat king!")
            return rat_king()
def alley():
    print("You are in a dark alley between two buildings, one to the right and one to the left.")
    while True:
        text = input("Do you go left, right or straight? ").lower()
        if "straight" in text:
            print("You stumble and fall through a manhole into the sewers!")
            return sewer()
        elif "turn around" in text:
            print("You leave and go home, but what did you miss?")
            return "You Win?"
        elif "right" in text:
            print("You go into the right building and are instantly knocked unconscious.")
            return right_building()
        elif "left" in text:
            print ("You enter the left building and are hit with a strong, unidentifiable scent.")
            return left_building()

def text_adventure():
    print(alley())
    return
print(text_adventure())