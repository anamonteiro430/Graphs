from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"

#map_file = "projects/adventure/maps/test_cross.txt"
map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt" """

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

#print("IS THIS REAL WORLD ????", room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#print("TYPE", type(room_graph[0][1]))
#print("LENGTH OF ROOM GRAPH", len(room_graph))

###########################################

def dir():
    ''' directions = ["n", "s", "e", "w"]

    print("inside fn")
    #direction is 1st elem in directions 
    direction = directions[0]
    if direction == "n":
        opposite = "s"
    if direction == "s":
        opposite = "n"
    if direction == "e":
        opposite = "w"
    if direction == "w":
        opposite = "e"
    if player.travel(direction) is None:
        for i in directions:
            if player.travel(i) is not None:
                print("whats this")
        print("work") '''

    




def traversal_adv():
    
    ''' keys = room_graph.keys()
    for i in keys:
        world_map[i] = {} '''

    values = list(room_graph.values())

    ''' for key in world_map:
        print("Key in mine", key)
        print("Value in Mine", world_map[key])

        for key in room_graph:
        #if set not necessary take the set out to switch to dict of dicts
        #world_map[key] = "value[1]"
            #world_map[key] = room_graph
            print("key in world", key)
            print("value in world", room_graph[key][1]) '''

    #world_map[key] = room_graph[key][1]
    
    ''' for i in values:
        print("yo", i[1])

    for key in world_map:
        for i in values:
            print(i)
        world_map[key] = i[0] '''

    tests = []
    for i in range(len(values)):
        tests.append(values[i][1])

    world_map = { i : tests[i] for i in range(0, len(tests) ) }

    for i in tests:
        for j in i:
            i[j] = "?"

    print("WORLD MAP", world_map)
    #######################################################################
    #print("traversal path right now", traversal_path)
    print("current room is ", player.current_room.id)
    #keep track of visited node, has to be len of 500
    visited = []
    stack = []
    path = []
    directions = ["n", "e", "s", "w"]
    direction = "n"
    count = 0
    
    prev_room = player.current_room.id
    stack.append(player.current_room.id)
    
    #while loop until
    for i in range(9):
        print("enter main loop")
        print("MAIN DIRECTION", direction)
        room = stack.pop()
        print("room is", room)

        #check if it's on visited
        if room not in visited:
            print("visiting room ", room)
            visited.append(room)
        print("visited", visited)
        #move to north
        #check room
        #if im still in the same room
        #move to south
        #loop over list try to move to n ,
        if direction == "n":
            opposite = "s"
        if direction == "s":
            opposite = "n"
        if direction == "e":
            opposite = "w"
        if direction == "w":
            opposite = "e" 
        proom = player.current_room.id
        print("prev room is ", proom)
        print("travelinnggg", direction)
        player.travel(direction)
        
        
        if proom != player.current_room.id: 
            print("different rooms, update map")
            world_map[proom][direction] = player.current_room.id
            world_map[player.current_room.id][opposite] = proom
            path.append(direction)
            print("update path", path)
        else:
            print("ENter")
            yo = directions[count]
            print("YO", yo)

            #for i in directions:
            print("directions now", directions)
            
            player.travel(yo)
            direction = yo
            print(direction)
            print("current", player.current_room.id)

            if proom != player.current_room.id:
                #we changed rooms
                print("changing rooms")
                #update path
                count += 1
                print("count now")
                print("direction is", direction)
                if direction == "n":
                    opposite = "s"
                if direction == "s":
                    opposite = "n"
                if direction == "e":
                    opposite = "w"
                if direction == "w":
                    opposite = "e"
                path.append(direction)
                print("Paths is", path)
                world_map[proom][direction] = player.current_room.id
                world_map[player.current_room.id][opposite] = proom
                print("check world", world_map)
                break
            else: #if we hit a wall
                #v = directions.pop(0) #take out first elem in directions and put in on last
                #directions.append(v)
                #print("directions should be [eswn] ", directions)
                print("trying again, i should be e")

            print("out of LOOP")
        
        

        #update path
        #path.append(direction)
        ##update map
        

        print("map now", world_map)
        print("now in room", player.current_room.id)

        stack.append(player.current_room.id)
        print("path", path)

    

    ''' while len(visited) < 5:
        print(stack)
        print(len(world_map))
        value = stack.pop()
        print("value", value)
        if value not in visited:
            visited.append(value)
        
        
        print("current room exits are ", player.current_room.get_exits())
        exits = player.current_room.get_exits()  
        #Directions
        direction = random.choice(exits)
        def dir(direction):
            for n in exits:
                if world_map[value][direction] == "?" 



                
        alt_direction = exits[0]
        print("direction is", direction)
        if world_map[value][direction] == "?":
                

            if direction == "n":
                opposite = "s"
            if direction == "s":
                opposite = "n"
            if direction == "e":
                opposite = "w"
            if direction == "w":
                opposite = "e"
        else:
            direction = alt_direction
            if direction == "n":
                opposite = "s"
            if direction == "s":
                opposite = "n"
            if direction == "e":
                opposite = "w"
            if direction == "w":
                opposite = "e"
            
        
        
        #travel to next room
        player.travel(direction)
        print("travel to room", player.current_room.id)
        #update map
        world_map[value][direction] = player.current_room.id
        world_map[player.current_room.id][opposite] = value
        print("world", world_map)
        stack.append(player.current_room.id)
        print("vis", visited, "stack", stack, "path", path) 


    
    room = player.current_room.id
    print("start in room ", room)
    #put in in stack
    stack.append(room)
    print("stack", stack)
    #visit room
    
    while len(stack) > 0:
        
        
        value = stack.pop() #tira do stack
        if value not in visited:  #first is room 0
            visited.append(room) # put in visited
            print("VISITED, ", visited)

        for i in world_map:
            if "?" in world_map[i].values():
                print("yup")
                

                
        for i in list(world_map.values()):
        for j in i:
            if str(i[j]) not in '?':
                print(path)
            return path     
            
                

                print("direction", direction)
                print("opposite", opposite)
                print("stack", stack)
                #print("this should be next room", player.current_room.id)
                
                #update map in both directions
                print("whats room previous", room)
                

                print("now my room is ", player.current_room.id)
                print("WORLD UPDATED", world_map)
                path.append(direction)
                print("PATH", path)
                #append current room to stack
                room = player.current_room.id
                print("NECT ROOM", room)
                stack.append(room)
                print("STACK", stack)
            else:
                print("NO", world_map[i].values())
                return
            

        





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
 player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.") '''


traversal_adv()
