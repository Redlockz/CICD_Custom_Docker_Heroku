# CICD_Custom_Docker_Heroku

Custom CI/CD pipeline to build a Docker image with a Python Flask web application and deploy to Heroku.

## Features

- 🐍 **Python Flask Web Application**: Simple REST API with multiple endpoints
- 🐳 **Docker Containerization**: Fully containerized application
- 🧪 **Automated Testing**: Unit tests and integration tests for Docker deployment
- 🔒 **Security Scanning**: Checkov security checks on Dockerfile and infrastructure
- 🚀 **CI/CD Pipeline**: GitHub Actions workflow for automated build, test, and deploy
- ☁️ **Heroku Ready**: Configured for Heroku deployment

## Application Endpoints

- `GET /` - Home endpoint with application info
- `GET /health` - Health check endpoint
- `GET /api/info` - Application information

## Local Development

### Prerequisites

- Python 3.11+
- Docker (optional, for containerized testing)

### Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Application will be available at http://localhost:5000
```

### Run Tests

```bash
# Run unit tests
pytest test_app.py -v
```

## Docker

### Build Docker Image

```bash
docker build -t flask-app:latest .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 --name flask-app flask-app:latest
```

### Test Docker Deployment

```bash
python test_docker_deployment.py
```

### Stop Container

```bash
docker stop flask-app
docker rm flask-app
```

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/docker-pipeline.yml`) includes:

1. **Unit Tests**: Runs pytest tests on the Flask application
2. **Security Scan**: Runs Checkov security analysis on Dockerfile
3. **Docker Build & Test**: 
   - Builds Docker image
   - Starts container
   - Tests accessibility of all endpoints
4. **Heroku Deploy** (optional): Deploys to Heroku on main branch

### Pipeline Stages

```
Test → Security Scan → Build & Test Docker → Deploy to Heroku
```

## Heroku Deployment

To enable Heroku deployment, add the following secrets to your GitHub repository:

- `HEROKU_API_KEY`: Your Heroku API key
- `HEROKU_APP_NAME`: Your Heroku app name

The application is configured to work with Heroku's dynamic port assignment.

## Security

- Uses non-root user in Docker container
- Checkov security scanning in CI pipeline
- Minimal base image (python:3.11-slim)
- No cache for pip installations to reduce image size

## Project Structure

```
.
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── test_app.py                 # Unit tests
├── test_docker_deployment.py   # Docker integration tests
├── .github/
│   └── workflows/
│       └── docker-pipeline.yml # CI/CD workflow
└── README.md                   # This file
```
