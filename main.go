package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
)

func main() {
	// Get bot token from environment variable
	token := os.Getenv("TELEGRAM_BOT_TOKEN")
	if token == "" {
		log.Fatal("TELEGRAM_BOT_TOKEN environment variable is not set")
	}

	// Create a new bot instance
	bot, err := tgbotapi.NewBotAPI(token)
	if err != nil {
		log.Fatalf("Failed to create bot: %v", err)
	}

	// Set this to true to see all API interactions
	bot.Debug = os.Getenv("DEBUG") == "true"

	log.Printf("Authorized on account %s", bot.Self.UserName)

	// Create a new UpdateConfig struct with an offset of 0
	updateConfig := tgbotapi.NewUpdate(0)
	updateConfig.Timeout = 60

	// Start receiving updates
	updates := bot.GetUpdatesChan(updateConfig)

	// Create a context that will be canceled on interrupt signal
	ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer cancel()

	// Handle updates in a separate goroutine
	go handleUpdates(ctx, bot, updates)

	// Wait for a signal to quit
	<-ctx.Done()
	log.Println("Shutting down bot...")
}

func handleUpdates(ctx context.Context, bot *tgbotapi.BotAPI, updates tgbotapi.UpdatesChannel) {
	for {
		select {
		case <-ctx.Done():
			return
		case update := <-updates:
			// Ignore any non-message updates
			if update.Message == nil {
				continue
			}

			// Log the message
			log.Printf("[%s] %s", update.Message.From.UserName, update.Message.Text)

			// If the message is not a command, process it as a chat message
			if !update.Message.IsCommand() {
				// Here you would typically send the message to your LLM service
				// and get a response back
				response := processMessageWithLLM(update.Message.Text)
				
				// Create a new message to send back
				msg := tgbotapi.NewMessage(update.Message.Chat.ID, response)
				msg.ReplyToMessageID = update.Message.MessageID

				// Send the message
				if _, err := bot.Send(msg); err != nil {
					log.Printf("Error sending message: %v", err)
				}
				continue
			}

			// Handle commands
			switch update.Message.Command() {
			case "start":
				msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Hello! I'm your AI assistant. How can I help you today?")
				bot.Send(msg)
			case "help":
				msg := tgbotapi.NewMessage(update.Message.Chat.ID, "I'm an AI assistant. Just send me a message and I'll respond!")
				bot.Send(msg)
			default:
				msg := tgbotapi.NewMessage(update.Message.Chat.ID, "I don't know that command. Try sending me a message instead!")
				bot.Send(msg)
			}
		}
	}
}

// This is a placeholder function that would be replaced with actual LLM integration
func processMessageWithLLM(message string) string {
	// In a real implementation, you would:
	// 1. Send the message to your LLM API
	// 2. Get the response
	// 3. Return it
	
	// For now, we'll just echo the message with a prefix
	return fmt.Sprintf("AI response to: %s\n\nThis is a placeholder. In a real implementation, this would be a response from your LLM API.", message)
}