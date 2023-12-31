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
        return str(self)

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

def root(a: Zm):
    if not a**((Zm.mod()-1)//2) == 1:
        raise ValueError()
    if Zm.mod() % 4 == 1:
        s = 0
        q = (Zm.mod()-1) // 2
        while q % 2 == 0:
            q = q // 2
            s += 1
        r = a**((q+1)//2)
        if a**q == 1:
            return r
        else:
            t = a**q
            while True:
                ts = t
                i = 1
                while not ts == Zm.mod() - 1:
                    ts = ts**2
                    i += 1
                for j in range(1,Zm.mod()):
                    if Zm(j)**((Zm.mod()-1)//2) == Zm.mod() - 1:
                        z = Zm(j)
                        break
                b = z**(q*2**(s-i))
                r = r*b
                t = t*b*b
                if t == 1:
                    break
            return r

    elif Zm.mod() % 4 == 3:
        rt = a**((p+1)/4)
        return rt
    else:
        raise ValueError('Even module')

if __name__ == '__main__':
    p = int(input('Enter module p: '))
    Zm.setModule(p)

    num = Zm(int(input('Enter number: ')))
    try:
        rt = root(num).n
        print(f'Square root of {num.n} modulo {Zm.mod()} is {rt}')
    except ValueError:
        print(f'{num.n} is not a square modulo {Zm.mod()}')
