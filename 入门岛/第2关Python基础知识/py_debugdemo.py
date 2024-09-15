import re
from collections import defaultdict

def wordcount(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()

    word_freq = defaultdict(int)

    for word in words:
        word_freq[word] += 1 

    return dict(word_freq)  


text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

print(wordcount(text))