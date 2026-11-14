#Import Library
#from openai import OpenAI

from google import genai

#Establish Connection
client =genai.Client(api_key="Your API KEY")
#Invoke LLM
def call_llm(prompt):
    response = client.models.generate_content(
        model= "gemini-2.5-flash",
        contents = prompt
    )
    return response.output_text

#Asking for user input
user_input =input("Enter your instruction :")  
print("**********User Input********") 
print(user_input) 

# Calling the function
 
result = call_llm(user_input)
print("**********Ai Response********") 
print(result) 
