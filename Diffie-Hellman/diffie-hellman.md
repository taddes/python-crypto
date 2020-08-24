# Diffie-Hellman Key Exchange
* Created by Diffie, Hellman and Merkle.
* Protocol to exchange private keys over a public channel. This is intended to securely exchange private keys for symmetric cryptosystems. 
* No information is shared during the key exchange.
* *sidenote* Merkle created the Merkle Tree data-structure, which is the fundamental building block of the Bitcoin ecosystem

## Process
* Generate large prime numbers n and g. **g must be the primitive root of n**
* *Primitive Root:* g is the primitive root of n if g mod n, g^2 mod 2 ... g^n-1 mod n generates all the integers within the range [1, n-1]
  * Example:
  We can conclude that 8 is a primitive root of 11, so these are good values for the Diffie-Hellman key exchange, since they generate all the integers within the range [1, n-1].
  8^1 mod 11 = 8
  8^2 mod 11 = 9
  8^3 mod 11 = 6
  8^4 mod 11 = 4
  8^5 mod 11 = 10
  8^6 mod 11 = 3
  8^7 mod 11 = 2
  8^8 mod 11 = 5
  8^9 mod 11 = 7
  8^10 mod 11 = 1

## How to compromise Diffie-Hellman
* Because of the discrete algorithm problem (trapdoor problem): you can't easily calculate the exponents to determine each private key. It is esentially easy to calculate (using modular exponentiation), reversing the process is impossible due to its difficulty (while theoretically possible, just not feasible)
* Using Man-In-The-Middle attack to compromise key exchange. There is no authentication during the exchange of initial variables (n, g and two public keys). If someone in the middle manages to intercept a public key, they can pretend to be one of the parties in the public key exchange. *This is why it is recommended to use SHA256 hashes for authentication* Messages are signed with a SHA256 hash that prevents MITM attacks.