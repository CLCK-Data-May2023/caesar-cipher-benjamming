"""Personal test file"""
from cipher import *

tests = dict([
    ['python is fun!', 'udymts nx kzs!'],
    ['aaa', 'fff'],
    ['xyz', 'cde'],
    ['A sentence with Capital letters.', 'f xjsyjshj bnym hfunyfq qjyyjwx.'],
    ['#$%^&*()', '#$%^&*()']
    ])
# These are the same tests used in the tests.py file.

##Old code: This behaved the way I expected it to.
# for plaintext, cryptotext in tests.items():
#     print("PLAIN", plaintext)
#     print("CRYPT", cryptotext)
#     print("SHFT5", shift5(plaintext))

for P, C in tests.items():
    if shift5(P) == C:
        # encrypt input string
        # test if the output of shift5 is identical to expected encrypted string
        CONDITION = True
    else:
        CONDITION = False
        break
print(CONDITION)
#CONDITION should be true if all the tests pass
#This test works for me. 

#This code worked as expected for me. I think my code is working fine? Very confusing why I'm still getting errors on github tests.
