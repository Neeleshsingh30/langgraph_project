from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    name: str
    greeting: str

def name_node(state: State):
    return {
        "name": state["name"]
    }

def greeting_node(state: State):
    return {
        "greeting": "Hello " + state["name"] + "!"
    }

builder = StateGraph(State)
builder.add_node("name_node", name_node)
builder.add_node("greeting_node", greeting_node)

builder.add_edge(START, "name_node")
builder.add_edge("name_node", "greeting_node")
builder.add_edge("greeting_node", END)

graph = builder.compile()

result = graph.invoke({"name": "Rahul", "greeting": ""})
print(result)