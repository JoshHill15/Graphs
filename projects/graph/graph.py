"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex doesn't exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            current_vertex = q.dequeue()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for next_vertex in self.get_neighbors(current_vertex):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for next_vertex in self.get_neighbors(current_vertex):
                    stack.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for next_vert in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            current_vertex = path[-1]
            if current_vertex not in visited:
                visited.add(current_vertex)
                for next_vert in self.get_neighbors(current_vertex):
                    new_path = path.copy()
                    new_path.append(next_vert)
                    q.enqueue(new_path)
                    if next_vert == destination_vertex:
                        return new_path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            return None

        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        path = []
        while stack.size() > 0:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                path.append(current)

            if current == destination_vertex:
                return path

            for next_v in self.get_neighbors(current):
                stack.push(next_v)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        paths = []
        visited = set()

        def helper(current, destination, current_path=None):
            if current_path == None:
                current_path = []
            visited.add(current)
            current_path.append(current)
            if current == destination:
                paths.append(current_path)

            for next_vert in self.get_neighbors(current):
                if next_vert not in visited:
                    helper(next_vert, destination, current_path.copy())

        helper(starting_vertex, destination_vertex)
        return paths[0]

    def beej_dfs(self, start_vert, target, visited=None, path=None):
        if visited is None:
            visited = set()

        if path is None:
            path = []
        # MAKE COPY
        path = path.copy()
        path.append(start_vert)
        # BASE CASE
        if start_vert == target:
            return path
        visited.add(start_vert)
        for next_vert in self.get_neighbors(start_vert):
            if next_vert not in visited:
                new_path = self.beej_dfs(next_vert, target, visited, path)

                if new_path:
                    return new_path

        return None


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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7 => my bft
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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7 => my recursive dft
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5 => my dft
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6] 
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6] => my recursive dft
        [1, 2, 4, 7, 6] => my dft
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
    print(graph.beej_dfs(1, 6))
