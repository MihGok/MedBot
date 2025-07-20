class ValidationReviewer():
    def __init__(self):
        pass

    def decide(self, state):
        if state["basic_count_check_result"] is True:
            if state["basic_conteinment_check_result"] is True:
                return "final_node"
        return "symptomps_grouping"
