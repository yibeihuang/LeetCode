__author__ = 'yibeihuang'

class Node(object):
    def __init__(self, name=None):
        self.name = name
        self.children=[]

class Solution(object):
    def buildgraph(self, input):
        inputlist = input.split(',')
        name1 = inputlist[-2]
        name2 = inputlist[-1]
        inputlist = inputlist[:-2]
        self.graph = dict()
        self.roots = dict()
        for p in inputlist:
            p1, p2 = p.split('->')[0],p.split('->')[1]
            if p1 in self.graph:
                if p2 in self.graph:
                    self.graph[p1].children.append(self.graph[p2])
                    if p2 in self.roots: del self.roots[p2]
                else:
                    node = Node(p2)
                    self.graph[p2] = node
                    self.graph[p1].children.append(node)
            else:
                node1 = Node(p1)
                self.graph[p1] = node1
                self.roots[p1] = node1
                if p2 in self.graph:
                    node2 = self.graph[p2]
                    node1.children.append(node2)
                    if p2 in self.roots: del self.roots[p2]
                else:
                    node2 = Node(p2)
                    self.graph[p2] = node2
                    node1.children.append(node2)
        self.person1 = self.graph[name1]
        self.person2 = self.graph[name2]

    def LCA(self, r):
        if r==None or r == self.person1 or r==self.person2:
            return r
        n1, n2 = None, None
        for child in r.children:
            if n1==None:
                n1 = self.LCA(child)
            else:
                n2 = self.LCA(child)
        if n1!=None and n2!=None: return r
        elif n1!=None: return n1
        else: return n2

    def find(self):
        for ele in self.roots:
            manager = self.LCA(self.roots[ele])
            if manager != None:
                return manager.name
        return None

iinput = "Frank->Mary,Mary->Sam,Mary->Bob,Sam->Katie,Sam->Pete,Bob->John,Bob,Katie"
iinput2 = "Sam->Pete,Pete->Nancy,Sam->Katie,Frank->Mary1,Mary1->Sam,Mary1->Bill,Bill->John,Sam,John"
sol = Solution()
sol.buildgraph(iinput2)
manager = sol.find()
print(manager)