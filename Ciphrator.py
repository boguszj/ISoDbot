class Ciphrator:

	def cypher(text):
		result = ''
		for letter in text:
			letter = chr((ord(letter) + len(text) % 6) % 128)
			result += letter
		return result

	def decypher(text):
		result = ''
		for letter in text:
			letter = chr((ord(letter) - len(text) % 6) % 128)
			result += letter
		return result

		





