class Stack():
    """(LIFO) queuing policy implemented using python list."""
    def __init__(self) -> None:
        self.list=[]

    def push(self, item):
        """Push 'item' onto the stack."""
        self.list.append(item)

    def pop(self):
        """Pop the most recently pushed item from the stack."""
        return self.list.pop()

    def top(self):
        """Return the last element."""
        return self.list[-1]

    def is_empty(self):
        """Returns true if the stack is empty."""
        return len(self.list) == 0

class Queue():
    def __init__(self) -> None:
        self.list=[]
        self.rare=0
    def enqueue(self,val):
        self.list.append(val)
        self.rare += 1

    def dequeue(self):
        if(self.rare != 0):
            return self.list.pop(0)

    def isEmpty(self):
        if(self.rare == 0):
            print("Queue is Empty...")
        else:
            print("Queue is not Empty...")

    def traverse(self):
        for i in range(self.rare):
            print(self.list[i])

def depth_first_search(graph, start):
    stack = Stack()
    stack.push(start)
    path = []

    while not stack.is_empty():
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.push(neighbor)

    return path

visited = [] # List for visited nodes.
queue = Queue()     #Initialize a queue
def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.enqueue(node)

  while queue.list:          # Creating loop to visit each node
    m = queue.dequeue()
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.enqueue(neighbour)

def main():
    graph1 = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: [7],
        7: []
    }
    graph2 = {
        '5' : ['3','7'],
        '3' : ['2', '4'],
        '7' : ['8'],
        '2' : [],
        '4' : ['8'],
        '8' : []
    }
    # Driver Code
    print("Following is the Breadth-First Search")
    bfs(visited, graph2, '5')

    print("\nFollowing is the Depth-First Search")
    dfs_path = depth_first_search(graph1, 1)
    print(dfs_path)

main()




