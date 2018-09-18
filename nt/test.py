import nt
from random import randint

import unittest

TESTS = 10

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(nt.gcd(15,6), 3)
    def test_gcd_rev(self):
        for i in range(TESTS):
            a = randint(1,10000000) 
            b = randint(1,10000000) 
            self.assertEqual(nt.gcd(a,b), nt.gcd(b,a))
    def test_gcd_one(self):
        for i in range(TESTS):
            a = randint(1,10000000)
            self.assertEqual(nt.gcd(a, 1), 1)
    def test_gcd_rand(self):
        for i in range(TESTS):
            a = randint(1,10000000)
            b = randint(1,10000000)
            g = nt.gcd(a,b)
            self.assertEqual(nt.gcd(a/g, b/g), 1)
    def test_mod_inv(self):
        for i in range(TESTS):
            a = randint(1,10000000)
            b = randint(1,10000000)
            g = nt.gcd(a,b)
            # ensure a, b are relatively prime
            a, b = a/g, b/g
            ainv = nt.modinv(a, b)
            self.assertEqual((a*ainv)%b, 1)
    def test_mod_exp(self):
        for i in range(TESTS):
            a = randint(2,10000000)
            b = randint(1,1000)
            m = randint(2,10000000)
            self.assertEqual(nt.modexp(a,b,m), (a**b)%m)
    def test_basechange(self):
        for i in range(TESTS):
            n = randint(1,10000000)
            b = randint(1,1000)
            k = nt.basechange(n, b)
            n_ = 0
            current_b = 1
            for d in k:
                n_ += current_b * d
                current_b *= b
            self.assertEqual(n, n_)

if __name__ == '__main__':
    unittest.main()
