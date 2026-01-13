text = "heLLo PytHoN"
text1 = "hello123"
num = "123"

print("Original word: ", text)

capitalize = text.capitalize()
print("Captilaize: ", capitalize)

lowercase = text.lower()
print("Lowercase: ", lowercase)

uppercase = text.upper()
print("Uppercase: ", uppercase)

word_count = text.count('h')
print("Word Count: ", word_count)

starts_with = text.startswith('hello')
print("Word starts with: ", starts_with)

ends_with = text.endswith('python')
print("Word ends with: ", ends_with)

name = 'SK'
age = 35
message = "My name is {} and I am {} years old".format(name, age)
print("Words format: ", message)

index_of_word = text.index('o')
print("Index of letter: ", index_of_word)

find_word = text.find('w')
print("Find letter: ", find_word)

is_alpha_num = text1.isalnum()
print("IsAlNum: ", is_alpha_num)

is_alpha = text1.isalpha()
print("IsAlpha: ", is_alpha)

is_num = num.isnumeric()
print("IsNum: ", is_num)

is_decimal = num.isdecimal()
print("IsDecimal: ", is_decimal)

is_digit = num.isdigit()
print("IsDigit: ", is_digit)

is_lowercase = text.islower()
print("IsLowercase: ", is_lowercase)

is_uppercase = text.isupper()
print("IsUppercase: ", is_uppercase)

word = ["Hello", "Python"]
joined_word = ' '.join(word)
print("Joined words: ", joined_word)

replace_word = text.replace("PytHoN", "World")
print("Replace words: ", replace_word)

text3 = "  Hello  Python  "
strip_word = text3.strip()
print("Strips word: ", strip_word)

split_word = text.split()
print("Splits word: ", split_word)

partition_word = text.partition(" ")
print("Partition words: ", partition_word)

text4 = "hello\nworld"
split_the_lines = text4.splitlines()
print("Split the lines ", split_the_lines)

zfill_zeros = num.zfill(6)
print("zfill numbers: ", zfill_zeros)

text5 = "hello@097"
encode_words = text5.encode()
print("Encode words: ", encode_words)

remove_prefix = text.removeprefix("heLLo ")
print("Remove prefix: ", remove_prefix)

remove_suffix = text.removesuffix(" PytHoN")
print("Remove suffix: ", remove_suffix)

