# Реализация

## Architecture overview

[![Architecture overview][architecture-overview]][architecture-overview]

Приложение спроектировано с возможностью переключения обслуживающиего приложения (fastapi)
без изменения кода домена (`application.{api,controller,model}`)

## Test run 

```sh
docker-compose up test
```

[architecture-overview]: _static/architecture-overview.class-diagram.svg
