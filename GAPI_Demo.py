from google import genai

# ============================================================
# Gemini API Configuration
# ============================================================

API_KEY = "Your API Key"

# Create Gemini client
client = genai.Client(api_key=API_KEY)


# ============================================================
# Function to call Gemini LLM
# ============================================================

def call_llm(prompt):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


# ============================================================
# Main Program
# ============================================================

def main():

    # Get input from user
    user_input = input("Enter your instruction: ")

    print("\n********** User Input **********")
    print(user_input)

    # Call Gemini
    result = call_llm(user_input)

    # Display response
    print("\n********** AI Response **********")
    print(result)


# ============================================================
# Program Entry Point to access GAPI
# ============================================================

if __name__ == "__main__":
    main()