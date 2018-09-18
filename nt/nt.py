import math

# some elementary number theory algorithms/functions
def isroot(a, m):
    return isrelprime(a, m)

def isrelprime(a, b):
    return gcd(a, b) == 1

# euclid's alg impl, assumes a > b
def gcd(a, b):
    assert(a > 0 and b > 0)
    if (a < b):
        a,b = b,a
    while b != 0:
        a, b = b, a - b * (a//b)
    return a

def lcm(a, b):
    return a*b/gcd(a,b)

# returns the modular inverse of a mod m
def modinv(a, m):
    s = 0
    t = 1
    r = m
    old_s = 1
    old_t = 0
    old_r = a
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q*r
        old_s, s = s, old_s - q*s
        old_t, t = t, old_t - q*old_t
    return old_s

# ~O(n)
# return a^b mod m
def modexp(a, b, m):
    lookup = [a]
    bitstring = basechange(b, 2)
    for i in range(len(bitstring)-1):
        k = lookup[-1]
        lookup.append((k*k)%m)
    final = 1
    for i in range(len(bitstring)):
        if bitstring[i] == 1:
            final = (final*lookup[i])%m
    return final

# returns N, M where N is a single solution and M is a factor that yields
# infinitely many solutions of the form N' = N + Mk for int k
# constraints are list of tuples and of the form
# [ (a1, m1), (a2, m2), ... ]
# where a tuple a,m defines a single constraint to the solution, s
# s = a mod m
def crt(constraints):
    pass

# returns a list of coefficients c such that
# n = c0*b^0 + c1*b^1 + c2*b^2 + ...
def basechange(n, b):
    c = []
    prev_b = 1
    current_b = b
    while (n != 0):
        a = n%current_b
        n -= a
        c.append(a//prev_b)
        prev_b, current_b = current_b, current_b*b
    return c

# returns c number in some base
def c(n, b=10):
    nstr = basechange(n, b)
    final = 1
    cur_comb = 1
    for i in range (math.floor(len(nstr)/2)):
        final *= nstr[i]**cur_comb
        final *= nstr[-i-1]**cur_comb
        cur_comb *= len(nstr)-i-1
        cur_comb = cur_comb//(i+1)
    if len(nstr)%2 == 1:
        final *= nstr[len(nstr)//2]**cur_comb
    return final
