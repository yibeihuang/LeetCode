__author__ = 'yibeihuang'
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {}
        for i in dictionary:
            num = len(i)-2
            if num>0: keyi = i[0]+str(num)+i[-1]
            else: keyi = i
            if keyi in self.dic:
                self.dic[keyi].append(i)
            else:
                self.dic[keyi] = [i]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word)>=2: keyw = word[0]+str(len(word)-2)+word[-1]
        else: keyw = word
        if keyw in self.dic:
            if len(self.dic[keyw])==1 and self.dic[keyw][0]==word:
                return True
            return False
        return True

dictionary = ['dog']
sol = ValidWordAbbr(dictionary)
print(sol.isUnique('dig'))