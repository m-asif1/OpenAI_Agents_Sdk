from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv
load_dotenv()
import os
set_tracing_disabled(disabled=True)

provider = AsyncOpenAI(
        api_key= os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

# creating model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    # openai_client = AsyncOpenAI(
    #     api_key= os.getenv("GEMINI_API_KEY"),
    #     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    openai_client = provider
) 

def run_agent():
    # creating agent
    MyAgent = Agent(
        name="Assistant", 
        instructions="You will response user queries.",model=model)
    
    result = Runner.run_sync(MyAgent, input="Please tell me about Pakistan.")
    print(result.final_output)

run_agent()