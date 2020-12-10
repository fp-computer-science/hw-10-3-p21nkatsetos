# Author: NJK (AMDG) 12/9/20

def three_letter_words(lst):
    word_count = 0
    while word_count == lst:
        if len(word_count) == 3:
            word_count += 1
    return word_count

print(three_letter_words(["cat", "bat", "apple"]))
print(three_letter_words(["apple", "hippo", "mouse"]))
print(three_letter_words(["hop", "pop", "bop"]))
