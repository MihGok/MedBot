from langchain_together import ChatTogether


def multiply(a: int, b: int) -> int:
    return a * b


class LLM_Model():
    def __init__(self, model_name: str, api_key: str, prompt: str):
        self.client = ChatTogether(
            model=model_name,
            temperature=0,
            api_key=api_key,
            max_tokens=None,
            timeout=None
        )
        self.prompt = prompt

    def generate_responce(self, state: str):
        messages = [
            ("system", self.prompt),
            ("human", ", ".join(state["entities"]))
        ]
        ai_msg = self.client.invoke(messages)
        state["final_symptoms"] = ai_msg.content
        return state
