from morsecode import MORSECODE_DICT

text = input('Enter text to convert: ').upper()
converted_morsecode = ''

for letter in text:
    converted_morsecode += MORSECODE_DICT[letter] + ' '

print(converted_morsecode)
