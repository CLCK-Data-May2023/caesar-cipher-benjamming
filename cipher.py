#General functions
def make_key(alphabet:str, shift:int) -> dict:
    """Rotate alphabet to the right by shift spaces, map alphabet letters to shfted letters"""
    alphabet_length = len(alphabet)
    shift %= alphabet_length
    key = dict()
    for index, letter in enumerate(alphabet):
        key[letter] = alphabet[(index + shift) % alphabet_length]
    return key

def shift_text(text:str, key:dict) -> str:
    """Shift characters in string according to the rules in key;
    Ignores characters not in key"""
    output = list()
    for character in text:
        output.append(key.get(character, character))
    return ''.join(output)

### Code for assignment
lowercases = 'abcdefghijklmnopqrstuvwxyz'

shift5_key = make_key(lowercases, 5)
def shift5(text):
    """Rotate the letters in text right by 5 letters alphabetically"""
    return shift_text(text, shift5_key)

def test_function():
    test_string1 = "python is fun!"
    encrypted_string1 = "udymts nx kzs!"
    print(encrypted_string1 == shift5(test_string1))

def assignment_function():
    print("The encrypted sentence is: ",
          shift5(input("Please enter a sentence: ")), sep='')
    
#test_function()
assignment_function()
    