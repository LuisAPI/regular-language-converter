# Command to start the backend
start-backend:
    python Backend/app.py

# Placeholder for starting the frontend
start-frontend:
    @echo "Frontend setup not implemented yet."

# Command to start both backend and frontend
start:
    make start-backend
    # Uncomment the line below when the frontend is ready
    # make start-frontend