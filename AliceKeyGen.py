# This script implements a simple version of the RSA Encryption protocol

# Importing the necessary libraries
import random
import math
# Sympy is a library for symbolic mathematics
import sympy

# Now we use Sympy to generate a random prime number of a given size
def generate_prime_number(size):
    while True:
        number = random.randint(2**(size-1), 2**size)
        if sympy.isprime(number):
            return number
        
# where "size" is the number of bits of the prime number

# This function takes two prime numbers p and q and returns the Euler's Totient function (p-1).(q-1)

def totient(p, q):
    return (p-1)*(q-1)

# This function takes the Euler's Totient function and returns a random number e such that 1 < e < totient and gcd(e, totient) = 1

def generate_e(totient):
    while True:
        e = random.randint(2, totient)
        if math.gcd(e, totient) == 1:
            return e

# You can just pick e=3, which is the most common choice.

# This function takes the Euler's Totient function and the number e and returns the number d such that (d.e) mod totient = 1 which is the private key

def generate_d(totient, e):
    d = sympy.mod_inverse(e, totient)
    return d

# Alice generates a public key (n, e) and a private key d

print("Enter the number of bits of the prime numbers: ")
size = int(input())
p = generate_prime_number(size)
q = generate_prime_number(size)
n = p*q
t = totient(p, q)
e = generate_e(t)
d = generate_d(t, e)

# The public key is made of the pair (n, e) and the private key is the number d
print("Public key: ", (n, e))

# The private key is kept secret
print("Private key: ", d)

# Alice writes the public key in a file called "public_key.txt"
with open("public_key.txt", "w") as file:
    file.write(str(n) + "\n")
    file.write(str(e))

# Alice writes the private key in a file called "private_key.txt"
with open("private_key.txt", "w") as file:
    file.write(str(d) + "\n")
    file.write(str(n))

    






