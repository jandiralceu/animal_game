.PHONY: start install docker help

start: ## Start the application
	@echo "Starting the application..."
	poetry run app

install: ## Install dependencies
	@echo "Installing dependencies..."
	poetry install

docker: ## Build the Docker image
	@echo "Building the Docker image..."
	docker build -t jandir/animal-game:latest .

help: ## Display all available commands
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)