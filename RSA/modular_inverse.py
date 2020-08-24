"""
A naive approach for determining the modular inverse. 
Beware it is not a practical algorithm, as it has an exponential runtime
"""
from math import sqrt
from math import floor

def modular_inverse(a, m):
    for inv in range(0, m):
        if (a*inv) % m == 1:
            return inv
    print(f'There is no modular inverse, as a ({a}) is not coprime to m ({m})')

if __name__ == "__main__":
    print(modular_inverse(7, 31))