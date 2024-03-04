import spacy
import stanza

stanza_nlp = stanza.Pipeline('es')
spacy_nlp = spacy.load('es_core_news_lg', disable=['parser', 'ner'])
text = "Soy un texto. Normalmente soy más largo y más grande. Que no te engañe mi tamaño."
print([ token.lemma_ for token in spacy_nlp(text)])
print([ word.lemma for sentence in stanza_nlp(text).sentences for word in sentence.words])