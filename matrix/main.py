class Zm:
    m = 7

    @staticmethod
    def setModule(m):
        n = int(m)
        if n == 0:
            raise ValueError('Zero module')
        if n > 0:
            Zm.m = n
        else:
            Zm.m = (-n)

    @staticmethod
    def mod():
        return Zm.m

    def __init__(self, n=0):
        self.n = int(n)%Zm.m

    def __int__(self):
        return self.n

    def copy(self):
        return Zm(self.n)

    def __add__(self, y):
        x = (self.n + int(y))%Zm.m
        return Zm(x)

    def __radd__(self, y):
        x = (int(y) + self.n)%Zm.m
        return Zm(x)

    def __iadd__(self, y):
        self.n = (self.n + int(y))%Zm.m
        return self

    def __sub__(self, y):
        x = (self.n - int(y))%Zm.m
        return Zm(x)

    def __rsub__(self, y):
        x = (int(y) - self.n)%Zm.m
        return Zm(x)

    def __isub__(self, y):
        self.n = (self.n - int(y))%Zm.m
        return self

    def __mul__(self, y):
        x = (self.n * int(y))%Zm.m
        return Zm(x)

    def __rmul__(self, y):
        x = (int(y) * self.n)%Zm.m
        return Zm(x)

    def __imul__(self, y):
        self.n = (self.n * int(y))%Zm.m
        return self

    def inverse(self):
        (d, u, v) = extgcd(self.n, Zm.m)
        if d != 1:
            raise ZeroDivisionError('Division by zero modulo m')
        return Zm(u)

    def __truediv__(self, y):
        k = Zm(y).inverse()
        return self * k

    def __rtruediv__(self, y):
        k = self.inverse()
        return Zm(y) * k

    def __itruediv__(self, y):
        k = Zm(y).inverse()
        self.n = (self.n * int(k))%Zm.m
        return self

    def __pow__(self, n):
        a = self.copy()
        k = int(n)
        if k < 0:
            k = (-k)
            a = self.inverse()
        p = Zm(1)
        while k > 0:
            if k%2 == 0:
                k //= 2
                a *= a
            else:
                k -= 1
                p *= a
        return p

    def __repr__(self):
        return str(self.n)

    def __eq__(self, y):
        return (self.n - int(y))%Zm.m == 0

    def __ne__(self, y):
        return not (self == y)

    def __lt__(self, y):
        return (self.n < int(y))

    def __le__(self, y):
        return (self.n <= int(y))

    def __gt__(self, y):
        return (self.n > int(y))

    def __ge__(self, y):
        return (self.n >= int(y))

def powmod(a, n, m):
    b = a; k = n; p = 1
    while k > 0:
        if k%2 == 0:
            k //= 2; b = (b*b)%m
        else:
            k -= 1; p = (p*b)%m
    if (p < 0):
        p += m
    return p

def gcd(m, n):
    a = int(m); b = int(n)
    while b != 0:
        r = a%b
        (a, b) = (b, r)
    if a > 0:
        return a
    else:
        return (-a)
    
def extgcd(m, n):
    (a, b) = (int(m), int(n))
    (u1, v1) = (1, 0)
    (u2, v2) = (0, 1)
    while b != 0:
        q = a // b 
        r = a % b
        (u1, u2) = (u2, u1 - q*u2)
        (v1, v2) = (v2, v1 - q*v2)
        (a, b) = (b, r)
    if a > 0:
        return (a, u1, v1)
    else:
        return (-a, -u1, -v1)
    
def invmod(x, m):
    (d, u, v) = extgcd(x, m)
    if d != 1:
        raise ZeroDivisionError('Division by zero modulo m')
    return u

