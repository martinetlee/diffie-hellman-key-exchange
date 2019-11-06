# a, b --> (gcd, X, Y), where aX + bY = gcd(a,b)
def euclidean_algorithm(a,b):
    if a > b:
        curLarge = a
        curSmall = b
    else:
        curLarge = b
        curSmall = a

    curSmallX = 1
    curSmallY = 0

    curLargeX = 0
    curLargeY = 1


    while(curSmall > 0):
        multiplier = curLarge//curSmall
        remainder = curLarge%curSmall

        tempX = curLargeX - multiplier * curSmallX
        tempY = curLargeY - multiplier * curSmallY

        curLargeX = curSmallX
        curLargeY = curSmallY
        curSmallX = tempX
        curSmallY = tempY

        curLarge = curSmall
        curSmall = remainder

    gcd_result = curLarge
    
    if a > b:
        X = curLargeX
        Y = curLargeY
    else:
        X = curLargeY
        Y = curLargeX

    return [gcd_result, X, Y]



class NumInFiniteField:
    def __init__(self, val, finitefield):
        self.finitefield = finitefield
        self.val = val;

    def __str__(self):
        return "{0}".format(self.val)


    def checkFiniteFieldMatch(self, num1, num2):
        if(num1.finitefield != num2.finitefield):
            raise ValueError("Finite field of both numbers doesn't match", self.finitefield, base.finitefield)

    def __add__(self, other):
        self.checkFiniteFieldMatch(self, other)
        newVal = (self.val + other.val) % self.finitefield
        return NumInFiniteField(newVal, self.finitefield)


    def __sub__(self, other):
        self.checkFiniteFieldMatch(self, other)
        newVal = (self.val - other.val)% self.finitefield
        return NumInFiniteField(newVal, self.finitefield)

    def __mul__(self, other):
        self.checkFiniteFieldMatch(self, other)
        newVal = (self.val * other.val)% self.finitefield
        return NumInFiniteField(newVal, self.finitefield)


    # Using Extended Euclidean algorithm to calculate
    # the inverse. ax + my = gcd(a,m) = 1
    # 
    # A couple of assumptions here: 
    # (1) self.val < self.finitefield
    # (2) gcd(self.val, self.finitefield) = 1
    
    def inverse(self):
       
        curSmallX = 1
        curSmallY = 0

        curLargeX = 0
        curLargeY = 1

        curSmall = self.val
        curLarge = self.finitefield

        while(curSmall > 0):
            multiplier = curLarge//curSmall
            remainder = curLarge%curSmall

            tempX = curLargeX - multiplier * curSmallX
            tempY = curLargeY - multiplier * curSmallY

            curLargeX = curSmallX
            curLargeY = curSmallY
            curSmallX = tempX
            curSmallY = tempY

            curLarge = curSmall
            curSmall = remainder

        # when curSmall = 0, curLarge is the gcd

        # check if the gcd is 1
        if(curLarge != 1):
            raise ValueError("expecting the value and the base to be coprime")

        # when curLarge is 1 : curLargeX * self.val + curLargeY * self.finitefield = 1
        # curLargeX is the inverse

        # However, curLargeX could be < 0, we will need to convert it into the field

        return curLargeX % self.finitefield



    # Calculate the square root
    #   One way is to utilize Fermat's little theorem
    #   What is the other more efficient way?

