# Python program Elgamel

import random
from math import pow

a = random.randint(2, 10)

# Function for finding greatest common divisor of two numbers using the eulcid algorithm whose time complexity is log(min(a,b)).

def euclid_gcd(a, b):
	if a < b:
		return euclid_gcd(b, a)
	elif a % b == 0:
		return b;
	else:
		return euclid_gcd(b, a % b)

# Function used for generating large random numbers.

def gen_large_key(q):

	key = random.randint(pow(10, 20), q)
	while euclid_gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)

	return key

# Function used for computing (a^b)%c in log(b) steps using modular exponentiation.

def power_mod(a, b, c):
	x = 1
	y = a

	while b > 0:
		if b % 2 != 0:
			x = (x * y) % c;
		y = (y * y) % c
		b = int(b / 2)

	return x % c

# Asymmetric encryption
def encrypt(msg, q, h, g):

	en_msg = []

	k = gen_large_key(q)# Private key for sender
	s = power_mod(h, k, q)
	p = power_mod(g, k, q)
	
	for i in range(0, len(msg)):
		en_msg.append(msg[i])

	print("g^k used : ", p)
	print("g^ak used : ", s)
	for i in range(0, len(en_msg)):
		en_msg[i] = s * ord(en_msg[i])

	return en_msg, p

def decrypt(en_msg, p, key, q):

	dr_msg = []
	h = power_mod(p, key, q)
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(int(en_msg[i]/h)))
		
	return dr_msg

# Driver code
def main():

	msg = 'BharatIsAGoodBoy '
	print("Original Message :", msg)

	q = random.randint(pow(10, 20), pow(10, 50))
	g = random.randint(2, q)

	key = gen_large_key(q)# Private key for receiver
	h = power_mod(g, key, q)
	print("g used : ", g)
	print("g^a used : ", h)

	en_msg, p = encrypt(msg, q, h, g)
	dr_msg = decrypt(en_msg, p, key, q)
	dmsg = ''.join(dr_msg)
	print("Decrypted Message :", dmsg);


if __name__ == '__main__':
	main()
