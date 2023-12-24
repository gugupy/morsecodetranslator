import re

__all__ = "MorseCodeTranslator"


class MorseCodeTranslator:
    """
    Morse code translator convert text to morse code and vice versa.
    Its follow below algorithm for the conversion as per the morse-code,
        1. Single space for same char follows
        2. Three spaces for different char
        3. Seven spaces to differentiate the word
    """

    def __init__(self):
        self.__MORSE_CODE = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
        }

    def encrypt(self, message) -> str:
        """
        Encrypt text to morse code

        :param message: message for convert to morse code
        :return: morse code
        """

        morse_code = ""
        _pre_char = None

        for char in str(message).upper():
            # Evaluating space to separate the word
            if char == " ":
                morse_code += "       "
                # reset the previous char to None
                # To avoid append space to the morse code
                # on the next word cycle
                _pre_char = None
                continue
            # Checking previous char is current char
            # To add spaces based on the morse algorithm
            if _pre_char:
                if str(_pre_char).__eq__(char):
                    morse_code += " "
                else:
                    morse_code += "   "

            try:
                morse_code += self.__MORSE_CODE.get(char)
            except TypeError:
                print(f'"{char}" is not a valid text to get Morse Code!')
                exit(1)

            _pre_char = char
        return morse_code

    def decrypt(self, morse_code) -> str:
        """
        Decrypting the morse code to text

        :param morse_code: morse code for convert to text
        :return: Plain text of equivalent morse code
        """
        message = ""

        # Splitting the morse based more than 4 spaces
        # So its exactly split the words
        mc_li = re.split(r"\s\s\s\s+", morse_code)
        for mc in mc_li:
            if mc == "":
                continue
            codes = re.split(r"\s+", mc)
            for code in codes:
                try:
                    idx = list(self.__MORSE_CODE.values()).index(code)
                    message += list(self.__MORSE_CODE.keys())[idx]
                except ValueError:
                    print(f'"{code}" is not a valid Morse Code! ')
                    exit(1)

            message += " "
        return message.removesuffix(" ")


if __name__ == "__main__":
    mct = MorseCodeTranslator()
    print(mct.encrypt("MORSE CODE"))
    print(mct.decrypt("--   ---   .-.   ...   .       -.-.   ---   -..   ."))
