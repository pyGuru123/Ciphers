import string
import webbrowser

class CeaserCipher:
	def __init__(self):
		''' This is a python implementation of Ceaser Cipher'''
		self.alphabets = string.ascii_lowercase

	def about(self):
		'''Read about Ceaser Cipher online'''
		url = 'https://en.wikipedia.org/wiki/Caesar_cipher'
		webbrowser.open(url) 

	def encrypt(self, msg: str, key: int) -> str:
		result = ''
		for ele in msg.lower():
			pos = self.alphabets.find(ele)
			new = (pos + key) % 26
			result += self.alphabets[new]

		return result

	def decrypt(self, msg: str, key: int) -> str:
		result = ''
		for ele in msg.lower():
			pos = self.alphabets.find(ele)
			new = (pos - key) % 26
			result += self.alphabets[new]

		return result

if __name__ == '__main__':
	cipher = CeaserCipher()
	message = 'hello'
	key = 3

	encrypted = cipher.encrypt(message, key)
	decrypted = cipher.decrypt(encrypted, key)

	print(encrypted, decrypted)