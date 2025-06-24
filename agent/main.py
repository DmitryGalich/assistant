import torch
import time

# Проверяем наличие GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Размер матрицы (можно увеличить для большей нагрузки)
N = 10000

# Создаём две случайные матрицы и перемещаем их на GPU
a = torch.randn((N, N), device=device)
b = torch.randn((N, N), device=device)

# Засекаем время
start = time.time()

# Матричное умножение на GPU
for i in range(10):  # Несколько итераций для постоянной нагрузки
    c = torch.matmul(a, b)

# Синхронизируем, чтобы убедиться, что вычисления завершены
torch.cuda.synchronize()
end = time.time()

print(f"Matrix multiplication done on GPU in {end - start:.2f} seconds")
