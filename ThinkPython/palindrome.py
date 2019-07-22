def pal_first(word):
    return word[0]

def pal_last(word):
    return word[-1]

def pal_middle(word):
    return word[1:-1]

def palindrome(word):
    if word == word[::-1]:
        print ('回文です')
    else:
        print ('回文じゃないです')
