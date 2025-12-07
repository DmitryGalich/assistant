from langchain.agents import create_agent
from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.tools import tool

CUSTOM_CHAT_TEMPLATE = """
{%- if messages[0]['role'] == 'system' %}
    {%- set system_message = messages[0]['content'] %}
    {%- set loop_messages = messages[1:] %}
{%- else %}
    {%- set loop_messages = messages %}
{%- endif %}

{{ bos_token }}
{%- for message in loop_messages %}
    {%- if (message['role'] == 'user') != (loop.index0 % 2 == 0) %}
        {{ raise_exception('After the optional system message, conversation roles must alternate user/assistant/user/assistant/...') }}
    {%- endif %}
    {%- if message['role'] == 'user' %}
        {%- if loop.last and system_message is defined %}
            {{ '[INST] ' + system_message + '\\n\\n' + message['content'] + '[/INST]' }}
        {%- else %}
            {{ '[INST] ' + message['content'] + '[/INST]' }}
        {%- endif %}
    {%- elif message['role'] == 'assistant' %}
        {{ ' ' + message['content'] + eos_token }}
    {%- else %}
        {{ raise_exception('Only user and assistant roles are supported, with the exception of an initial optional system message!') }}
    {%- endif %}
{%- endfor %}
"""

@tool
def get_current_weather(location: str) -> str:
    """Gets the current weather for a given location.
    
    Args:
        location: The city to get the weather for.
    
    Returns:
        A string describing the current weather at the given location.
    """

    return f"The weather in {location} is sunny with a temperature of 25°C."

def main():
    system_prompt_path = r"model_handler/prompts/main.txt"
    system_prompt = ""

    model_path = r"model_handler/models/Mistral-Nemo-Instruct-2407.Q2_K.gguf"

    with open(system_prompt_path, "r", encoding="utf-8") as file:
        system_prompt = file.read()

    model = ChatLlamaCpp(
        model_path=model_path,
        temperature=0.1,
        n_ctx=2000,
        repeat_penalty=1.1,
        max_tokens=2000,
        n_gpu_layers=-1,
        stop=["Human:"],
        chat_format="custom",
        chat_format_kwargs={
            "template": CUSTOM_CHAT_TEMPLATE,
            "bos_token": "<s>",
            "eos_token": "</s>",
        },
    )

    model_with_tools = model.bind_tools([get_current_weather])
    result = model_with_tools.invoke("What's the weather like in London?")
    print(result)

    agent = create_agent(model=model, system_prompt=system_prompt)

    # while True:
    #     user_input = input("You: ")
    #     if user_input.lower() == "exit":
    #         break

        # input_object = {"messages": [{"role": "user", "content": user_input}]}
        # result = agent.invoke(input_object)


        # print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
