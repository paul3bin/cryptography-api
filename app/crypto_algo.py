from pandas import DataFrame


class CaesarCipher:

    def __init__(self, text, key) -> None:
        self.text = text
        self.key = key

    def decrypt(self):
        decipheredText = ""
        for ch in self.text.upper():
            if ch.isalpha():
                newchar = ord(ch)-self.key
                if newchar < ord('A'):
                    newchar += 26
                newShiftedALphabet = chr(newchar)
                decipheredText += newShiftedALphabet
        return decipheredText.upper()

    def encrypt(self):
        cipherText = ""
        for ch in self.text.upper():
            if ch.isalpha():
                alphabetInString = ord(ch) + self.key
                if alphabetInString > ord('Z'):
                    alphabetInString -= 26
                shiftedAlphabet = chr(alphabetInString)
                cipherText += shiftedAlphabet
        return cipherText.upper()


class VigenereCipher:

    # Initialization funtion
    def __init__(self, text, key):

        # creating a list of character from the given text and key in upper case.
        txt = list(text.upper())
        ky = list(key.upper())

        # Removing the white space characters.
        for char in txt:
            if char == ' ':
                txt.remove(char)
        # Removing white spaces from the key
        for char in ky:
            if char == ' ':
                ky.remove(char)

        self.text = txt
        self.key = ky

    # Function that encrypts the given plain text using given key.
    def encrypt(self):
        cipher_text, j = [], 0
        for i in range(len(self.text)):
            if j < len(self.key):
                character = (
                    (ord(self.text[i])+ord(self.key[j])) % 26)+ord('A')
                j += 1
            else:
                j = 0
                character = (
                    (ord(self.text[i])+ord(self.key[j])) % 26)+ord('A')
                j += 1

            cipher_text.append(chr(character))
        return ''.join(cipher_text)

    # Function that decrypts the given plain text using given key.
    def decrypt(self):
        plain_text, j = [], 0
        for i in range(len(self.text)):
            if j < len(self.key):
                character = (
                    (ord(self.text[i])-ord(self.key[j])+26) % 26)+ord('A')
                plain_text.append(chr(character))
                j += 1
            else:
                j = 0
                character = (
                    (ord(self.text[i])-ord(self.key[j])+26) % 26)+ord('A')
                plain_text.append(chr(character))
                j += 1

        return ''.join(plain_text)


class MorseCode:
    # Function that returns value or key from morse_dict dictionary
    def getDictItems(self, val, option):
        morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..',
                      '0': '-----', '1': '.----', '2': '..--', '3': '...--', '4': '....-',
                      '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                      '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.',
                      '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
                      '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '$': '...-..-', '@': '.--.-.'}
        if option == 1:
            return morse_dict[val]

        elif option == 2:
            for key, value in morse_dict.items():
                if val == value:
                    return key

    # Function to encrypt given message
    def encrypt(self, message):
        cipherText = ''
        for character in message:
            if character == ' ':
                cipherText += '/ '
            else:
                cipherText += self.getDictItems(character, 1)
                cipherText += ' '
        return cipherText[:-1]

    # Function to decrypt given cipher text
    def decrypt(self, message):
        plainText = ''
        characterList = message.split(' ')
        for character in characterList:
            if character == '/':
                plainText += ' '
            else:
                plainText += self.getDictItems(character, 2)
        return plainText


class RunningKeyCipher:

    def __init__(self, plainText, key):
    # converting the plain text and key to upper case
        self.pt = list(plainText.upper())
        self.ky = list(key.upper())

        # removing spaces in key and plain text
        for char in self.ky:
            if char == ' ':
                self.ky.remove(char)
        for char in self.pt:
            if char == ' ':
                self.pt.remove(char)

        # creating a DataFrame of size 26x26
        tab, tableau = [chr(a) for a in range(65, 91)], []
        for i in range(26):
            a = tab[i:]+tab[:i]
            tableau.append(a)
        self.tabulaRecta = DataFrame(tableau, index=tab, columns=tab)

    def encrypt(self):
        encryptedText = ''
        for i in range(len(self.pt)):
            encryptedText += self.tabulaRecta.values[ord(self.pt[i])-65][ord(self.ky[i])-65]
        return encryptedText
    
    def decrypt(self):
        decryptedText = ''
        for i in range(len(self.pt)):
            decryptedText += ''.join(
                self.tabulaRecta[self.tabulaRecta[self.ky[i]] == self.pt[i]].index.values)
        return decryptedText
