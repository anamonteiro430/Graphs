from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"

#map_file = "adventure/maps/test_cross.txt"    
#map_file = "adventure/maps/test_loop.txt"     ✔✔✔✔
#map_file = "adventure/maps/test_loop_fork.txt" 
map_file = "adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

#print("IS THIS REAL WORLD ????", room_graph)

# Print an ASCII map
#world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#print("TYPE", type(room_graph[0][1]))
#print("LENGTH OF ROOM GRAPH", len(room_graph))

###########################################

def traversal_adv():

    stack = []
    visited = []
    backtrack = []
    world_map = {}
    #print(room_graph)
    #print("first", player.current_room.id)

    #find and stack first room
    first = player.current_room.id
    stack.append(first)
    
    #Pop value and set it to current   --- keep track of current
    #Visit it if it's not visited   
    #Get exits
    #Populate world with exits ---> current : {n:"?" ...}
    #Choose an exit, first key with value == "?"
    #Travel to next room through that exit -- "n"
    #Create logic to discover the opposite of exit
    #Update path with exit coordinate
    #Update world ----> current: {n: 1}
    #Create next entry for the "next room", where we are now
    #world : {0:{n:1...}, 1:{s:0}}     n is the exit and s is the opposite

    #append "next room" to stack
    #begin loop again

    
    #print("first world", world_map)
    
    while len(visited) != len(room_graph):
        found = "nothing"
        #print("found is", found)
    
        #Pop it and set it to current
        current = stack.pop()
        #print("current room is", current)

        #Explore exits
        exits = player.current_room.get_exits()
        #print("exits from room", current , exits)
    
        #check if it's visited 
        if current not in visited:
            visited.append(current)
            #print("visited", visited)

        #always add to backtrack list the rooms
        backtrack.append(current)
        #print("my backtrack is", backtrack)

        #Add entry
        if current not in world_map:    
            world_map[current] = {i[1]: "?" for i in enumerate(exits)}
          
        #print("my world_map", world_map)
        
        

        #pick first exit with value of "?"from world
        for item in world_map[current].items():
            #print("items IS", item)

            if item[1] == '?':
                found = "found"
                exit = item[0]
                #print("there one ?", exit)
                #logic to discover opposite
                if exit == "n" :
                    opposite = "s"
                if exit == "s" :
                    opposite = "n"
                if exit == "e" :
                    opposite = "w"
                if exit == "w" :
                    opposite = "e"
                break

        if found == "found":
            pass

        else:
            
            #print("NO QUESTION MARKS")
            #print("BACKTRACK", backtrack)
            
            #no questions marks, backtrack
            value = backtrack.pop() #gives me the current room
            before = backtrack.pop()
            #print("value is ", value, "and before is ", before)

            for key in world_map[value]:
                #print("whats my key", key)
                if world_map[value][key] == before:
                    exit = key
            
            #print("this is the exit", exit)
            
            
            #exit = exits[0]
            #print("these are the exits", exits)
            #print("random choice is", exit)
            

        #logic to discover opposite
        if exit == "n" :
            opposite = "s"
        if exit == "s" :
            opposite = "n"
        if exit == "e" :
            opposite = "w"
        if exit == "w" :
            opposite = "e"
        
        #print("breaking")
        #print("exit is", exit)

        #travel
        #print("current room is", current)
        player.travel(exit)
        next_room = player.current_room.id
        #print("about to travel from room ", current, exit, "to", next_room)

        #update my exits
        exits = player.current_room.get_exits()
        #print("new exits", exits)

        #print("exit was ", exit)
        #print("opposite is", opposite)

        #add coordinate to path  
        traversal_path.append(exit)
        #print("path", traversal_path)

        #update current entry in map
        
        if world_map[current][exit] != '?':
            pass
            #print("do nothing")
        else:
            world_map[current].update({exit:next_room})
        
        #add next entry to my map 
        #get exits
        #exits = player.current_room.get_exits()
        #print("exits from room", next_room , exits)

        #Add entry
        if next_room in world_map:
            pass
            #print(next_room, "  already in world") 
        else:
            world_map[next_room] = {i[1]: "?" for i in enumerate(exits)}

        #print("whats this", world_map[next_room][opposite])
        if  world_map[next_room][opposite] is True and world_map[next_room][opposite] != "?":
            pass
            #print("DONT UPDATE WORLD")
        else:
            #print("UPDATING")
            world_map[next_room].update({opposite:current})
        #print("my world_map", world_map)

        #Add next_room to stack to explore in next iteration
        stack.append(next_room)


        #print("world now", world_map)

        
            


            
        







    #print("random direction", random_dir)
    #player.travel(random_dir)

    
        #next_room = player.current_room.get_exits()      
        #world_map[current_room] = next_room
  


    #while len(stack) > 0:
        
        




    #values = list(room_graph.values())



    ''' tests = []
    for i in range(len(values)):
        tests.append(values[i][1])

    world_map = { i : tests[i] for i in range(0, len(tests) ) }

    for i in tests:
        for j in i:
            i[j] = "?"
    print("WORLD MAP", world_map) '''
    

            

        









#######
# UNCOMMENT TO WALK AROUND
#######
'''  player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.") ''' 


traversal_adv()
print("LENGTH traversal_path = ", len(traversal_path) )


#TRAVERSAL TEST
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