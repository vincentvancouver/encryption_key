## Return a 24 digit alphanumeric passkey

import random


def encryption():
	alphanum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	key = ''
	while len(key)<24:
		key += alphanum[random.randint(0, 61)]
	print(key)