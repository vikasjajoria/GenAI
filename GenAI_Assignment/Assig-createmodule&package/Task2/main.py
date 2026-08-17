import string_utils

# test word capitalize_word()
print("Capitalize:", string_utils.captialize_word("hello_word"))

# test reverse string
print("Reverse String:", string_utils.reverse_string("Vikas"))

# test word string
print("Word String:", string_utils.word_string("Python is easy to learn"))



# Test all cases
print("\n--- Testing All Cases ---")

# capitalize_word()
print(string_utils.capitalize_word("hello python"))
print(string_utils.capitalize_word("vikas kumar"))
print(string_utils.capitalize_word("python programming language"))

# reverse_string()
print(string_utils.reverse_string("hello"))
print(string_utils.reverse_string("Python"))
print(string_utils.reverse_string(""))

# word_string()
print(string_utils.word_string("Hello World"))
print(string_utils.word_string("Python is easy"))
print(string_utils.word_string(""))