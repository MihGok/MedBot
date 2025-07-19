class Validator():
    def basic_check(self, state):
        self.result = state["final_symptoms"]
        self.entities = state['entities']
        self.calculate_groups()
        if self.word_count != len(self.entities):
            state["basic_count_check_result"] = False
        else:
            state["basic_count_check_result"] = True
        return state

    def calculate_groups(self):
        self.group_number = len(self.result)
        self.word_count = sum([len(self.result[i].split(" ")) for i in range(self.group_number)])

    def word_containment_check(self, state):
        self.list_of_symptoms = (
            [word for phrase in state["final_symptoms"] for word in phrase.split()]
        )
        for elem in state["entities"]:
            if elem not in self.list_of_symptoms:
                state["basic_conteinment_check_result"] = False
                return state
        state["basic_conteinment_check_result"] = True
        return state
