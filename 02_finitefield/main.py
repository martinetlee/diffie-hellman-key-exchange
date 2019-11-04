import finitefield

a = finitefield.NumInFiniteField(10, 19)
b = finitefield.NumInFiniteField(11, 19)

c = a+b


print("The inverse of ", a, " is ", a.inverse(), " in field ", a.finitefield )
print("The inverse of ", b, " is ", b.inverse(), " in field ", b.finitefield )
print("The inverse of ", c, " is ", c.inverse(), " in field ", c.finitefield )
