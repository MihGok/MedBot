import re


class Output_transfromer():
    def __init__(self):
        pass

    def change_type(self, state):
        input = state["final_symptoms"]
        input = input[2:-2]
        input = re.sub("'", '', input)
        input = re.sub('"', '', input)
        input = input.split(",")
        input = self.get_final_list(input)
        state["final_symptoms"] = input
        return state

    def get_final_list(self, list_of_symptoms):
        final_list = []
        for elem in list_of_symptoms:
            if elem[0] == " ":
                final_list.append(elem[1:])
            else:
                final_list.append(elem)
        return final_list
