import random, string

digits = ''.join(random.sample(string.digits, 8))
chars = ''.join(random.sample(string.ascii_letters, 10)).upper()

print("digits="+str(digits))
print("chars="+chars)
