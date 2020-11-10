import re
import pandas as pd
import spacy
import en_core_web_sm
from spacy import displacy


class NER:

    _ENTITY_DICT = {
        "PERSON": "Person",
        "NORP": "Nationalities, Religious Groups, Political Groups",
        "FAC": "Building, airports, highways, bridges",
        "ORG": "Companies, agencies, institutions",
        "GPE": "Countries, cities, states",
        "PRODUCT": "Products",
        "WORK_OF_ART": "Titles of songs, books, movies etc",
        "LAW": "Law Documents",
        "LANGUAGE": "Language",
        "MONEY": "Money",
    }

    def __init__(self, raw_text, choice):
        self.text = raw_text
        self.choice = choice
        self.results = {}
        self.nlp = en_core_web_sm.load()

    def process_text(self):
        document = self.nlp(self.text)
        data = []
        for entity in document.ents:
            data.append((entity.label_, entity.text))

            df = pd.DataFrame(data, columns=["Entity Name", "Output"])

            for k, v in self._ENTITY_DICT.items():
                self.results[k] = df.loc[df["Entity Name"] == k]["Output"]

        if self.choice in self.results:
            result = self.results[self.choice]
            return result, len(result)
        else:
            return None, 0

