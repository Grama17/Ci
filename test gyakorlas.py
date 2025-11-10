import unittest
import math

szam1=int(input("szam1"))
szam2=int(input("szam2"))

def abs_max(a:int, b:int) -> int:
    if(abs(a)>abs(b)):
        return(abs(a))
    if(abs(a)<abs(b)):
        return(abs(b))
    
        
print(abs_max(szam1,szam2))

class Testek(unittest.Testcase):
    def test_nagyobb_nulla(self):
        nagyobb=int(abs_max(szam1,szam2))
        self.assertGreater(nagyobb,0)

class Testek(unittest.Testcase):
    def test_nagyobb_nulla(self):
        nagyobb=int(abs_max(szam1,szam2))
        self.assertGreater(nagyobb,99)

unittest.main()