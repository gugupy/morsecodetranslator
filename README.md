# Morce Code Translator

Its converts plain text to morce code and vice versa and follows below rules for the convertion as per the morce-code algorithm,  
1. Single space for same char repeats  
2. Three spaces for different char  
3. Seven spaces to differentiate the word  

## Installation
To install the MorceCodeTranslator just clone the code and run below command 
```pip install -e .```

## Sample code
```
from morcecodetranslator.morce import MorceCodeTranslator

mct = MorceCodeTranslator()
print(mct.encript('MORCE CODE'))
print(mct.decript('--   ---   .-.   -.-.   .       -.-.   ---   -..   .'))
```
### output
```
--   ---   .-.   -.-.   .       -.-.   ---   -..   .  
MORCE CODE
```
