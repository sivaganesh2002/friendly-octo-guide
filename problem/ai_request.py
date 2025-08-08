from google import genai
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


def aicall(payload:list, action:str):

    query = '\n'.join(x for x in payload if x)

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=query,
        )

        return response.text
    except Exception as e:
        return f"An error occurred while communicating with the AI. {e}"