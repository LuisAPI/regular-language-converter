# Install Python dependencies
install-deps:
	pip install -r requirements.txt

# Command to start the backend with optional dependency installation
# Usage: make start-backend DEPS=true
start-backend:
	@if [ "$(DEPS)" = "true" ]; then \
		echo "Installing dependencies..."; \
		pip install -r requirements.txt; \
	fi
	python Backend/app.py

# Placeholder for starting the frontend
start-frontend:
	@echo "Frontend setup not implemented yet."

# Command to start both backend and frontend
start: start-backend
	# Uncomment the line below when the frontend is ready
	# make start-frontend