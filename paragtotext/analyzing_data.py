import spacy

def For_noun_verb_adj_from_article(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    verbs = [token.text for token in doc if token.pos_ == "VERB"]

    dialogue_info = []

    line_info = {'nouns': nouns, 'verbs': verbs, 'adjectives': adjectives}

    dialogue_info.append(line_info)

    return dialogue_info