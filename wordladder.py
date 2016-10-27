__author__ = 'yibeihuang'
def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    # tmp = d.get(s, []) dict.get(key, default=None),
                    # default is the Value to be returned in case key does not exist.
                    d[s] = d.get(s, []) + [word]
            return d

def ladderLength(beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue, visited = [(beginWord,1)], set(beginWord)
        while queue:
            word, length = queue.pop(0)
            if word==endWord: return length
            for j in range(len(word)):
                for i in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:j]+i+word[j+1:]
                    if tmp not in visited and tmp in wordList:
                        queue.append((tmp,length+1))
                        visited.add(tmp)
        return 0

word_list=["a","b","c"]
print(ladderLength("a","c",word_list))