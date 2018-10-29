#Program 1
coeff = []
for i in range(2,-1,-1):
    stri = "Enter coefficients of x^"+str(i)+":"
    coeff.append(int(input(stri)))
print("Your quadartic equation is:",str(coeff[0])+"x^2+"+str(coeff[1])+"x+"+str(coeff[0]))
d = (coeff[1]**2)-(4*coeff[0]*coeff[2])
rd = d**(1/2)
if d==0:
    print("Roots are real and equal!")
elif d>0:
    print("Roots are real!")
elif d<0:
    print("No real roots!")
if d>=0:
    x1 = (-coeff[1] + rd)/(2*coeff[2])
    x2 = (-coeff[1] - rd)/(2*coeff[2])
    print("Roots of quadratic equation are:",x1,",",x2)
