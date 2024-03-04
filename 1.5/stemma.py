from nltk import SnowballStemmer
from nltk.tokenize import ToktokTokenizer

tokenizer = ToktokTokenizer()

snowball_stemmer = SnowballStemmer(language="spanish")
texts = ("Soy un texto que pide a gritos que lo procesen.", "Por eso yo canto, tú cantas, ella canta, nosotros cantamos, cantáis, cantan")
sample_sentences = tokenizer.tokenize_sents(texts)
sample_stems = [snowball_stemmer.stem(word) for sentence in sample_sentences for word in sentence]
print(sample_stems)