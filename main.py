from langchain_community.llms import LlamaCpp
from langchain.agents import create_agent

def main():
    model_path = r"D:\models\saiga_yandexgpt_8b.Q4_K_M.gguf"
    
    with open('system_prompt.txt', 'r', encoding='utf-8') as file:
        system_prompt = file.read()

    model = LlamaCpp(
        model_path=model_path,
        temperature=0.1,
        max_tokens=200,
        n_ctx=8192,
        n_threads=6,
        n_threads_batch=6,
        repeat_penalty=1.1,
        top_k=40,
        top_p=0.9,
        stop=["Human:"],
        stream=True,
    )

    # Создаем агента с правильным системным промптом
    agent = create_agent(model=model, system_prompt=system_prompt)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # answer = agent.invoke(
        input_object = {
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }
        
        for chunk in agent.stream(input_object, stream_mode="updates",):
            for step, data in chunk.items():
                print(f"step: {step}")
                print(f"content: {data['messages'][-1].content_blocks}")
        
        # for chunk in agent.stream(input_object, stream_mode="values"):
        #     latest_message = chunk["messages"][-1]
            
        #     if latest_message.content:
        #         print(f"Assistant: {latest_message.content}")



if __name__ == "__main__":
    main()

