import os
import json
import asyncio

from agents import Agent
from agents import Runner
from agents import OpenAIChatCompletionsModel
from agents import Tool
from agents import function_tool


from openai import AsyncOpenAI

from pydantic import BaseModel
from pydantic import Field

from typing import List
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

llm_api_key = os.getenv("API_KEY")
llm_base_url = os.getenv("BASE_URL")
llm_model_name = os.getenv("MODEL_NAME")

if not llm_model_name or not llm_base_url or not llm_api_key:
    raise ValueError("Problem in env file")

client=AsyncOpenAI(
    api_key=llm_api_key,
    base_url=llm_base_url
)

structured_model=OpenAIChatCompletionsModel(
    openai_client=client,
    model=llm_model_name
)


