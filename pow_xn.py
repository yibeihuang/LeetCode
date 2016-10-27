__author__ = 'yibeihuang'
def myPow( x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x, n =1/x, -n
            return self.myPow(x,n)
        while n//2 > 0:
            if n%2==0:
                n=n//2
                x = x*x
            elif n%2==1:
                n=n//2
                x = x*x*x
        return x

x, n= 3.8, 3
print(myPow(x,n))