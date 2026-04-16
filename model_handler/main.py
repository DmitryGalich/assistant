# # from langchain_community.chat_models import ChatLlamaCpp
# # from langchain_core.tools import tool
# # from pydantic import BaseModel, Field
# # from langchain.agents import create_agent

# # from langchain_core.messages import HumanMessage

# # class WeatherInput(BaseModel):
# #     location: str = Field(description="Город или страна")
# #     unit: str = Field(enum=["градусы Цельсия", "градусы Фаренгейта"])


# # @tool("get_current_weather", args_schema=WeatherInput)
# # def get_weather(location: str, unit: str):
# #     """Отвечать на вопрос какая погода сейчас в указанном месте"""
# #     return f"Актуальная погода в {location} - это 999999 {unit}"

# # # @tool("make_small_talk")
# # # def make_small_talk():
# # #     """Поддержи разговор"""
# # #     return f"Иди нахуй"

# # def main():
# #     model_path = r"model_handler/models/qwen2.5-7b-instruct-q4_k_m.gguf"

# #     model = ChatLlamaCpp(
# #         model_path=model_path,
# #         temperature=0,
# #         n_gpu_layers=-1,
# #         verbose=True,
# #         n_ctx = 650,
# #     )

# #     agent = create_agent(
# #         model=model,
# #         # tools=[get_weather, make_small_talk],
# #         tools=[get_weather],

# #     )

# #     input_object = {
# #         "messages": [
# #             {"role": "user", "content": "какая погода в краснодарчике?"}
# #             # {"role": "user", "content": "как дела?"}
# #         ]
# #     }
# #     result = agent.invoke(input_object)
# #     print(result)
# #     print("===================================")

# # if __name__ == "__main__":
# #     main()

from langchain_core.tools import tool
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


from typing import Literal

class WeatherInput(BaseModel):
    location: str = Field(description="Город или страна")
    unit: Literal["градусы Цельсия", "градусы Фаренгейта"]



@tool("get_current_weather", args_schema=WeatherInput)
def get_weather(location: str, unit: str):
    """Получает текущую погоду для указанной локации."""
    return f"Актуальная погода в {location} - это 999999 {unit}"

def main():
    model = ChatOpenAI(
        base_url="http://model_runner:8080/v1",
        api_key="not-needed",
    )

    agent = create_agent(
        model=model,
        tools=[get_weather],
    )

    input_object = {
        "messages": [
            # {"role": "user", "content": "какая погода в краснодарчике?"}
            {"role": "user", "content": "как дела?"}

        ]
    }

    result = agent.invoke(input_object)
    print(result)
    print("===================================")


if __name__ == "__main__":
    main()
