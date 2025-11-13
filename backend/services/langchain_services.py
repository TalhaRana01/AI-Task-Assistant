# backend/services/langchain_service.py

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from typing import Optional

load_dotenv()  # Load environment variables from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Chat Model
chat_model = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    model_name="gpt-3.5-turbo"
)

# Prompt Template
task_prompt = PromptTemplate(
    input_variables=["task"],
    template="You are a helpful AI assistant. Provide a detailed solution for this task: {task}"
)

async def generate_task_response(task_description: str) -> Optional[str]:
    """
    Generate AI response for a given task description.

    Args:
        task_description (str): The task text provided by the user.

    Returns:
        Optional[str]: AI-generated solution or None if error occurs.
    """
    try:
        # Format the prompt
        final_prompt = task_prompt.format(task=task_description)
        
        # Call the chat model
        response = await chat_model.agenerate(
            messages=[
                SystemMessage(content="You are a helpful AI assistant."),
                HumanMessage(content=final_prompt)
            ]
        )
        
        # Return AI response text
        return response.generations[0][0].message.content

    except Exception as e:
        print(f"Error generating AI response: {e}")
        return None

