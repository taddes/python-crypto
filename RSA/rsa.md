# RSA - Rivest, Shamir, Adlemann

## Fundamentals
* Strength lies in the integer factorization problem/integer factorization as a 'trapdoor' function: validating the reuslt by multiplying two numbers is quite easy, but finding the factors is hard.
* Requires knowledge of prime numbers, Fermat's little theorem and Euler's Phi Function.
* Relatively prime: two integers `a` and `b` are said to be relatively prime or coprime if the only positive integer (factor) that divides both is 1. `gcd(a, b) = 1`
* Let `p` be a prime number, then for any integer, `a`, where `a` is not divisible by `p`, the number `a^p-1` is an integer multiple of `p`. `a^p-1 is congruent to 1 (mod p)`, so the remainder is always 1. 

* Euler's Phi Function: takes in a number, and for all values up to that number, returns the number of values that are relatively prime (being ones that have a greatest common divisor of 1 with the number passed in. 
* Euler's Phi Function counts the positive integers up to a given integer, `n`, that are relatively prime to `n`. `a^phi(n) is congruent to 1 (mod p)` if `n` and `a` are relative primes.
* This function makes it quite easy to calculate for prime numbers. 
* By definition, a prime is coprime with all the smaller integers within the range `[1, prime-1]`. **If the input is a prime number, the output is the prime - 1: Phi(prime_no) = prime_no - 1**
  * Examples:
  * Phi(5) = 1,2,3,4 -> so the value of the function is 4
  * Phi(8) = 1,3,5,7 -> so the value of the function is 4
  * Phi(7) = 1,2,3,4,5,6 -> so the value of the function is 6

## Algorithm Implementation
### Key Generation
1. Generate 2 large prime numbers, `p` and `q`, usually using the Rabin-Miller algorithm. Generally numbers are > 1024 bits, but it is recommended to use > 2048 bits in modern implementations.
2. Calculate `n`, by multiplying `p` and `q` together. `n = p*q`. Using Euler's Phi Function, the result is as such: `Phi(n) = (p-1)(q-1)`
3. Calculate the public key `e` parameter. We calculate `e`, such that `gcd(e, Phi(n))=1`, so that `e` and `Phi(n)` are relative primes, and that they share no factor other than 1.
4. Calculate the private key `d` parameter. We calculate the modular inverse of `e`. The modular inverse of `e` is `d`. This is why it is crucial that `e` and `Phi(n)` are coprime. `d * e mod Phi(n) = 1`
* **PUBLIC KEY: (E,N)**
* **PRIVATE KEY: (D,N)**

### Encryption
1. Transform plaintext into blocks where each block is smaller than n.
2. Use the public key for encryption and the private key for decryption. Typically use ASCII table to convert text to numbers.
```
ciphertext_block = plaintext_block^e mod n
plaintext_block = ciphertext_block^d mod n
```
### Problem of Modular Inverse



## Cracking RSA
* Because this is a public-key system, everyone on the public network is aware of the public keys. The aim of an attacker is to calculate the private key pair (d, n).
* The main problem is integer factorization. When encrypting, a trapdoor function is run to create they keys (two primes, p and q). To reverse this operation, the runtime complexity is exponential. 
* Factoring large numbers is hard (if a given number has smaller factors, it could be found within hundreds or thousands of iterations). This is why one must ensure the prime factors are large. **`n = p*q`**. To get the factors of n, it is incredibly difficult.