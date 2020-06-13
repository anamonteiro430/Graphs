#######################################################################
    #print("traversal path right now", traversal_path)
    print("current room is ", player.current_room.id)
    #keep track of visited node, has to be len of 500
    visited = []
    stack = []
    count = 0
    directions = ["n", "e", "s", "w"]
    direction = directions[count]
    
    prev_room = player.current_room.id
    stack.append(player.current_room.id)
    
    #while len(visited) != len(world_map):
    for i in range(30):
        print("LEN VISITED", len(visited))
        print("LEN WORLD", len(world_map))
        
        
        print("enter main loop")
        print("MAIN DIRECTION", direction)
        room = stack.pop()
        print("room is", room)

        #check if it's on visited
        if room not in visited:
            print("visiting room ", room)
            visited.append(room)
        print("visited", visited)
       
       
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
        print("current", player.current_room.id)
        
        if proom != player.current_room.id: 
                
            print("different rooms, update map")
            
            

        #Loop until player can move
        while proom == player.current_room.id:
            count += 1
            print("in the same room")
            if count > 3:
                print("count is too high, resetting")
                count = 0
            else:
                
                print("count is cool")
            print("COUNT", count)
            direction = directions[count]
            print("direction is ", direction)
            player.travel(direction)
            if direction == "n":
                opposite = "s"
            if direction == "s":
                opposite = "n"
            if direction == "e":
                opposite = "w"
            if direction == "w":
                opposite = "e"
            
        
            

        world_map[proom][direction] = player.current_room.id
        world_map[player.current_room.id][opposite] = proom
        print("out of the loop!!")
        print("map now", world_map)
        print("now in room", player.current_room.id)

        stack.append(player.current_room.id)
        traversal_path.append(direction)
        print("traversal_path", traversal_path)