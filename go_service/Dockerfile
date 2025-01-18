# Используем официальный образ Go
FROM golang:1.23-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы go.mod и go.sum для установки зависимостей
COPY go.mod go.sum ./

# Копируем остальные файлы
COPY . .

# Устанавливаем зависимости
RUN go mod download

WORKDIR /app

RUN chmod +x /app/entrypoint.sh