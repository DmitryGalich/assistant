def main():
    model_path = "D:\models\saiga_yandexgpt_8b.Q4_K_M.gguf"
    system_prompt = ""

    with open('system_prompt.txt', 'r', encoding='utf-8') as file:
        system_prompt = file.read()

    print(model_path)
    print(system_prompt)


if __name__ == "__main__":
    main()