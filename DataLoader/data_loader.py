import pandas as pd


class Datamodule:
    def __init__(self, data_name="Symptom2Disease.csv"):
        self.data_name = data_name

    def load(self):
        self.data = pd.read_csv(self.data_name)
        self.labels = set(self.data["label"])
        self.text = self.data["text"]
