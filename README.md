# Telegram LLM Chat Bot

A Golang-based Telegram bot that integrates with an LLM (Language Learning Model) for chat functionality. This bot is containerized using Docker and can be deployed using Docker Compose.

## Features

- Telegram bot integration
- Placeholder for LLM integration
- Docker containerization
- Graceful shutdown handling

## Prerequisites

- Docker and Docker Compose installed
- A Telegram Bot Token (obtained from [@BotFather](https://t.me/BotFather))
- (Optional) API key for your preferred LLM service

## Setup

1. Clone this repository
2. Create a `.env` file based on the `.env.example` template:
   ```bash
   cp .env.example .env
   ```
3. Edit the `.env` file and add your Telegram Bot Token:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   ```
4. (Optional) Add any LLM API credentials if you're integrating with a specific service

## Running the Bot

To start the bot:

```bash
docker-compose up -d
```

To view logs:

```bash
docker-compose logs -f
```

To stop the bot:

```bash
docker-compose down
```

## Customizing LLM Integration

The current implementation includes a placeholder function `processMessageWithLLM` that should be replaced with actual LLM API integration code. Modify this function in `main.go` to connect to your preferred LLM service.

## Commands

The bot currently supports the following commands:

- `/start` - Introduces the bot
- `/help` - Shows help information

All other messages are processed through the LLM integration.

## License

[MIT](LICENSE)