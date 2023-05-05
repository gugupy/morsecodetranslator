# Morse Code Translator

[![dot-dash](dotdash.png)](https://en.wikipedia.org/wiki/Morse_code)

[![codecov](https://codecov.io/gh/gugupy/morsecodetranslator/branch/master/graph/badge.svg?token=TG5AR36QNI)](https://codecov.io/gh/gugupy/morsecodetranslator)

Its converts plain text to morse code and vice versa and follows below rules for the conversion as per the morse-code algorithm,  
1. Single space for same char repeats  
2. Three spaces for different char  
3. Seven spaces to differentiate the word  

## Installation

### Method 1:
To install the MorseCodeTranslator just run the command `pip install -U morse-transcript`

### Method 2:
1. Clone the repository `git clone https://github.com/gugupy/morsecodetranslator.git`
2. Run the command `pip install -e .`


## Sample code
```python
from morsecodetranslator.morse import MorseCodeTranslator

mct = MorseCodeTranslator()
print(mct.encrypt('MORSE CODE'))
print(mct.decrypt('--   ---   .-.   ...   .       -.-.   ---   -..   .'))
```
### output
``` textmate
--   ---   .-.   -.-.   .       -.-.   ---   -..   .  
MORSE CODE
```
