import time
from reciprocals import Reciprocal
from utils import *
import numpy as np


# Looking for a certain fraction's repeating decimal notation :
print(Reciprocal(5, 42))
# prints 0.1(190476), the repeating decimal notation of 5/42 in base 10


# Looking for a certain fraction's repeating notation in another base :
print(Reciprocal(5, 42, 16))
# prints 0.1(e79), the repeating notation of 5/42 in base 16


# Looking for the fraction notation of a rational number given its repeating and non-repeating digits, in any base
number = Reciprocal(base=69)
number.set_dp([55, 17, 14, 47, 14, 16, 14, 23, 13, 50, 15], [61, 14, 21, 13, 10])
number.find_dn() # finds fraction numerator (d) and denominator (n), variable names made sense way back when
print(number) # This took too long



# More sophisticated uses : --------------------------------------------------------

t = time.process_time()
# Checks if period-only reciprocals in base B of all numbers from 2 to 1000 are all primes
B = 2*3*5*7*11*13*17*19*23*29*31
print(check_if_find_primes(range(2,1000), B, False))
# To achieve high precision, B is best chosen when a product of all primes leading up to a chosen integer
print(f"Done in {time.process_time()-t}s")



t = time.process_time()
# Generates random digits and periods in a given base and finds the fraction representing them
reciprocal = Reciprocal(base=16)
digits, period = np.random.randint(0,16,2), np.random.randint(0,16,2)
print("Expected :", convert_arbitrary_base(digits, period))
reciprocal.set_dp(digits, period)
print("{}/{}".format(*reciprocal.find_dn()))
print(reciprocal)
# This works very well in base 10, sometimes has trouble in weird bases
print(f"Done in {time.process_time()-t}s")


