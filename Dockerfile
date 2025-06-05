FROM golang:1.21-alpine AS builder

WORKDIR /app

# Copy go.mod and go.sum files
COPY go.mod ./

# Download dependencies
RUN go mod download

# Copy the source code
COPY . .

RUN go get telegram-llm-bot

# Build the application
RUN CGO_ENABLED=0 GOOS=linux go build -o /telegram-bot


# Use a smaller image for the final container
FROM alpine:latest

# Install ca-certificates for HTTPS requests
RUN apk --no-cache add ca-certificates

WORKDIR /root/

# Copy the binary from the builder stage
COPY --from=builder /telegram-bot .

# Command to run the executable
CMD ["./telegram-bot"]