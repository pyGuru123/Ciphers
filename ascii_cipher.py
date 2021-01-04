import webbrowser

class ASCIICipher:
	def __init__(self):
		''' This is a python implementation of Ascii Cipher'''
		self.result = None

	def about(self):
		'''Read about Ascii Cipher online'''
		url = 'http://www.asciitable.com/'
		webbrowser.open(url) 

	def encrypt(self, msg: str) -> str:
		result = ''
		for ele in msg:
			value = ord(ele)
			result += f'{value} '

		return result

	def decrypt(self, msg: str) -> str:
		result = ''
		for ele in msg.split():
			value = chr(int(ele))
			result += value

		return result

if __name__ == '__main__':
	cipher = ASCIICipher()
	message = 'The quick brown 🦊 jumps over the lazy 🐶.'

	encrypted = cipher.encrypt(message)
	decrypted = cipher.decrypt(encrypted)

	print(encrypted)
	print(decrypted)