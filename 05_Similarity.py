import spacy
nlp = spacy.load('en_core_web_sm')

hello_doc = nlp("hello")
hi_doc = nlp("hi")
hella_doc = nlp("hella")

print(hello_doc.similarity(hi_doc))
print(hello_doc.similarity(hella_doc))