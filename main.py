import spacy
import nltk
from nltk.corpus import brown
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_md", disable=["parser", "ner"])

nlp.max_length = 650000

# made it these categories to limit tokens in brown corpus
categories = ['fiction', 'Mystery'] 
word_list = brown.words(categories=categories)

# boring stuff we have to do to limit words
word_list = word_list[:50000]
text = ' '.join(word_list)
doc_text = nlp(text)

# Word list that has no punctuation and no stop words :) 
filtered_words = []

for token in doc_text:
    if token.text.lower() not in STOP_WORDS and token.is_alpha and (token.pos_ in {'NOUN', 'VERB', 'PROPN'}): # cant remember if it can be a verb too?
        filtered_words.append(token.text.lower())

# example of the list
print(filtered_words[:30])