__author__ = 'yibeihuang'
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        queue, wordmap, worddist = [(1,beginWord)], dict(), dict()
        visited = set([beginWord])
        ladder = False
        flag = 0
        while queue:
            length, word=queue.pop(0)
            wordmap[word], worddist[word]=[],length
            if word==endWord:
                ladder=True
                continue
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i]+j+word[i+1:]
                    # if tmp in wordlist and tmp not in visited and flag==0:
                    #     if tmp!=endWord:visited.add(tmp)
                    #     else: flag=1
                    #     wordmap[word].append(tmp)
                    #     queue.append((length+1,tmp))
                    # elif tmp in wordlist and tmp not in visited and flag==1:
                    #     if tmp!=endWord:
                    #         visited.add(tmp)
                    #         queue.append((length+1,tmp))
                    #     wordmap[word].append(tmp)
                    if tmp in wordlist:
                        wordmap[word].append(tmp)
                        if tmp not in visited:
                            queue.append((length+1,tmp))
                            visited.add(tmp)

        rst = []
        if ladder == False: return rst
        return self.dfs(beginWord, endWord, wordmap, worddist, 1, [], rst)

    def dfs(self, begin, end, wordmap, worddist, length, tmp, rst):
        tmp.append(begin)
        if begin==end: return rst.append(tmp[:])
        for word in wordmap[begin]:
            if worddist[word]==length+1:
                self.dfs(word, end, wordmap, worddist, length+1, tmp, rst)
                tmp.pop()
        return rst


sol = Solution()
begin = 'red'
end = 'tax'
wordList=['red','tax','ted','tad','tex','rex']
rst = sol.findLadders(begin,end,wordList)
print(rst)