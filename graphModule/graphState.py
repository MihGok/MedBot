from typing_extensions import TypedDict


class State(TypedDict):
    text: str
    entities: list
    final_symptoms: list
    basic_check_result: bool
