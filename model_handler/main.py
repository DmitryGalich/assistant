from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from langchain.agents import create_agent

from langchain_core.messages import HumanMessage

class WeatherInput(BaseModel):
    location: str = Field(description="The city and state, e.g. San Francisco, CA")
    unit: str = Field(enum=["celsius", "fahrenheit"])


@tool("get_current_weather", args_schema=WeatherInput)
def get_weather(location: str, unit: str):
    """Get the current weather in a given location"""
    return f"Now the weather in {location} is 999999 {unit}"


def main():
    model_path = r"model_handler/models/meta-llama-3.1-8b-instruct-q6_k.gguf"

    model = ChatLlamaCpp(
        model_path=model_path,
        temperature=0,
        n_gpu_layers=-1,
        verbose=True,
        f16_kv=True,
    )

    agent = create_agent(
        model=model,
        tools=[get_weather],
    )

    input_object = {
        "messages": [
            {"role": "user", "content": "какая погода в краснодаре?"}
        ]
    }
    result = agent.invoke(input_object)
    print(result)
    print("===================================")

if __name__ == "__main__":
    main()
