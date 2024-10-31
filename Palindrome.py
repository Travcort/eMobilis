from Reverse import reverse_string
def is_palindrome(word):
    word = word.lower()

    return word == reverse_string(word)

print(is_palindrome('level'))