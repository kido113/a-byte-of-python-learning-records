from string import punctuation
def deal(text):
	text = text.lower()
	print("text.lower():",text)
	text = text.replace(' ','')
	print("text.replace():",text)
	text = text.translate(str.maketrans('','',punctuation))
	print(text)
	return text

def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = input("Enter text:")
something = deal(something)
if is_palindrome(something):
	print("Yes, it is a palindrome.")
else:
	print("No, it is not a palindrome.")


