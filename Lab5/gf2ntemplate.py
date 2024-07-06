# 50.042 FCS Lab 5 Modular Arithmetic
# Year 2023

import copy
class Polynomial2:
    coeffs= []
    def __init__(self,coeffs):
        self.coeffs=copy.deepcopy(coeffs)

    def add(self,p2):
        p2_coeff = copy.deepcopy(p2.coeffs)
        if len(self.coeffs) < len(p2_coeff):
            self.coeffs = self.coeffs + [0]*(len(p2_coeff)-len(self.coeffs))
        elif len(self.coeffs) > len(p2_coeff):
            p2_coeff = p2_coeff + [0]*(len(self.coeffs)-len(p2_coeff))
        output = []
        for i in range(len(self.coeffs)):
            if self.coeffs[i] +p2_coeff[i] ==1:
                output.append(1)
            else:
                output.append(0)
        return Polynomial2(output)


    def sub(self,p2):
        return self.add(p2)

    def mul(self,p2,modp=None):
        result_coeff = [0]*(len(self.coeffs)+len(p2.coeffs)-1)
        for i,a in enumerate(self.coeffs):
            for j,b in enumerate(p2.coeffs):
                result_coeff[i+j] = (result_coeff[i+j] + a&b)%2
        if modp is not None:
            polynomial = Polynomial2(result_coeff)
            quotient , result = polynomial.div(modp)
            result_coeff = result.coeffs
        return Polynomial2(result_coeff)
    
    def get_degree(self):
        i=0
        while self.coeffs[i] == 0:
            i+=1
        degree = len(self.coeffs)-i-1
        return degree
    
    def div(self,p2):
        self_degree = self.get_degree()
        p2_degree = p2.get_degree()
        if self_degree< p2_degree:
            return Polynomial2([0]), self
        quotient = [0]*(self_degree-p2_degree+1)
        remainder = self.coeffs[:]
        while len(remainder) >= len(p2.coeffs):
            leading_coeff_ind = len(remainder)-1
            diff_degree = leading_coeff_ind - p2_degree
            if remainder[0]==1:
                quotient[-diff_degree-1] =1
                for i in range(len(p2.coeffs)):
                    remainder[i]^=p2.coeffs[i]
            while remainder and remainder[0]==0:
                remainder.pop(0)
        return Polynomial2(quotient), Polynomial2(remainder)
    
    def make_same_length(self,p2):
        p1coeffs = self.coeffs[:]
        p2coeffs = p2.coeffs[:]
        while len(p1coeffs) != len(p2coeffs):
            if len(p1coeffs) > len(p2coeffs):
                p2coeffs.insert(0, 0)
            else:
                p1coeffs.insert(0, 0)
        return p1coeffs, p2coeffs


    def __str__(self):
        terms = []
        for i in range(len(self.coeffs)):
            if self.coeffs[i] != 0:
                terms.append(f"x^{len(self.coeffs) - i - 1}" if i != len(self.coeffs) - 1 else "1")
        return " + ".join(terms) if terms else "0"

    def getInt(self):
        result = 0
        for coeff in self.coeffs:
            result = (result << 1) | coeff
        return result

