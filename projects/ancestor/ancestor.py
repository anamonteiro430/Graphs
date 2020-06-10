from collections import defaultdict 


ancestors = ([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)])
starting_node = 10

def earliest_ancestor(ancestors, starting_node):
    vertices = defaultdict(set)
    stack = []
    visited = []
    paths = []
    longest = int
    

    #build graph
    for a,b in ancestors:        
        vertices[b].add(a)
    
    stack.append([starting_node])
    

    while len(stack) > 0:
        path = stack.pop()
        
        if path[-1] not in visited:
            visited.append(path[-1])

            if path[-1] in vertices.keys():
                for n in vertices[path[-1]]:
                    new_path = list(path)
                    new_path.append(n)
                    stack.append(new_path)
            else: 
                paths.append(path)
        
    if len(paths[-1]) == 1:
        return -1
        
    if len(paths) == 1:
        ancestor = paths[0][-1]
        return ancestor

    else:
        for a in range(len(paths) - 1):
            
            if len(paths[a]) < len(paths[a+1]):
                longest = paths[a+1]
                ancestor = longest[-1]
                
            else:
                longest = paths[a]
                ancestor = longest[-1]
            
        return ancestor   

    for b in range(len(longest) -1):
        if longest[b][-1] < longest[b+1][-1]:
            ancestor = longest[b][-1]
        else:
            ancestor = longest[b+1][-1]
        return ancestor

    ancestor = longest[-1]
    return ancestor


print(earliest_ancestor(ancestors, starting_node))