from langchain_community.llms import LlamaCpp
from langchain.agents import create_agent


def main():
    system_prompt_path = r"model_handler/prompts/main.txt"
    system_prompt = ""
    model_path = r"model_handler/models/saiga_yandexgpt_8b.Q4_K_M.gguf"

    with open(system_prompt_path, "r", encoding="utf-8") as file:
        system_prompt = file.read()

    model = LlamaCpp(
        model_path=model_path,
        temperature=0.1,
        max_tokens=2000,
        n_gpu_layers=-1,
        stop=["Human:"],
        stream=True,
    )

    agent = create_agent(model=model, system_prompt=system_prompt)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        input_object = {"messages": [{"role": "user", "content": user_input}]}
        result = agent.invoke(input_object)
        print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
