from langchain_community.llms import LlamaCpp
from langchain.agents import create_agent

def main():
    model_path = "D:\models\saiga_yandexgpt_8b.Q4_K_M.gguf"
    system_prompt = ""

    with open('system_prompt.txt', 'r', encoding='utf-8') as file:
        system_prompt = file.read()


    model = LlamaCpp(
        model_path=model_path,
        # temperature=0.75,
        max_tokens=200,
        n_ctx=8192,
        # verbose=True,
        n_threads = 6,
        n_threads_batch = 6,
    )

    agent = create_agent(model = model,
                         system_prompt=system_prompt)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        answer = agent.invoke({
            "messages": [
                {"role": "user", "content": user_input}
            ]
        })

        print(answer)


if __name__ == "__main__":
    main()