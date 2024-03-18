# Используем официальный базовый образ Python
FROM python:3.9-alpine

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Обновляем pip и устанавливаем необходимые пакеты
RUN pip install --upgrade pip setuptools wheel

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Определяем точку входа для контейнера
CMD ["python", "./main.py"]
