import spacy

text = ' Hi There'
nlp = spacy.load('en_core_web_lg')
doc = nlp(text)

for token in doc:
    print(token)



