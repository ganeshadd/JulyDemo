# Goal : "Analyze competitor pricing for a product"
# Tasks : Find competitor ,collect data,Analyze data,Generate a report
#Trying to understand GIT 

from langgraph.graph import StateGraph
from typing import TypedDict ,List


class AgentState(TypedDict):
    task:str
    data =List[str]
    report =str
    memory:List[str]

graph =StateGraph(AgentState)   

def find_competitors(state):
    return{"data":["competitor A","competitor B"]}

def collect_data(state):
    data = state.get("data",[])
    enriched =[d+ "pricing data" for d in data]
    memory =state.get("memory",[])
    memory.append("collected pricing data")
    return{"data":enriched ,"memory":memory}


def analyze_data(state):
    return{"report":"Basic price comparison"}

def generate_report(state):
    report = state.get("report","")
    return{"report": report + "Final insights Added"}

def reflect(state):
    memory =state.get("memory",[])
    if len(memory)<2:
        return{"report":"Retry needed as data is insufficient"}

    return{"report": state["report"] +"Imports after reflection"}

# Added the nodes
graph.add_node("find",find_competitors)
graph.add_node("collect",collect_data)
graph.add_node("analyze",analyze_data)
graph.add_node("report",generate_report)
graph.add_node("reflect",reflect)


# Added the edges to the flow
graph.set_entry_point("find")
graph.add_edge("find","collect")
graph.add_edge("collect","analyze")
graph.add_edge("analyze","report")
graph.add_edge("report","reflect")

app = graph.compile()

result = app.invoke({
    "task":"Analyze pricing",
    "data":"",
    "report":"",
    "memory":[]
})


print(result)