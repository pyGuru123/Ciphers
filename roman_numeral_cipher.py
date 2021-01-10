import webbrowser

class RomanNumeralCipher:
	def __init__(self):
		''' This is a python implementation of Roman Numeral Cipher'''
		self.val = [
				1000, 900, 500, 400,
				100, 90, 50, 40,
				10, 9, 5, 4,
				1
		]
		self.syb = [
				"M", "CM", "D", "CD",
				"C", "XC", "L", "XL",
				"X", "IX", "V", "IV",
				"I"
		]

	def about(self):
		'''Read about Roman Numeral Cipher online'''
		url = 'https://www.britannica.com/topic/Roman-numeral'
		webbrowser.open(url) 

	def encrypt(self, num: int) -> str:
		result = ''

		if not isinstance(num, int):
			return 'Cannot cast to Roman cipher'

		i = 0
		while  num > 0:
			for _ in range(num // self.val[i]):
				result += self.syb[i]
				num -= self.val[i]
			i += 1

		return result

	def decrypt(self, msg: str) -> int:
		list_ = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']
		num = 0

		for ele in list_:
			if ele in msg:
				msg = msg.replace(ele, '')
				num += self.val[self.syb.index(ele)]
		for ele in msg:
			num += self.val[self.syb.index(ele)]

		return num

if __name__ == '__main__':
	cipher = RomanNumeralCipher()
	message = 3349

	encrypted = cipher.encrypt(message)
	decrypted = cipher.decrypt(encrypted)

	print(encrypted)
	print(decrypted)