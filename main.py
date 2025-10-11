from langchain_community.llms import LlamaCpp

model_path = "D:\models\saiga_yandexgpt_8b.Q4_K_M.gguf"

llm = LlamaCpp(
    model_path=model_path,
    temperature=0.75,
    max_tokens=2000,
    n_ctx=4096,
    verbose=True,
)

print(llm.invoke("What is the capital of France?"))
