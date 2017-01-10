__author__ = 'yibeihuang'
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        even = 0
        odd = 1
        rst  = ''
        while even<len(strs) and odd<len(strs):
            rst += strs[odd]
            rst += ','
            rst += strs[even]
            odd += 2
            even +=2
        if even<len(strs):rst+=strs[even]
        elif odd<len(strs): rst+=strs[odd]
        return rst

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        lststr = s.split(',')
        if s=='': return []
        rst = []
        for i in range(len(lststr)):
            rst.append(lststr[i])
        return rst

strs = []
codec = Codec();
print codec.decode(codec.encode(strs))