from morsecode import MORSECODE_DICT

text = input('Enter text to convert: ').upper()
converted_morsecode = ''

for letter in text:
    if letter != ' ':
        converted_morsecode += MORSECODE_DICT[letter]
        converted_morsecode += ' '
    else:
        converted_morsecode += ' '


print(converted_morsecode)
