import llama_cpp

def main():
    model_path = "D:\models\saiga_yandexgpt_8b.Q4_K_M.gguf"
    init_prompt = ""

    with open('init_prompt.txt', 'r', encoding='utf-8') as file:
        init_prompt = file.read()

    model = llama_cpp.Llama(
        model_path=model_path,
        n_ctx=8192,)
    messages = [{"role": "system", "content": init_prompt}]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})
        for part in model.create_chat_completion(
            messages,
            temperature=0.1,
            top_k=30,
            top_p=0.9,
            repeat_penalty=1.1,
            stream=True,
        ):
            delta = part["choices"][0]["delta"]
            if "content" in delta:
                print(delta["content"], end="", flush=True)

if __name__ == "__main__":
    main()