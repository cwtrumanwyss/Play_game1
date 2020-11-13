import json
import os

def main():
    print("Select a game file to see if it is a winnable game!")
    json_files = []
    for file in os.listdir():
        if file[-5:] == '.json':
            json_files.append(file)
    if len(json_files) == 0:
        print("No adventure files found!")
        return
    print("Which game needs to be checked?")
    for i in range(len(json_files)):
        print(str(i+1)+'. '+json_files[i])
    file_number = input("> ").lower().strip()
    try:
        num = int(file_number) - 1
        file_name = json_files[num]
    except:
        print("I don't understand '{}' ...".format(file_number))
        return
    with open(file_name) as fp:
        game = json.load(fp)
    print("Checking game '{}'".format(game['__metadata__']['title']))
    print("")
    check(game)

def check(rooms):
    if not check_all_exits(rooms):
        print("These exits won't take you anywhere!")
        
        current_place = rooms['__metadata__']['start']
        
        here = rooms[current_place]
        if check_for_exits(rooms,here):
            print('There is an exit!')
        else:
            print('There is no exit!')
            
def check_for_exits(rooms, room, visited=[]):
    if room.get('ends_game', False):
        return True
    for i in room.get('exits',[]):
        if i['destination'] not in visited:
            new_visited = visited.copy()
            new_visited.append(room['name'])
            if check_for_exits(rooms,rooms[i['destination']],new_visited):
                return True
    return False

def check_all(rooms):
    for i in rooms:
        if i=='__metadata__':
            continue
        for r in rooms[i]['exits']:
            if r['destination'] not in rooms:
                return False
    return True

if __name__ == '__main__':
    main()