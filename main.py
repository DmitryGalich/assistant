from langchain_community.llms import LlamaCpp
from langchain.agents import create_agent

def main():
    model_path = "D:\models\saiga_yandexgpt_8b.Q4_K_M.gguf"
 
    llm = LlamaCpp(
        model_path=model_path,
        temperature=0.75,
        max_tokens=2000,
        n_ctx=4096,
        verbose=True,
    )

    agent = create_agent(llm)

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