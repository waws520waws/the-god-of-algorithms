class Fraction(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        x = self.gcd2(a,b)
        self.a /= x
        self.b /= x


    @staticmethod
    def gcd2(a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def zgs(self,a,b):
        s = self.gcd2(a,b)
        m = a/s
        n = b/s
        return m*n*s

    def __add__(self, other):
        # 1/12 +1/20
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgs(b,d)
        fenzi = a*(fenmu/b) +c* fenmu/d
        return Fraction(fenzi,fenmu)

    def __str__(self):
       return "%d/%d"%(self.a,self.b)

f1 = Fraction(1,3)
f2 = Fraction(1,2)
print(f1+f2)
