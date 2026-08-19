import os
from dotenv import load_dotenv
from google import genai


# Load .env
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")


# Create Gemini client
client = genai.Client(api_key=api_key)


def chatbot_response(user_message):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_message
    )

    return response.text

