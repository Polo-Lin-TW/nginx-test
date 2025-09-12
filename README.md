# Nginx Demo Web Application

A full-stack web application demonstrating the integration of Vue 3 frontend, FastAPI backend, and Nginx reverse proxy, all containerized with Docker.

## Architecture

- **Frontend**: Vue 3 with Vite build system
- **Backend**: FastAPI (Python)
- **Reverse Proxy**: Nginx
- **Containerization**: Docker & Docker Compose

## Project Structure

```
nginx_demo/
├── backend/                  # FastAPI backend application
│   ├── Dockerfile           # Backend container
│   ├── main.py              # FastAPI application
│   └── requirements.txt     # Python dependencies
├── frontend/                 # Vue 3 frontend application
│   ├── Dockerfile           # Frontend container with Nginx
│   ├── nginx.conf           # Reverse proxy configuration
│   ├── package.json         # Node.js dependencies
│   ├── vite.config.js       # Vite configuration
│   └── src/
│       ├── App.vue          # Main Vue component
│       └── main.js          # Application entry point
├── docker-compose.yml        # Docker Compose setup
└── README.md                 # This file
```

## Features

### Frontend (Vue 3)
- Modern Vue 3 Composition API
- Responsive design with CSS Grid
- API connectivity testing
- Hot reload in development
- Optimized production builds

### Backend (FastAPI)
- RESTful API endpoints
- Automatic OpenAPI documentation
- CORS middleware configured
- Pydantic data validation
- Health check endpoints

### Infrastructure
- Nginx reverse proxy
- Docker containerization
- Static file serving optimization
- API request proxying

## Getting Started

### Prerequisites
- Docker and Docker Compose installed

### Running the Application

1. **Build and start all services:**
```bash
docker-compose up --build -d
```

2. **Access the application:**
- Frontend: [http://localhost](http://localhost)
- Backend API: [http://localhost:8000](http://localhost:8000)
- API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints

| Method | Endpoint       | Description                   |
|--------|----------------|-------------------------------|
| GET    | `/`            | Welcome message               |
| GET    | `/health`      | Backend health check          |
| GET    | `/api/health`  | API health check              |
| GET    | `/api/info`    | Application information       |
| POST   | `/api/process` | Process a message             |
| GET    | `/docs`        | Interactive API documentation |

## Docker Commands

```bash
# Start services in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Configuration

### Nginx Configuration
The Nginx configuration (`frontend/nginx.conf`) includes:
- Static file serving
- API request proxying to the backend service

## Health Checks

Both services include health check endpoints:
- Backend: `http://localhost:8000/health`
- Frontend: The frontend is served by Nginx, and the container health is checked by accessing the root URL.

## Contributing

1. Make changes to the appropriate service directory.
2. Test locally using Docker Compose.
3. Update documentation as needed.

## License

This project is for demonstration purposes.
