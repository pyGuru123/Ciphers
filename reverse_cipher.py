import webbrowser

class ReverseCipher:
	def __init__(self):
		''' This is a python implementation of Reverse Cipher'''
		self.result = None

	def about(self):
		'''Read about Reverse Cipher online'''
		url = 'https://inventwithpython.com/hacking/chapter5.html'
		webbrowser.open(url) 

	def encrypt(self, msg: str) -> str:
		result = msg[::-1]
		return result

	def decrypt(self, msg: str) -> str:
		result = self.encrypt(msg)
		return result

if __name__ == '__main__':
	cipher = ReverseCipher()
	message = 'The quick brown 🦊 jumps over the lazy 🐶.'

	encrypted = cipher.encrypt(message)
	decrypted = cipher.decrypt(encrypted)

	print(encrypted)
	print(decrypted)