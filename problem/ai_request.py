from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


def aicall(payload:list, action:str):

    query = '\n'.join(string for string in payload if string != '')

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=query,
        )

        return response.text
    except Exception as e:
        return f"An error occurred while communicating with the AI. {e}"