from collections import defaultdict 


ancestors = ([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)])
starting_node = 10

def earliest_ancestor(ancestors, starting_node):
    #create dict with sets as values
    vertices = defaultdict(set)
    #stack to hold my values and top the loop in depth order
    stack = []
    #list to keep track of nodes visited 
    visited = []
    #list keeping all possible paths from the starting node until it reaches a dead end
    paths = []
    #it's going to be the list inside paths with more elements so that in case I have multiple paths I can easily see what's the oldest ancestor(the [-1] of the list with more elements)
    longest = int
    

    #build graph - populate vertices
    #build it in a reverse order so it's easier to traverse later
    for a,b in ancestors:        
        vertices[b].add(a)
    #append the starting node in stack as a list to keep track of paths
    stack.append([starting_node])
    
    #while stack is not empty
    while len(stack) > 0:
        #is going to pop a list, keep track
        path = stack.pop()
        
        if path[-1] not in visited: #if the last element in that list is not in visited array
            visited.append(path[-1]) #visit it
            #if that number is in the keys of vertices
            if path[-1] in vertices.keys():
                #check it's neighbors
                for n in vertices[path[-1]]:
                    #create copy of the previous path
                    new_path = list(path)
                    #append the neighbor
                    new_path.append(n)
                    #and append the new path to stack
                    stack.append(new_path)
            else: #if it's not one of the keys it means it's a dead end, no ancestors prior it
                #append that current path to list os possible paths
                paths.append(path)
    
    #after paths list is populated with all possible paths

    #if there's a list with just one element in paths array return -1 because there's no ancestors
    if len(paths[-1]) == 1:
        return -1
        
    if len(paths) == 1: #if there's only one list inside paths, no need to compare there is just one possible path 
        ancestor = paths[0][-1] #so check out the last element of list that's the ancestor
        return ancestor

    else: #for cases where arrays have different lengths, I have to figure out the longest list
        for a in range(len(paths) - 1): #iterate over index of arrays in paths list
            
            if len(paths[a]) < len(paths[a+1]):  #compare lengths of each one. If the length of the first is smaller that the second
                longest = paths[a+1]  #the longest array is the second
                ancestor = longest[-1]  #therefore the ancestor is the last element of that list
                
            else: #if it continues to be the longest
                longest = paths[a] 
                ancestor = longest[-1] #ancestor is last elem of that list
            
        return ancestor  #return it for both cases and to stop loop 

    for b in range(len(longest) -1): #for cases where arrays have all the same length, we want the ancestor with lowest number
        if longest[b][-1] < longest[b+1][-1]:   #compare last elements of lists
            ancestor = longest[b][-1]
        else:
            ancestor = longest[b+1][-1]
        return ancestor   #return it

    


print(earliest_ancestor(ancestors, starting_node))