"""Personal test file"""
from cipher import *

tests = dict([
    ['python is fun!', 'udymts nx kzs!'],
    ['aaa', 'fff'],
    ['xyz', 'cde'],
    ['A sentence with Capital letters.', 'f xjsyjshj bnym hfunyfq qjyyjwx.'],
    ['#$%^&*()', '#$%^&*()']
    ])

# for plaintext, cryptotext in tests.items():
#     print("PLAIN", plaintext)
#     print("CRYPT", cryptotext)
#     print("SHFT5", shift5(plaintext))

CONDITION = True
for P, C in tests.items():
    CONDITION = (True if shift5(P) == C else False)
print(CONDITION)
