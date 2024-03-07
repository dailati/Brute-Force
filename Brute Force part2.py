#import string
import itertools

strings = input("[+] Enter a minimum of 10 pieces of information. Words must be 8-10 characters long. ")[:10]

while True:
    if 8 <= len(strings) <= 10:
      break
    else:
      print("[-] Words must be a maximum of 5 characters long.")
      break

p = open("bruteforcer.txt")

for i in itertools.product(strings, repeat=3):
  password = ''.join(i)
  p.write(password + '\n')
