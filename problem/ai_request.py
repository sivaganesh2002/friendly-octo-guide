from google import genai
from google.genai import types

import os
from dotenv import load_dotenv


def aicall(payload:list[str], action):

    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')

    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")

    system_prompt = [
            "You are a highly skilled programming assistant. \
            Your purpose is to help the user progress toward the correct code without giving complete solution.\
            Your task:\
                1. If the user is solving a problem, provide 1-5 concise, actionable hints that guide them toward the right code.\
                    * Focus on thought process, approach and concept rather than exact code.\
                    * Hints must be short, concise, clear and avoid any step-by-step solution.\
                2. If the user shares code, review it and give concise feedback for refactoring.\
                    * Identify key issues, suggest improvement and highlight best practices.\
                    * Feedback should be high-level and  avoid rewriting any complete code.\
            Important: \
                * Choose exactly one direction per request (either hint or code review), never both\
                * never write or rewrite the complete code.\
                * keep response concise and practical.\
                * Avoid any step-by-step solution or complete code.\
            "
        ]

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        )
    )

    user_query = ["\n".join(filter(None, (s.strip() for s in payload)))]
    
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_query,
            config=config,
        )

        return response.text
    except Exception as e:
        return f"An error occurred while communicating with the AI. {e}"