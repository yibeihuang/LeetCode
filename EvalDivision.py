__author__ = 'yibeihuang'
import collections
def calcEquation(equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        words = collections.defaultdict(dict)
        for (num, den),val in zip(equations, values):
            words[num][den]=val
            words[den][num]=1/val
        for k in words:
            for i in words[k]:
                for j in words[k]:
                        words[i][j]=words[i][k]*words[k][j]
        res = []
        for i,j in queries:
            if i==j:res.append(1.0)
            elif i in words and j in words[i]: res.append(words[i][j])
            else: res.append(-1.0)
        return res

euq = [ ["a","b"],["b","c"] ]
val = [2.0,3.0]
qur = [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]
print(calcEquation(euq,val,qur))