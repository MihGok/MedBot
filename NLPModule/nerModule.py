from transformers import pipeline


class NERModule():
    def __init__(self, model_name="HUMADEX/english_medical_ner"):
        self.pipeline = pipeline("ner", model_name)

    def get_entities(self, text):
        entities = self.pipeline(text)
        return entities

    def process_entities(self, entities):
        words = []
        for elem in entities:
            if "##" in elem["word"]:
                elem["word"] = elem["word"].replace("##", "")
                words[-1] += (elem["word"])
            else:
                words.append(elem["word"])
        return words
