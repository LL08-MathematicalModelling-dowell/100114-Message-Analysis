import re
import spacy

def extract_noun_verbs_adjective(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    verbs = [token.text for token in doc if token.pos_ == "VERB"]

    return {'nouns': nouns, 'verbs': verbs, 'adjectives': adjectives}

def organize_text_by_time(input_text):
    dialogue_info = {}
    time_pattern = r'\d{1,2}:\d{2}[apmAPM]{2}'

    matches = re.finditer(time_pattern, input_text)
    matches = [match.group() for match in matches]

    # Split the input text using time as a delimiter
    segments = re.split(time_pattern, input_text)
    segments = [segment.strip() for segment in segments]

    for time, text in zip(matches, segments[1:]):  # Skip the first empty segment
        full_text = text + ' ' + segments[0]
        tags = extract_noun_verbs_adjective(full_text)
        dialogue_info[time] = {"text": full_text, **tags}

    return dialogue_info

# input_text = """
# Nadeem — 9:24am
# Joint diplomatic statement issued by multiple countries' governments concerning recent violence and gatherings.
# Jacobninandowell — 9:45am
# This is concerning.
# """

# Call the function with the input text
# result = organize_text_by_time(input_text)

# Print the organized information in the desired format
# for key, value in result.items():
#     print(f"{key}: {value}")
