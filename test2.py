__author__ = 'yibeihuang'
a = {'A': ['B', 'C'],
     'B': ['C', 'E', 'G'],
     'C': ['A', 'F'],
     'D': ['C', 'J'],
     'F': ['B', 'H'],
     'G': ['C', 'D'],
     'H': ['A', 'B', 'F', 'I'],
     'I': ['B']
     }
path = {}
def search(start, dest, visited): #search all path from given to dest
    visited.append(start)
    result = []
    for ele in a[start]:
        if ele in visited:
            continue
        if ele == dest:
            result.append([start, dest])
        #elif ele in path:
        #    for sub in path[ele]:
        #        result.append([start] + sub)
        else:
            if ele in a:
                for sub in search(ele, dest, visited):
                    result.append([start] + sub)
    #path[start] = result
    del visited[-1]
    return result

print search('A','J',[])