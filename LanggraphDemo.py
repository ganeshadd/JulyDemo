from langgraph.graph import StateGraph
from openai import OpenAI


client=OpenAI(api_key="Your API Key")

def call_llm(prompt):
    response= client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    return response.choices[0].message.content


#Step 1: Research Agent
def research(state):
    query= state["query"]
    prompt=f"Find out the top compititors of :{query}"
    print("Research is completed")
    return{"data":call_llm(prompt)}

#Step 2:Analyze
def analyze(state):
    prompt=f"Analyze the stenghts and weaknesses of :{state['data']}"
    print("Analysis is complete.")
    return{"Analysis":call_llm(prompt)}

#Step 3:Summarize and report
def summarize(state):
    prompt=f"Summarize the market trends for:{state['Analysis']},give me the outputin a structured Json format"
    print("Summarization is complete.")
    return{"Summary":call_llm(prompt)}

graph =StateGraph(dict)
#Added the nodes
graph.add_node("Research",research)
graph.add_node("Analyze",analyze)
graph.add_node("Summary",summarize)


#Added the edges
graph.set_entry_point("Research")
graph.add_edge("Research","Analyze")
graph.add_edge("Analyze","Summary")

app =graph.compile()

result = app.invoke({"query":"Smart phone"})

print("Here is the result of analysis :",result)

