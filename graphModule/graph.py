from DataLoader.data_loader import Datamodule
from NLPModule.nerModule import NERModule
from LLMModule.LLMModule import LLM_Model
from dotenv import load_dotenv
import os
from LLMModule.LLM_output_transformer import Output_transfromer
from ValidationModule.validator import Validator
from typing import Literal

load_dotenv()
prompt = """
You are a symptom grouping assistant.
You only need to group input tags into symptom phrases—avoid giving advice or adding any extra words.
Be very precise and accurate.
Input: a Python list of extracted entity tokens.
Task: Combine adjacent tokens into meaningful symptom phrases; remove filler tokens (e.g. 'and', ',', 'on').
Output: a JSON array of strings; do not add any explanatory text or punctuation outside the JSON.

Example:
  Input: ['a', 'skin', 'rash', 'on', 'my', 'arms', ',', 'legs', ',', 'and', 'torso',
          'red', 'itchy', 'dry', ',', 'scaly', 'patches']
  Output: ["a skin rash on my arms, legs, and torso", "red itchy dry scaly patches"]
"""



def load_data(state):
    data_module = Datamodule()
    data_module.load()
    state["text"] = data_module.text[15]
    return state


def process_text(state):
    ner_Model = NERModule()
    entities = ner_Model.get_entities(state["text"])
    state["entities"] = ner_Model.process_entities(entities)
    return state


def get_LLM_responce(state):
    api_key = os.getenv("TOGETHER_API_KEY")
    model_name = os.getenv("TOGETHER_MODEL_NAME")
    model = LLM_Model(api_key=api_key, model_name=model_name, prompt=prompt)
    model.generate_responce(state)
    return state


def transform_grouping_output(state):
    type_transfromer = Output_transfromer()
    type_transfromer.change_type(state)
    return state


def perform_basic_check(state):
    validator = Validator()
    validator.basic_check(state)
    validator.word_containment_check(state)
    return state


def final_node(state):
    print("Success")
    return state
