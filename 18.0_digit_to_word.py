number_mapping ={'1' :'one','2' :'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

input_digit = input('> ')
result = ''

for digit in input_digit:
    converted = number_mapping.get(digit)
    result =  result + ' ' +converted
print(result)