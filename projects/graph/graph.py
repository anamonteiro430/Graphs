"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        """ '0': {'1', '3'},
        '1': {'0'},
        '2': set(),
        '3': {'0'} """

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph. 
        """
        self.vertices[vertex_id] = set()

        return vertex_id

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph. One-way from v1 to v2
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        neighbors = self.vertices[vertex_id]
        return neighbors

    def bft(self, starting_vertex): #✔
        #use queue for BFT
        queue = Queue()
        visited = set()
        #enqueue first vert
        queue.enqueue(starting_vertex)
        
        #loop while queue is not empty:
        while queue.size() != 0:
            
            #keep track of the current, when it enqueue it pops the value at index 0 and returns that value. That's the current
            current = queue.dequeue()
            print(current)  #visit it
            if current not in visited: #if we haven't visited them yet
                visited.add(current) #add it to visited, no need to check if it's already there because it's a set, unique values only        

                #check the neighbors of current
                for n in self.get_neighbors(current):
                    if n not in visited and n not in queue.queue:
                        queue.enqueue(n) #enqueue it to our queue to check it
        
    def dft(self, starting_vertex): #✔
        #use stack for DFT
        stack = Stack()
        #keep track of visited
        visited = set()

        #add to stack the starting vertex
        
        stack.push(starting_vertex)

        while stack.size() != 0:
            current = stack.pop()
            print(current)
            visited.add(current)

            for n in self.get_neighbors(current):
                if n not in visited and n not in stack.stack: #if we haven't visited them yet
                    stack.push(n) #enqueue it to our queue to check it

    def dft_recursive(self, starting_vertex, visited=None, stack=None):
        #Initial Case
        if visited is None: #keep track of visited
            visited = set()    
        
        if stack is None:
            stack = list()


        stack.append(starting_vertex)

        if len(stack) == 0:
            return visited
        
        _next = stack.pop()
        print(_next)
        visited.add(_next)

        for n in self.get_neighbors(_next):
            if n not in visited and n not in stack:
                self.dft_recursive(n, visited, stack)

    def bfs(self, starting_vertex, destination_vertex):
             #use queue for BFT
        queue = Queue()
        visited = set()
        #enqueue first vert
        queue.enqueue([starting_vertex])
        
        #loop while queue is not empty:
        while queue.size() != 0:
            
            #keep track of the current, when it enqueue it pops the value at index 0 and returns that value. That's the current
            path = queue.dequeue()

            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                   
                visited.add(path[-1]) #add it to visited, no need to check if it's already there because it's a set, unique values only        

                #check the neighbors of current
                for n in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(n)
                    queue.enqueue(new_path)
                    

    def dfs(self, starting_vertex, destination_vertex):
        #use stack for DFT
        stack = Stack()
        #keep track of visited
        visited = set()

        #add to stack the starting vertex
        
        stack.push([starting_vertex])

        while stack.size() != 0:
            path = stack.pop()
            print(path)

            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path

                visited.add(path[-1])

                for n in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(n)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        #Initial Case
        if visited is None: #keep track of visited
            visited = set()    
        
        if path is None:
            path = list()


        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                n_path = self.dfs_recursive(n, destination_vertex, visited, path)
                if n_path:
                    return n_path
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    print("Neighbors of 7", graph.get_neighbors(7))

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
