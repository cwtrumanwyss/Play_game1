import json
import os
import time

def main():
    # TODO: allow them to choose from multiple JSON files?
    json_files = []
    for file in os.listdir():
        if file[-5:] == '.json':
            json_files.append(file)
    if len(json_files) == 0:
        print("Oops! There are no adventure files!")
        return
    print("Which game do you wish to play?")
    for i in range(len(json_files)):
        print(str(i + 1) + '. ' + json_files[i])
    filenumber = input('>').lower().strip()
    try:
        num = int(filenumber) - 1
        filetitle = json_files[num]
    except:
        print ("Sorry, I don't understand '{}'...".format(filenumber))
        return
    with open(filetitle) as fp:
        game = json.load(fp)
    print_instructions()
    print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
    print("")
    play(game)


def play(rooms):
    # Where are we? Look in __metadata__ for the room we should start in first.
    if not check_all_exits(rooms):
        print("These exits won't take you anywhere!")
        
    starttime = time.time()
    
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    stuff = ['Cell Phone; no signal or battery...']

    while True:
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        print(here['description'])
        if len(here['items']) != 0:
            for i in here['items']:
                print('There is a' + i)

        # TODO: print any available items in the room...
        # e.g., There is a Mansion Key.

        # Is this a game-over?
        if here.get("ends_game", False):
            break

        # Allow the user to choose an exit:
        usable_exits = find_usable_exits(here, stuff)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            print("  {}. {}".format(i+1, exit['description']))

        # See what they typed:
        action = input("> ").lower().strip()

        # If they type any variant of quit; exit the game.
        if action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break
        
        if action == 'help':
            print_instructions()
            continue
        if action == 'stuff':
            if len(stuff) == 0:
                print ('You do not have anything')
            else:
                print('===Items===')
                for s in stuff:
                    print(s)
                print('===Items===')
            continue
        if action == 'take':
            stuff.extend(here['items'])
            here['items'] = []
            continue
        if action == 'drop':
            print ('Which item do you wish to drop')
            for i in range(len(stuff)):
                print(str(i +1) + '. ' + stuff[i])
            which_item = input('> ').lower().strip()
            try:
                num = int(which_item) - 1
                here['items'].append(stuff.pop(i))
            except:
                print("I do not understand '{}' ...".format(which_items))
            continue
    
        # TODO: if they type "stuff", print any items they have (check the stuff list!)
        # TODO: if they type "take", grab any items in the room.
    
        # TODO: if they type "search", or "find", look through any exits in the room that might be hidden, and make them not hidden anymore!
        if action in ['search', 'find']:
            print('Searching for exits...')
            for e in here['exits']:
                e['hidden'] = False
            continue
        # Try to turn their action into an exit, by number.
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            if 'required_key' in selected:
                if selected ['required_key'] not in stuff:
                    print('You try to open the door, but it is locked!')
                    continue
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
        
    print("")
    print("")
    endtime = time.time()
    elapsedtime = endtime-starttime
    print("It took you "+str(int(elapsedtime//60))+ " minutes and "+str(int(elapsedtime%60))+ " seconds to escape!")
    print("=== GAME OVER ===")

def find_usable_exits(room, stuff):
    """
    Given a room, and the player's stuff, find a list of exits that they can use right now.
    That means the exits must not be hidden, and if they require a key, the player has it.

    RETURNS
     - a list of exits that are visible (not hidden) and don't require a key!
    """
    usable = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
#         if "required_key" in exit:
#             if exit["required_key"] in stuff:
#                 usable.append(exit)
            continue
        usable.append(exit)
    return usable
def check_all_exits(rooms):
    for r in rooms:
        if r=='__metadata__':
            continue
        for i in rooms[r]['exits']:
            if i['destination'] not in rooms:
                return False
    return True

def print_instructions():
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'search' to take a deeper look at a room.")
    print(" - Type 'help' to print these instructions again")
    print("=== Instructions ===")
    print("")

if __name__ == '__main__':
    main()
