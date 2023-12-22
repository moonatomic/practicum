def inRad(I, g):
    f = sum(I)
    R = f.parent()
    vars = [str(v) for v in R.gens()]
    vars.append('y')
    R1 = PolynomialRing(CC, vars)
    y = R.gens()[-1]
    I1 = I + [1 - y*g]
    J = Ideal(I1).groebner_basis()
    return J == [1.0]

R.<x1,x2,x3> = PolynomialRing(CC, order='lex')
system1 = [x, y, z]
system2 = [x, y]
I = ideal(system1)
J = ideal(system2)

ans = True

for f in I:
    if inRad(J, f) == 0:
        ans = False
        break
if ans:
    for f in J:
    if inRad(I, f) == 0:
        ans = False
        break
print(ans)