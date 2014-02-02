# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

import json

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    max_len = 1
    longest_s = 0
    longest_e = 0
    text = text.lower()
    
    for i in range(len(text)):
        s = e = i # start and end positions
        while e < len(text) and text[s] == text[e]: e += 1 # search for the same character i.e. 'BBBB'
        #        print 'Char is %s, s = %d, e = %d' % (text[s:e], s, e)

        j = 1
        while (s - j) >= 0 and (e + j - 1) < len(text) and text[s - j] == text[e + j - 1]: j += 1

        if (e + j - 1) - (s - j + 1) > max_len:
                #   print 'I = %d, max_len = %d, longest_e = %d, longest_s = %d' % (i, max_len, e + j - 1, s - j + 1)
            longest_e = e + j - 1
            longest_s = s - j + 1
            max_len = longest_e - longest_s

    return (longest_s, longest_e)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    assert L('MabbaJ') == (1, 5)
    assert L('Able was I ere I saw Elba') == (0, 25)
    assert L('Mississipi') == (1, 8)
    return 'tests pass'

# print test()

texxt = RecString('Hello World!')
print longest_subpalindrome_slice(texxt)
print texxt.get_recording_link()

class RecString(str):
    def __init__(self, text):
        self.steps = [text]
        self.index = 0

    def get_recording_link(self):
        return ('http://explored.tk/experiments/palindrome#[%s]' %
                json.dumps(self.steps, separators=(',',':')))

    def __eq__(self, other):
        if other is '':
            return not len(self)

        if len(self) != 1 or len(other) != 1 or not isinstance(other, RecString):
            self.error()

        equal = str.__eq__(self, other)
        self.steps.append(['c', self.index, other.index, 1 if equal else 0])
        return equal

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, *args):
        if (len(args) > 1):
            self.error()
        else:
            return self.baby(str.__getitem__(self, *args), args[0])

    def __getslice__(self, *args):
        self.error()

    def lower(self):
        return self.baby(str.lower(self), self.index)

    def upper(self):
        return self.baby(str.upper(self), self.index)

    def baby(self, text, index):
        baby = RecString(text)
        baby.steps = self.steps
        baby.index = index
        return baby

    def error(self):
        raise Exception("""
        Please access only individual characters: e.g. text[a]
        Comparisons such as text == text[::-1] are O(n),
        do them explicitly one character at a time.
        """)
