#Importing required modules.

import hashlib

#SHA-256 function.

def sha256():

	try:

		a1 = input("Enter what do you want to hash (SHA256): ")
		d1 = hashlib.sha256((a1).encode('utf8'))
		print(d1.hexdigest())

	except NameError:

		print(ERROR)
		sha256()

#MD5 function.

def md5():

	try:

		a2 = input("Enter what do you want to hash (MD5): ")
		d2 = hashlib.md5((a2).encode('utf8'))
		print(d2.hexdigest())

	except NameError:

		print(ERROR)
		md5()

#You can add more hash methods.



