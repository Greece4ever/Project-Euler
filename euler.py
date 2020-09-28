def p1():
    """multiples of 3 and 5"""
    total : int = 9 
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total #233177


def p2():
    """Even fibbonaci numbers"""
    cache = {}
    def fib(n):
        if n in cache:
            return cache.get(n)
        if n <= 1:
            return 1
        seq = fib(n-2) + fib(n-1)
        cache[n] = seq;return seq
    total : int = 0
    f = fib(0);i : int = 0
    while f < 4000000:
        f = fib(i)
        if f % 2 ==0:
            total += f
        i+=1
    return total #4613732

def p3():
    """Largest prime factor"""
    def isPrime(x):
        for i in range(2,round(x**(1/2))):
            if x%i==0:
                return False
        return True
    factors : list = []
    for j in range(2,round(600851475143**(1/2))):
        if 600851475143 % j ==0:
            factors.append(j)
    return max([num for num in factors if isPrime(num)]) #6857

def p4():
    """Largest palindrome product"""
    palindromes : list = []
    for i in range(999):
        for j in range(999):
            p = str(i*j)
            if list(p) == list(reversed(p)):
                palindromes.append(int(p))
    return max(palindromes) #906609

def p5(): #TODO
    """Smallest multiple"""
    divs : list = [];i : int = 21
    while not divs.count(0) == 19:
        divs = [i % d for d in range(2,21)]
        i +=1                    
        if divs.count(0) > 16:
            print(i,divs.count(0))                
    return i #One eternety later :

def p6():
    """Sum square difference"""
    diffs : list = []
    for i in range(100):
        s1 = sum(range(i))**2 
        s2 = sum([j**2 for j in range(i)])
        diffs.append(s1-s2)
    return diffs

def p7():
    """10001st prime"""
    def isPrime(x):
        for i in range(2,round(x**(1/2))):
            if x%i==0:
                return False
        return True
    primes : list = []
    i : int = 2
    while len(primes) <= 10001:
        if isPrime(i):
            primes.append(i)
        i+=1
    return primes[-1] #104009

def p8():
    """Largest product in a series"""
    largenum : str = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""
    def product(items):
        p = 1
        for l in items:
            p *= int(l)
        return p
    prods : list = [];d : int = 0
    while( (d+13) < len(largenum)):        
        prods.append(product(largenum[d:d+13]))
        d+=1
    return max(prods) #23514624000

def p9():
    """Special Pythagorean triplet"""
    # This is bad stupid code
    # there is no point in checking
    # when not a < b < c
    # do not write code like this
    def isPythagoreanTriplet(a,b,c):
        return (a**2 + b**2) == c**2
    for i in range(1,1000): # 1 3 3 
        for j in range(1,1000):
            for k in range(1,1000):
                if isPythagoreanTriplet(i,j,k):
                    if(i+j+k) == 1000:
                        return i*j*k #200 375 425

def p10(): #TODO
    def product(items):
        p = 1
        for l in items:
            p *= int(l)
        return p
    grid = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8,49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0,81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65,52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91,22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80,24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50,32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70,67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21,24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72,21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95,78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92,16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57,86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58,19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40,4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66,88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69,4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36,20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16,20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54,1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48,]
    
    def right(x):
        if x+4 > len(grid):
            return 1
        return product(grid[x:x+4])
    
    def left(x):
        return product(grid[x-3:x+1])
    
    def up(x):
        if 0 > (x - 60):
            return 0
        return product([grid[x-(i*20)] for i in range(4)])
    
    def down(x):
        if len(grid) < x+(4*20):
            return 0
        return product([grid[x+ (i*20)] for i in range(4)])

    products = []
    for d in range(len(grid)):
        products.append(max([right(d),left(d),up(d),down(d)]))
    return max(products)

print(p5())