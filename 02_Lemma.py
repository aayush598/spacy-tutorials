import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('chuckles') 
print(doc[0].lemma_)