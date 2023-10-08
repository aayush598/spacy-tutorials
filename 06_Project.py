import spacy

nlp = spacy.load('en_core_web_sm')


responses = {
    "greeting": "Hello! I am Aayushi , a chatbot. How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that."
}

print(responses["greeting"])

x = input()

doc = nlp(x)

for token in doc:
    if (token.pos_ =='VERB'):
        if (token.lemma_ == "book"):
            print("We have booked.Thanks for the booking.")
        elif (token.lemma_ == "cancel"):
            print("We have canceled your booking")

print("Thanks for using our sevices.")