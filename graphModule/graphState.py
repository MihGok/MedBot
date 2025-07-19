from typing_extensions import TypedDict


class State(TypedDict):
    text: str
    entities: list
    final_symptoms: list
    basic_count_check_result: bool
    basic_conteinment_check_result: bool
