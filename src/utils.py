import spacy
from nltk.corpus import brown
from spacy.lang.en.stop_words import STOP_WORDS
import random

def get_vocab(vocab_size: int) -> list[str]:
    total_words = 2*vocab_size+vocab_size+1
    nlp = spacy.load("en_core_web_md", disable=["parser", "ner"])
    nlp.max_length = 650000

    # made it these categories to limit tokens in brown corpus
    categories = ['fiction', 'Mystery'] 
    word_list = brown.words(categories=categories)

    # boring stuff we have to do to limit words
    text = ' '.join(word_list)
    doc_text = nlp(text)

    # Word list that has no punctuation and no stop words :) 
    filtered_words = []
    while len(filtered_words) < total_words:
        token = random.choice(doc_text)
        if token.text.lower() not in STOP_WORDS and token.is_alpha and (token.pos_ in {'NOUN', 'VERB'}) and len(token.text.lower()):
            filtered_words.append(token.text.lower())
    return filtered_words





if __name__ == "__main__":
    vocab = get_vocab(10)
    print(vocab)
