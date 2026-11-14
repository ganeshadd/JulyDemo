#AutoGen Demo
from autogen import UserProxyAgent,AssistantAgent
from dotenv import load_dotenv

load_dotenv()
import os
os.environ["OPENAI_API_KEY"]="Your API Key"
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set.")

config_list = [
    {
        "model": "gpt-4o-mini",
        "api_key": api_key,
        "temperature": 0.1,
    }
]

assitant =AssistantAgent(
    name="assistant",
    llm_config={"config_list":config_list}
)
user_proxy =UserProxyAgent(
    name='user',
    llm_config={"config_list":config_list},
    code_execution_config=False
)

user_proxy.initiate_chat(assitant,message='Analyze an idea and bring up an execution plan to start electric vehicle manufactuting at Tesla after performing copetitor analysis')

