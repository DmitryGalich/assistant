
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
            {"role": "user", "content": "какая погода в краснодарчике?"}
            # {"role": "user", "content": "как дела?"}

        ]
    }

    result = agent.invoke(input_object)
    print(result)
    print("===================================")


if __name__ == "__main__":
    main()
