# Morse Code Translator

[![dot-dash](dotdash.png)](https://en.wikipedia.org/wiki/Morse_code)

[![codecov](https://codecov.io/gh/gugupy/morsecodetranslator/branch/master/graph/badge.svg?token=TG5AR36QNI)](https://codecov.io/gh/gugupy/morsecodetranslator)

[//]: # (![graph]&#40;https://codecov.io/github/gugupy/morsecodetranslator/branch/master/graphs/sunburst.svg?token=TG5AR36QNI&#41;)

Its converts plain text to morse code and vice versa and follows below rules for the conversion as per the morse-code algorithm,  

1. Single space for same char repeats  
2. Three spaces for different char  
3. Seven spaces to differentiate the word  

## Installation

### Method 1

To install the MorseCodeTranslator just run the command `pip install -U morse-transcript`

### Method 2

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
--   ---   .-.   ...   .       -.-.   ---   -..   .  
MORSE CODE
```

## CLI for morse code

### Usage

```textmate
usage: morse [-h] {encrypt,decrypt} ...

Convert plain text to morse code and vise-versa.

positional arguments:
  {encrypt,decrypt}  sub-commands

optional arguments:
  -h, --help         show this help message and exit

Morse Code Converter
```

``` bash
morse encrypt --text 'MORSE CODE'
morse decrypt --morse-text '--   ---   .-.   ...   .       -.-.   ---   -..   .'
```

## Run Codecov

```textmate
pytest --cov=tests --cov-report term --cov-report xml:coverage.xml
./codecov -t ${CODECOV_TOKEN}
```
