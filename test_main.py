import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_forces(self) :
        pp = pos
        # Get the positions and analytic forces
        base_p, base_f = potential(pp)
        for i in range(7) :
           for j in range(2) :
               pp[i][j] = pp[i][j] + 1E-8
               new_p, crap = potential(pp)
               numder = (new_p-base_p)/1E-8
               self.assertTrue( np.abs(numder + base_f[i][j])<1e-4, "your forces are not consistent with the potential" )
               pp[i][j] = pp[i][j] - 1E-8
