from typing_extensions import TypedDict
from typing import Annotated
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider = "openai"
)

class State(TypedDict):
    messages : Annotated[list, add_messages]
    

def chatbot(state : State):
    # print("\n\n\nInside chatbot node", state)
    response = llm.invoke(state.get("messages"))
    return {"messages" : [response]}


def samplenode(state : State):
    print("\n\n\nInside sample node", state)
    return {"messages" : ["Sample message Appended"]}
    


graph_builder = StateGraph(State)



graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)


graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages" : ["Hi, my name is Purnesh Kalavagunta"]}))

print(f"\n\nUpdated State is : {updated_state}")


# If initial state = {messages : ["Hey There"]}
# Then Node runs : chatbot(state : ["Hey There"]) -> ["Hi, this is a message from chatbot"]
# Now state becomes : {"messages" : ["Hey There", "Hi, this is a message from chatbot"]}