class Matrix:
    m = 2
    n = 2
    matrix = []

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                self.matrix[i][j] = Zm(0)

    def copy(self):
        x = Matrix(self.n, self.n)
        for i in range(self.n):
            for j in range(self.m):
                x.setElement(i, j, self.getElement(i, j))
        return x
    
    def getString(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)  
    
    def __str__(self):
        return self.getString(self.matrix)

    def getElement(self, i, j):
        return self.matrix[i][j]
    
    def setElement(self, i, j, element):
        self.matrix[i][j] = Zm(element)
        return 0

    def __add__(self, y):
        x = Matrix(self.n, self.m)
        for i in range(x.n):
            for j in range(x.m):
                x.setElement(i, j, self.getElement(i,j)+y.getElement(i,j))
        return x

    def __radd__(self, y):
        x = Matrix(self.n, self.m)
        for i in range(x.n):
            for j in range(x.m):
                x.setElement(i, j, self.getElement(i,j)+y.getElement(i,j))
        return x

    def __sub__(self, y):
        x = Matrix(self.n, self.m)
        for i in range(x.n):
            for j in range(x.m):
                x.setElement(i, j, y.getElement(i,j)-self.getElement(i,j))
        return x

    def __rsub__(self, y):
        x = Matrix(self.n, self.m)
        for i in range(x.n):
            for j in range(x.m):
                x.setElement(i, j, self.getElement(i,j)-y.getElement(i,j))
        return x

    def __mul__(self, y):
        x = Matrix(self.n, y.m)
        res = Zm(0)
        for i in range(x.n):
            for j in range(x.m):
                res = 0
                for k in range(self.m):
                    res += self.getElement(i,k)*y.getElement(k,j)
                x.setElement(i, j, res)
        return x

    def __rmul__(self, y):
        x = Matrix(y.n, self.m)
        res = Zm(0)
        for i in range(x.n):
            for j in range(x.m):
                res = 0
                for k in range(y.m):
                    res += y.getElement(i,k)*self.getElement(k,j)
                x.setElement(i, j, res)
        return x
    
    def GaussJordanMethod(self):
        for i in range(self.n):
            if (self.getElement(i, i) == 0):
                fnd = False
                ind = 0
                for s in range(i+1, self.n):
                    if self.getElement(s, i) != 0:
                        fnd = True
                        ind = s
                        break
                if fnd:
                    for j in range(self.n):
                        swp = self.getElement(i, j)
                        self.setElement(i, j, self.getElement(ind, j))
                        self.setElement(ind, j, self.getElement(s, j))
                else:
                    continue
            mult = self.getElement(i,i).inverse()
            for j in range(self.m):
                self.setElement(i, j, self.getElement(i, j) * mult)
            for k in range(self.n):
                if (k != i):
                    mult = self.getElement(k, i)
                    for j in range(i, self.m):
                        self.setElement(k, j, self.getElement(k, j) - mult*self.getElement(i, j))


    def solveSystem(self, b):
        ext = Matrix(self.n, self.n+1)
        sol = []
        for i in range(self.n):
            for j in range(self.n):
                ext.setElement(i, j, self.getElement(i, j))
            ext.setElement(i, self.n, b[i])
        ext.GaussJordanMethod()
        for i in range(self.n):
            sol.append(ext.getElement(i, self.n))
        return sol

    def rank(self):
        b = self.copy()
        b.GaussJordanMethod()
        for i in range(b.n):
            if b.getElement(i, i) == 0:
                return i
        return b.n

    def det(self):
        ans = Zm(1)
        if self.n != self.m:
            raise Exception("Non-square matrix")
        else:
            for i in range(self.n):
                ans = ans * self.getElement(i, i)
        return ans

    def inverse(self):
        x = Matrix(self.n, self.n)
        for i in range(self.n):
            x.setElement(i, i, 1)
        ext = Matrix(self.n, 2*self.n)
        for i in range(self.n):
            for j in range(self.n):
                ext.setElement(i, j, self.getElement(i, j))
                ext.setElement(i, j+self.n, x.getElement(i, j))
        ext.GaussJordanMethod()
        for i in range(self.n):
            for j in range(self.n):
                self.setElement(i, j, ext.getElement(i, j+self.n))

if __name__ == '__main__':
    a = Matrix(5, 5)

    for i in range(a.n):
        for j in range(a.m):
            if i == j:
                a.setElement(i, j, 3)
            elif j == i+1:
                a.setElement(i, j, 1)

    print("MATRIX")
    print(a)
    print("RANK:")
    print(a.rank())
    print("DET")
    print(a.det())
    print("INVERSE")
    b = a.copy()
    a.inverse()
    print(a)
    print("A*A^-1")
    print(a*b)
    print()
    print(b*a)
    c = [1, 2, 3, 4, 5]
    print("SOLVING BX = ",end='')
    print(c)
    print(b.solveSystem(c))