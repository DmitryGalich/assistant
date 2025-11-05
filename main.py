# from langchain_community.llms import LlamaCpp
# from langchain.agents import create_agent
# # from os import cpu_count
# # import torch


# def main():

#     # if torch.cuda.is_available():
#     #     print("GPU is available!")
#     #     print(f"Number of GPUs: {torch.cuda.device_count()}")
#     #     print(f"Current GPU name: {torch.cuda.get_device_name(0)}") # Assuming you want info for the first GPU
#     # else:
#     #     print("GPU is not available. Running on CPU.")

#     model_path = r"D:\models\saiga_yandexgpt_8b.Q4_K_M.gguf"

#     # with open('prompts/main.txt', 'r', encoding='utf-8') as file:
#     #     system_prompt = file.read()

#     # print(cpu_count())

#     # model = LlamaCpp(
#     #     model_path=model_path,
#     #     n_gpu_layers = 33,
#     #     # n_threads=cpu_count(),
#     #     # repeat_penalty=1.1,
#     #     # streaming = True,
#     #     # temperature=0.1,
#     #     # max_tokens=200,
#     #     # n_ctx=8192,
#     #     # n_threads=6,
#     #     # n_threads_batch=6,
#     #     # repeat_penalty=1.1,
#     #     # top_k=40,
#     #     # top_p=0.9,
#     #     # stop=["Human:"],
#     #     # stream=True,


#     # )

#     model = LlamaCpp(
#         model_path=model_path,
#         temperature=0.75,
#         max_tokens=2000,
#         n_gpu_layers=-1,
#         # model_kwargs={"main_gpu" : 0},
#     )

#     agent = create_agent(
#         model=model,

#         #  system_prompt=system_prompt
#     )

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             break

#         input_object = {"messages": [{"role": "user", "content": user_input}]}
#         result = agent.invoke(input_object)
#         print(result["messages"][-1].content)


# if __name__ == "__main__":
#     main()

from llama_cpp import Llama

# Загружаем модель
llm = Llama(
    model_path=r"D:\models\saiga_yandexgpt_8b.Q4_K_M.gguf",
    n_gpu_layers=-1,  # Использовать GPU при наличии
    n_ctx=2048,       # Контекст (можно увеличить)
)

print("Модель загружена! Введите 'exit' для выхода.\n")

# Храним историю диалога (для контекста)
history = ""

while True:
    user_input = input("Ты: ").strip()
    if user_input.lower() in {"exit", "quit", "выход"}:
        print("До встречи!")
        break

    # Добавляем ввод пользователя к истории
    prompt = f"{history}\nQ: {user_input}\nA:"

    # Генерация ответа
    output = llm(
        prompt,
        max_tokens=256,
        stop=["Q:", "\n"],
        echo=False
    )

    # Извлекаем текст ответа
    answer = output["choices"][0]["text"].strip()
    print(f"Модель: {answer}\n")

    # Обновляем историю для следующего запроса
    history += f"\nQ: {user_input}\nA: {answer}"
