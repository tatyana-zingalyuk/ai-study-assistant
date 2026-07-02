from openai import OpenAI
import os
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT
from config import MODEL_NAME
import streamlit as st

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if API_KEY is None:
    API_KEY = st.secrets.get("OPENROUTER_API_KEY")

if API_KEY is None:
    raise ValueError("API key not found.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

def generate_response(
        topic: str,
        level: str,
        goal: str) -> str:
    try:
        user_prompt = f"""
            Create a personalized study plan using the following information.

            Topic:
            {topic}
            Current Level:
            {level}
            Learning Goal:
            {goal}
        """        

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages = [
                {
            "role": "system",
            "content": SYSTEM_PROMPT
            },
            {
            "role": "user",
            "content": user_prompt
            }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error:\n\n{str(e)}"

