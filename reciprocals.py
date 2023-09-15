

def prod(l):
    res = 1
    for num in l:
        res *= num
    return res

class Reciprocal:
    def __init__(self, d=1, n=False, base=10):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n == False:
            self.n = d
            self.d = 1
        else:
            self.d = d
            self.n = n
        self.given = True
        self.base = base
        self.digits, self.period = self.compute(self.d, self.n, self.base)

    
    def __mul__(self,other):
        return Reciprocal(other*self.d, self.n, self.base)
        
    def __truediv__(self,other):
        return Reciprocal(self.n*other)

    def __str__(self):
        number = "0."
        for d in self.digits:
            if d >= 10:
                if d < 62:
                    number += self.alphabet[d-10]
                else:
                    number += f"[{str(d)}]"
            else:
                number += str(d)
        number += "("
        for p in self.period:
            if p >= 10:
                if p < 62:
                    number += self.alphabet[p-10]
                else:
                    number += f"[{str(p)}]"
            else:
                number += str(p)
        number += ")"
        return number

    def set_dp(self, digits, period):
        self.digits, self.period, self.given = digits, period, False
        
    def compute(self, d, n, base=10):
        end = False
        digit = d % n
        digits = []
        remainders = [digit]
        rdic = {}
        while end==False:
            digits.append(base*digit//n)
            r = base*digit%n
            if r in rdic.keys():
                end=True
            else:
                rdic[digit] = r
                digit = r
                remainders.append(r)
        period = [0]
        for i in range(len(remainders)):
            if remainders[i] == r:
                period = digits[i:]
                break
        if len(period) == 2 and len(set(period)) == 1:
            period.pop(1)
        return digits[:i], period

    def find_dn(self):
        if self.given:
            return self.d, self.n
        b = self.base
        dig_num, prd_num = 0,0
        for i,d in enumerate(self.digits):
            dig_num += d*b**(len(self.digits)-i-1)
        for j,p in enumerate(self.period):
            prd_num += p*b**(len(self.period)-j-1)
        prd_denom = b**len(self.digits)*(b**len(self.period)-1)
        num = dig_num*(b**len(self.period)-1) + prd_num
        # common_factors = gcd(num, prd_denom)
        # self.d, self.n = int(num/common_factors), int(prd_denom/common_factors)
        # not viable because division of large values often changes base value
        self.d, self.n = num, prd_denom
        return self.d, self.n



