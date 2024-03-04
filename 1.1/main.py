# Examples of text preprocessing using some famous text corpus
from nltk.corpus import gutenberg
from collections import Counter
import re

bible = gutenberg.open('domcs.txt')
bible = bible.readlines()

bible_wo_nl = [line.strip('\n') for line in bible]

bible_wo_el = list(filter(None, bible_wo_nl))

line_lengths = [len(sentence) for sentence in bible_wo_el]

line_tokens = [sentence.split() for sentence in bible_wo_el]

words =[ word for token_sentence in line_tokens for word in token_sentence]

words_clean = [ re.sub(r'[^A-Za-z]','', word).lower() for word in words]

words_clean = list(filter(None, words_clean))

c = Counter(words_clean)
print("Most common words in text corpus:")
print(c.most_common(10))

