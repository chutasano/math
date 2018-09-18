from random import randint

# return p,q,e,d
def genkey(bit_size):
    # two primes p,q such that |p*q| = bit_size
    p,q = genprimes(bit_size)
    # small e is better for practical purposes (makes distribution lighterweight +
    # mod exp on the enduser easier). I'm pretty sure most of the e's are 3 or 5,
    # but i'll try some other numbers for fun)
    e = 2*randint(0, 14)+1
    

