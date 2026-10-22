# Task Manager API — FastAPI & Docker

A simple REST API built using Python and FastAPI, containerized with Docker and published to Docker Hub. This project is a hands-on learning exercise for containerization and DevOps fundamentals.

## 1. Project Overview

The Task Manager API provides endpoints to check API status and retrieve sample tasks.

**Tech stack**
- Python 3.12
- FastAPI — API framework
- Uvicorn — ASGI web server
- Docker — application containerization
- Docker Hub — container image registry

## 2. Project Structure

```text
task-manager-api/
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## 3. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Health status |
| GET | `/tasks` | Retrieve all sample tasks |
| GET | `/docs` | Interactive API documentation |

The current task list is stored in Python memory. It is sample data, not persistent database storage.

## 4. Run Locally Without Docker

### Step 1: Create a virtual environment

```powershell
py -m venv .venv
```

### Step 2: Activate it on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```powershell
py -m pip install -r requirements.txt
```

### Step 4: Start the API

```powershell
py -m uvicorn main:app --reload
```

Open these URLs:

- Home: http://localhost:8000/
- Health: http://localhost:8000/health
- Tasks: http://localhost:8000/tasks
- API docs: http://localhost:8000/docs

Stop the server using `Ctrl+C`.

## 5. Docker Fundamentals

### Image vs. Container

- **Dockerfile:** Instructions used to build an image.
- **Image:** Packaged application and its runtime dependencies.
- **Container:** A running or stopped instance created from an image.
- **Docker Hub:** A registry used to publish and download images.

Workflow:

```text
Source Code + Dockerfile
          |
          v
     Docker Image
          |
          v
       Container
          |
          v
     Running API
```

### Step 1: Build the image

Run this from the project directory:

```powershell
docker build -t task-manager-api .
```

- `docker build`: Builds an image.
- `-t task-manager-api`: Names the image.
- `.`: Uses the current directory as the build context.

### Step 2: Run a container

```powershell
docker run -d -p 8000:8000 --name task-manager task-manager-api
```

- `-d`: Runs in the background.
- `-p 8000:8000`: Maps host port 8000 to container port 8000.
- `--name`: Assigns a container name.

Test the API at http://localhost:8000/tasks.

### Step 3: Inspect the container

```powershell
docker ps
docker ps -a
docker logs task-manager
```

- `docker ps`: Lists running containers.
- `docker ps -a`: Lists all containers, including stopped ones.
- `docker logs`: Displays container output.

### Step 4: Stop and remove the container

```powershell
docker stop task-manager
docker rm task-manager
```

Removing a container does not automatically remove its image.

## 6. Publish the Image to Docker Hub

Replace `YOUR_DOCKERHUB_USERNAME` with your Docker Hub username.

### Step 1: Log in

```powershell
docker login
```

### Step 2: Tag the image

```powershell
docker tag task-manager-api YOUR_DOCKERHUB_USERNAME/task-manager-api:latest
```

An image tag identifies a particular image version. The repository name includes your Docker Hub username.

### Step 3: Push the image

```powershell
docker push YOUR_DOCKERHUB_USERNAME/task-manager-api:latest
```

Verify that the `latest` tag appears in your Docker Hub repository.

## 7. Pull and Run the Published Image

### Step 1: Pull the image

```powershell
docker pull YOUR_DOCKERHUB_USERNAME/task-manager-api:latest
```

### Step 2: Run it

```powershell
docker run -d -p 8000:8000 --name task-manager YOUR_DOCKERHUB_USERNAME/task-manager-api:latest
```

### Step 3: Test it

Open http://localhost:8000/tasks.

This demonstrates how a published image can be downloaded and run without manually installing the application's Python dependencies on the target machine.

## 8. Useful Docker Commands

| Command | Purpose |
|---|---|
| `docker --version` | Check Docker version |
| `docker images` | List local images |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker build -t NAME .` | Build an image |
| `docker run -d -p HOST:CONTAINER NAME` | Run a container |
| `docker logs CONTAINER` | Read container logs |
| `docker stop CONTAINER` | Stop a container |
| `docker rm CONTAINER` | Remove a container |
| `docker pull IMAGE` | Download an image |
| `docker push IMAGE` | Publish an image |

## 9. Current Limitations

- Tasks are stored in an in-memory Python list.
- The API currently supports reading tasks, not creating, updating, or deleting them.
- No database is connected yet.
- No automated CI/CD pipeline is configured yet.

## 10. Planned Improvements

1. Implement full CRUD operations.
2. Connect PostgreSQL for persistent storage.
3. Use Docker Compose to manage the API and database together.
4. Automate tests and image publishing using GitHub Actions.
5. Deploy the application to a local Kubernetes cluster.

## Learning Outcome

This project demonstrates the basics of building a REST API, creating a Docker image, running containers, and publishing and pulling images through Docker Hub.
