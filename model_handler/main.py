from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from langchain.agents import create_agent

from langchain_core.messages import HumanMessage

class WeatherInput(BaseModel):
    location: str = Field(description="Город или страна")
    unit: str = Field(enum=["градусы Цельсия", "градусы Фаренгейта"])


@tool("get_current_weather", args_schema=WeatherInput)
def get_weather(location: str, unit: str):
    """Отвечать на вопрос какая погода сейчас в указанном месте"""
    return f"Актуальная погода в {location} - это 999999 {unit}"


# class WeatherInput(BaseModel):
#     location: str = Field(description="The city and state, e.g. San Francisco, CA")
#     unit: str = Field(enum=["celsius", "fahrenheit"])


# @tool("get_current_weather", args_schema=WeatherInput)
# def get_weather(location: str, unit: str):
#     """Get the current weather in a given location"""
#     return f"Now the weather in {location} is 999999 {unit}"

# @tool("make_small_talk")
# def get_weather():
#     """Keep small talk"""
#     return f"Making kek"

@tool("make_small_talk")
def make_small_talk():
    """Поддержи разговор"""
    return f"Making kek"

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
        # tools=[get_weather, make_small_talk],
        # system_prompt="you are smart assistant. Call tool if request about the weather. In other ways answer by simple text. Do NOT imagine tools"

    )

    input_object = {
        "messages": [
            # {"role": "user", "content": "what is the weather in Krasnodar?"}
            # {"role": "user", "content": "what is up?"}

            # {"role": "user", "content": "какая погода в краснодаре?"}
            {"role": "user", "content": "как дела?"}

        ]
    }
    result = agent.invoke(input_object)
    print(result)
    # messages = result["messages"]
    # print(messages)
    # last_response = messages[-1]
    # print(last_response)
    print("===================================")

if __name__ == "__main__":
    main()
