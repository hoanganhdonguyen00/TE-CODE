def word_frequency(text, target_word):
    thgxuyen = {}
    words = text.split()
    for word in words:
        s = word.strip().lower()
        thgxuyen[s] = thgxuyen.get(s, 0) + 1
    return thgxuyen.get(target_word.strip().lower(), 0)
text = "1 2 3 2 5 1"
print(word_frequency(text, "1"))
