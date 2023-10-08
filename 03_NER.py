import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp("I usually wake up at 9:00 AM. 90% of my daytime goes in learning new things.")

for ent in doc.ents:
    print(ent.text, ent.label_)