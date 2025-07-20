import pandas as pd
from random import randint


class Datamodule:
    def __init__(self, data_name="Symptom2Disease.csv"):
        self.data_name = data_name

    def load(self):
        with open("complainments.txt") as file:
            lines = file.readlines()
            number = randint(0, len(lines) - 1)
            print(number, len(lines))
            self.text = lines[number]
            print(self.text)