class GF2N:
    affinemat=[[1,0,0,0,1,1,1,1],
               [1,1,0,0,0,1,1,1],
               [1,1,1,0,0,0,1,1],
               [1,1,1,1,0,0,0,1],
               [1,1,1,1,1,0,0,0],
               [0,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,0],
               [0,0,0,1,1,1,1,1]]

    def __init__(self,x,n=8,ip=Polynomial2([1,1,0,1,1,0,0,0,1])):
        self.power = n
        self.p = ip
        self.x = x
        self.px = self.getPolynomial2()


    def add(self,g2):
        return GF2N(self.getPolynomial2().add(g2.getPolynomial2()).getInt(), ip=self.p)

    def sub(self,g2):
        return self.add(g2)
    
    def mul(self,g2):
        return GF2N(self.px.mul(g2.px, modp=self.p).getInt(), ip=self.p)
    
    def div(self,g2):
        pq, pr = self.px.div(g2.px)
        q = GF2N(pq.getInt(), ip=self.p)
        r = GF2N(pr.getInt(), ip=self.p)
        return q, r

    def getPolynomial2(self):
        return Polynomial2(self.int_to_binary_list(self.x))

    def __str__(self):
        return str(self.getInt())
    
    def getInt(self):
        return self.x

    def mulInv(self):
        r1 = self.p
        r2 = self.px
        t1 = Polynomial2([0])
        t2 = Polynomial2([1])
        while r2.getInt() > 0:
            q, r = r1.div(r2)
            r1, r2 = r2, r
            t1, t2 = t2, t1.add(q.mul(t2))
        return GF2N(t1.getInt(), ip=self.p)


    def affineMap(self):
        output = []
        transformation = [1, 1, 0, 0, 0, 1, 1, 0]
        for i in self.affinemat:
            output.append([a & b for a, b in zip(i, self.p.coeffs)])
        for i in range(len(output)):
            output[i][-1] ^= transformation[i]
        
        # Convert the resulting list back to an integer
        result = 0
        for i in output:
            result = (result << 1) | i[-1]
        
        return GF2N(result, n=self.power, ip=self.p)
    
    def int_to_binary_list(self, x):
        binary_str = bin(x)[2:]  # Convert to binary and remove '0b' prefix
        binary_list = [int(digit) for digit in binary_str]  # Convert each character to an integer
        return binary_list


print('\nTest 1')
print('======')
print('p1=x^5+x^2+x')
print('p2=x^3+x^2+1')
p1=Polynomial2([0,1,1,0,0,1])
p2=Polynomial2([1,0,1,1])
p3=p1.add(p2)
print('p3= p1+p2 = ',p3)

print('\nTest 2')
print('======')
print('p4=x^7+x^4+x^3+x^2+x')
print('modp=x^8+x^7+x^5+x^4+1')
p4 = Polynomial2([0, 1, 1, 1, 1, 0, 0, 1])
# modp = Polynomial2([1, 1, 0, 1, 1, 0, 0, 0, 1])
modp = Polynomial2([1, 0, 0, 0, 1, 1, 0, 1, 1])
p5 = p1.mul(p4, modp)
print('p5=p1*p4 mod (modp)=', p5)

print('\nTest 3')
print('======')
print('p6=x^12+x^7+x^2')
print('p7=x^8+x^4+x^3+x+1')
p6 = Polynomial2([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])    
p7 = Polynomial2([1, 1, 0, 1, 1, 0, 0, 0, 1])
p8q, p8r = p6.div(p7)
print('q for p6/p7=', p8q)
print('r for p6/p7=', p8r)

print('\nTest 4')
print('======')
g1 = GF2N(100)
g2 = GF2N(5)
print('g1 = ', g1.getPolynomial2())
print('g2 = ', g2.getPolynomial2())
g3 = g1.add(g2)
print('g1+g2 = ', g3)

print('\nTest 5')
print('======')
ip = Polynomial2([1, 1, 0, 0, 1])
print('irreducible polynomial', ip)
g4 = GF2N(0b1101, 4, ip)
g5 = GF2N(0b110, 4, ip)
print('g4 = ', g4.getPolynomial2())
print('g5 = ', g5.getPolynomial2())
g6 = g4.mul(g5)
print('g4 x g5 = ', g6.p)

print('\nTest 6')
print('======')
g7 = GF2N(0b1000010000100, 13, None)
g8 = GF2N(0b100011011, 13, None)
print('g7 = ', g7.getPolynomial2())
print('g8 = ', g8.getPolynomial2())
q, r = g7.div(g8)
print('g7/g8 =')
print('q = ', q.getPolynomial2())
print('r = ', r.getPolynomial2())

print('\nTest 7')
print('======')
ip = Polynomial2([1, 1, 0, 0, 1])
print('irreducible polynomial', ip)
g9 = GF2N(0b101, 4, ip)
print('g9 = ', g9.getPolynomial2())
print('inverse of g9 =', g9.mulInv().getPolynomial2())

print('\nTest 8')
print('======')
ip = Polynomial2([1, 1, 0, 1, 1, 0, 0, 0, 1])
print('irreducible polynomial', ip)
g10 = GF2N(0xc2, 8, ip)
print('g10 = 0xc2')
g11 = g10.mulInv()
print('inverse of g10 = g11 =', hex(g11.getInt()))
g12 = g11.affineMap()
print('affine map of g11 =', hex(g12.getInt()))