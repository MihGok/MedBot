from graphModule.graph import load_data, process_text, get_LLM_responce, transform_grouping_output
from graphModule.graph import perform_basic_check, final_node
from graphModule.graphState import State
from langgraph.graph import StateGraph
from ValidationModule.validationReviewer import ValidationReviewer
reviewer = ValidationReviewer()

builder = StateGraph(State)
builder.add_node("text_loader", load_data)
builder.add_node("text_processor", process_text)
builder.add_node("symptomps_grouping", get_LLM_responce)
builder.add_node("grouping_transformer", transform_grouping_output)
builder.add_node("basic_validator", perform_basic_check)
builder.add_node("final_node", final_node)
builder.add_node("validation_reviewer", ValidationReviewer().decide)


builder.set_entry_point("text_loader")
builder.set_finish_point("final_node")


builder.add_edge("text_loader", "text_processor")
builder.add_edge("text_processor", "symptomps_grouping")
builder.add_edge("symptomps_grouping", "grouping_transformer")
builder.add_edge("grouping_transformer", "basic_validator")

builder.add_conditional_edges(
    "basic_validator",
    reviewer.decide,
    path_map={
        "final_node": "final_node",
        "symptomps_grouping": "symptomps_grouping"
    }
)

graph = builder.compile()
print(graph.get_graph().draw_ascii())
result = graph.invoke(input={
    "text": "",
    "entities": "",
    "final_symptoms": "",
    "basic_conteinment_check_result": "",
    "basic_count_check_result": ""
})
print(result)
