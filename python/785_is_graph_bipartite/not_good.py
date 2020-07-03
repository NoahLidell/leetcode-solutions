class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        later = deque()
        a = set()
        b = set()
        
        for i, nodes in enumerate(graph):
            if i not in a and i not in b:
                if nodes == []:
                    a.add(i)
                if not set(nodes).intersection(a) and not set(nodes).intersection(b) and i != 0:
                    later.append((i, nodes))
                    continue
                    
                for j in nodes:
                    if j in a :
                        b.add(i)
                        a = a.union(set(nodes))
                    else:
                        a.add(i)
                        b = b.union(set(nodes))
            elif i in a:
                for j in nodes:
                    b.add(j)
            elif i in b:
                for j in nodes:
                    a.add(j)
        while later:
            try:
                i, nodes = later.popleft()
            except IndexError:
                break
            if i not in a and i not in b:
                if not set(nodes).intersection(a) and not set(nodes).intersection(b):
                    
                    later.append((i, nodes))
                    a.add(i)
                    continue
                    
                for j in nodes:
                    if j in a :
                        b.add(i)
                        a = a.union(set(nodes))
                    else:
                        a.add(i)
                        b = b.union(set(nodes))
            elif i in a:
                for j in nodes:
                    b.add(j)
            elif i in b:
                for j in nodes:
                    a.add(j)

        if len(a) == len(a-b):
            return True
        else:
            return False
