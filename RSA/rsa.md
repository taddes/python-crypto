# RSA - Rivest, Shamir, Adlemann

## Fundamentals
* Strength lies in the integer factorization problem/integer factorization as a 'trapdoor' function: validating the reuslt by multiplying two numbers is quite easy, but finding the factors is hard.


## Cracking RSA
* Because this is a public-key system, everyone on the public network is aware of the public keys. The aim of an attacker is to calculate the private key pair (d, n).
* The main problem is integer factorization. When encrypting, a trapdoor function is run to create they keys (two primes, p and q). To reverse this operation, the runtime complexity is exponential. 
* Factoring large numbers is hard (if a given number has smaller factors, it could be found within hundreds or thousands of iterations). This is why one must ensure the prime factors are large. **`n = p*q`**. To get the factors of n, it is incredibly difficult.