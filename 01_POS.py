import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("I am learning.")
for token in doc:
    print(token.text, token.pos_)