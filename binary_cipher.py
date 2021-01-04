import webbrowser

class BinaryCipher:
	def __init__(self):
		''' This is a python implementation of Binary Cipher'''
		self.result = None

	def about(self):
		'''Read about Binary Cipher online'''
		url = 'https://en.wikipedia.org/wiki/Binary-to-text_encoding'
		webbrowser.open(url) 

	def encrypt(self, msg: str) -> str:
		result = ''
		for ele in msg:
			value = ord(ele)
			binary_value = bin(value) + ' '
			result += binary_value[2:]

		return result

	def decrypt(self, msg: str) -> str:
		result = ''
		splitted_list = msg.split()
		for ele in splitted_list:
			value = int(ele, 2)
			result += chr(value)

		return result

if __name__ == '__main__':
	cipher = BinaryCipher()
	message = 'The quick brown 🦊 jumps over the lazy 🐶.'

	encrypted = cipher.encrypt(message)
	decrypted = cipher.decrypt(encrypted)

	print(encrypted)
	print(decrypted)