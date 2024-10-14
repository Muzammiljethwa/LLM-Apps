from langchain_openai import AzureChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")


llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("OPEN_AI_MODEL_NAME"),
    openai_api_version=os.getenv("AZURE_API_VERSION"),
)
print("AzureChatOpenAI Initilized...")