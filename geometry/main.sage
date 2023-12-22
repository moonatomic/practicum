def normal(v):
    return vector([-v[1], v[0]])
    
def intersectLines(p0, v0, p1, v1):
    n = normal(v1)
    t = (p1 - p0)*n / (v0*n)
    q = p0 + v0*t
    return q
    
def distanceToLine(t, p, v):
    n = normal(v).normalized()
    return (t - p)*n

a = vector([0, 0.4])
b = vector([4, 0])
c = vector([2.71, 3.14])

tr = line([a,b,c,a],color="black")

vba = ((b-a).normalized() + (c-a).normalized()).normalized()
vbb = ((a-b).normalized() + (c-b).normalized()).normalized()
vbc = ((a-c).normalized() + (b-c).normalized()).normalized()

vma = ((b+c)/2 - a).normalized()
vmb = ((a+c)/2 - b).normalized()
vmc = ((a+b)/2 - c).normalized()

vsma = 2*(vma*vba)*vba - vma
vsmb = 2*(vmb*vbb)*vbb - vmb
vsmc = 2*(vmc*vbc)*vbc - vmc

med = intersectLines(a, vma, b, vmb)
center = intersectLines(a, vba, b, vbb)
lemoine = intersectLines(a, vsma, b, vsmb)

osba = intersectLines(a, (center-a).normalized(), b, (b-c).normalized())
osbb = intersectLines(b, (center-b).normalized(), a, (c-a).normalized())
osbc = intersectLines(c, (center-c).normalized(), b, (a-b).normalized())

osma = intersectLines(a, (med-a).normalized(), b, (b-c).normalized())
osmb = intersectLines(b, (med-b).normalized(), a, (c-a).normalized())
osmc = intersectLines(c, (med-c).normalized(), b, (a-b).normalized())

ossma = intersectLines(a, vsma, b, (b-c).normalized())
ossmb = intersectLines(b, vsmb, a, (a-c).normalized())
ossmc = intersectLines(c, vsmc, a, (a-b).normalized())

bisa = line([a, osba], color="green")
bisb = line([b, osbb], color="green")
bisc = line([c, osbc], color="green")

meda = line([a, osma], color="blue")
medb = line([b, osmb], color="blue")
medc = line([c, osmc], color="blue")

smeda = line([a, ossma], color="red")
smedb = line([b, ossmb], color="red")
smedc = line([c, ossmc], color="red")

show(tr + 
     bisa + bisb + bisc + 
     meda + medb + medc + 
     smeda + smedb + smedc +
     point(center, size=40, color="green") + 
     point(med, size=40, color="blue") +
     point(lemoine, size=40, color="red"), aspect_ratio=1)
