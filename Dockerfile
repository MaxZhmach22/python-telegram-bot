# Определяем базовый образ для контейнера с поддержкой CUDA
FROM nvidia/cuda:12.3.2-base-ubuntu20.04

# Используем официальный базовый образ Python
FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Определяем точку входа для контейнера
CMD ["python", "./main.py"]
