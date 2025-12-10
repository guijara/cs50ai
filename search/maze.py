

class Node():
    def __init__(self,state,action,parent):
        self.state = state
        self.action = action
        self.parent = parent
        
class StackFrontier():
    def __init__(self):
        self.frontier = []
        
    def add(self, node):
        self.frontier.append(node)
        
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove (self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        
class QueueFrontier(StackFrontier):
    
    def remove(self):
        if self.empty():
            raise Exception("frontier is empty")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
class solve():
    
    num = 0
    
    start = Node(state=self.start, action=none, parent=none)
    frontier = StackFrontier
    frontier.add(start)
    
    vis = set()
    
    node = frontier.remove()
    vis.add(node)
    num += 1
    
    
    
                
    