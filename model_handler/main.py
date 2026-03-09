from langchain_community.chat_models import ChatLlamaCpp
# from langchain_core.tools import tool
# from pydantic import BaseModel, Field
# from langchain.agents import create_agent

# from langchain_core.messages import HumanMessage

from deepagents import create_deep_agent

# class WeatherInput(BaseModel):
#     location: str = Field(description="Город или страна")
#     unit: str = Field(enum=["градусы Цельсия", "градусы Фаренгейта"])


# @tool("get_current_weather", args_schema=WeatherInput)
# def get_weather(location: str, unit: str):
#     """Отвечать на вопрос какая погода сейчас в указанном месте"""
#     return f"Актуальная погода в {location} - это 999999 {unit}"

# @tool("make_small_talk")
# def make_small_talk():
#     """Поддержи разговор"""
#     return f"ИДИ НАХУЙ"

def main():
    model_path = r"model_handler/models/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf"
    llm = ChatLlamaCpp(
        model_path=model_path,
        temperature=0,
        n_gpu_layers=-1,
        verbose=True,
        f16_kv=True,
        n_ctx = 6379,
    )


    agent= create_deep_agent(
        model=llm
    )

    input_object = {
        "messages": [
            # {"role": "user", "content": "какая погода в краснодаре?"}
            {"role": "user", "content": "как дела?"}

        ]
    }

    result = agent.invoke(input_object)
    print(result)

    # messages = result["messages"]
    # last_response = messages[-1]

if __name__ == "__main__":
    main()
