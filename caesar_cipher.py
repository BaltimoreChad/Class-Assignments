import argparse
import sys

class CaesarCipher(object):
	"""
	Quick program to implement a Caesar cipher on a provided string, using the provided key.
	"""
	def __init__(self, phrase: str, key: int):
		self.phrase = phrase
		self.key = key
		self.alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
						 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 
						 'v':21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
		
	def input_check(self):
		"""
		Verifies that the input provided by the user is valid.
		"""
		for letter in self.phrase:
			if letter.lower() not in self.alphabet:
				if letter.isspace():
					pass
				else:
					return False
		return True
				
	def cipher(self):
		"""
		Performs the Caesar Cipher using the phrase and the key provided by the user.
		"""
		new_string = ""
		for letter in self.phrase:
			upper = False
			new_num = 0
			if letter.isspace():
				new_string += " "
			else:
				if letter.isupper():
					upper = True
				current_num = self.alphabet[letter.lower()]
				new_num = current_num + self.key
				if new_num > 25:
					new_num = (new_num - 25) -1
				new_letter = (list(self.alphabet.keys())[list(self.alphabet.values()).index(new_num)])
				if upper:
					new_letter = new_letter.upper()
				new_string += new_letter
		return new_string
		
	def decipher(self):
		"""
		Deciphers the given phrase using phrase and key provided by user.
		"""
		new_string = ""
		for letter in self.phrase:
			upper = False
			new_num = 0
			if letter.isspace():
				new_string += " "
			else:
				if letter.isupper():
					upper = True
				current_num = self.alphabet[letter.lower()]
				new_num = current_num - self.key
				if new_num < 0:
					new_num = (25 + new_num) + 1
				new_letter = (list(self.alphabet.keys())[list(self.alphabet.values()).index(new_num)])
				if upper:
					new_letter = new_letter.upper()
				new_string += new_letter
		return new_string
		
		
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	group = parser.add_argument_group('group')
	group.add_argument('--decipher', help="Decipher the provided phrase.", action='store_true')
	group.add_argument('--cipher', help="Cipher the provided phrase.", action='store_true')
	parser.add_argument('-p', '--phrase', help="The phrase to encrypt with Caesar Cipher.", required=True)
	parser.add_argument('-k', '--key', type=int, help="The key to use for encryption.", choices=range(0, 26), required=True)
	args = parser.parse_args()
	cipher = CaesarCipher(phrase=args.phrase, key=args.key)
	if cipher.input_check() == True:
		print("Original phrase: {0}".format(args.phrase))
		print("Shift original phrase by: {0}".format(args.key))
		if args.cipher:
			print("Ciphered phrase: {0}".format(cipher.cipher()))
		elif args.decipher:
			print("Deciphered phrase: {0}".format(cipher.decipher()))
	else:
		sys.exit("Invalid input, please try again.")