# To-Do CLI App (DevOps Project)

A simple CLI To-Do app packaged with Docker & Docker Compose.

## Run without Docker
```bash
python3 todo.py add "Read a book"
python3 todo.py list
python3 todo.py remove 1
```

## Run with Docker Compose
```bash
# Build & start container
docker-compose up -d

# Add a task
docker-compose exec todo python3 todo.py add "Read a book"

# Show tasks
docker-compose exec todo python3 todo.py list

# Remove task by ID
docker-compose exec todo python3 todo.py remove 1
```

Data persists in the `data/` folder using Docker volume mapping.
