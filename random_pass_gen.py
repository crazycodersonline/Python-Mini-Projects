import random
pass_len = 15

alphabets_lower = "abcdefghijklmnopqrstuvwxyz"
alphabets_upper = alphabets_lower.upper()
nums = "1234567890" 
special_chars =  "!@#$%^&*()"

possible_chars = alphabets_lower+alphabets_upper+nums+special_chars
password = []

for i in range(pass_len):
	random_char = random.choice(possible_chars)
	password.append(random_char)

password = ''.join(password)
print(password)