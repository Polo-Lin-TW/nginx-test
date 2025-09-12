# Nginx Demo Web Application

A full-stack web application demonstrating the integration of Vue 3 frontend, FastAPI backend, and Nginx reverse proxy, all containerized with Docker.

## Architecture

- **Frontend**: Vue 3 with Vite build system
- **Backend**: FastAPI (Python)
- **Reverse Proxy**: Nginx
- **Containerization**: Docker & Docker Compose
- **Documentation**: Context7 integration ready

## Project Structure

```
nginx_demo/
├── frontend/                 # Vue 3 frontend application
│   ├── src/
│   │   ├── App.vue          # Main Vue component
│   │   └── main.js          # Application entry point
│   ├── Dockerfile           # Frontend container with Nginx
│   ├── Dockerfile.build     # Build-only container for production
│   ├── package.json         # Node.js dependencies
│   └── vite.config.js       # Vite configuration
├── backend/                  # FastAPI backend application
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Backend container
├── nginx/                    # Nginx configuration
│   └── nginx.conf           # Reverse proxy configuration
├── docker-compose.yml        # Development setup
├── docker-compose.prod.yml   # Production setup
└── README.md                # This file
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
- Production-ready configuration
- Static file serving optimization
- API request proxying

## Getting Started

### Prerequisites
- Docker and Docker Compose installed
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Development Mode

1. **Start all services in development mode:**
```bash
docker-compose --profile dev up --build
```

2. **Access the application:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Production Mode

1. **Build and start production services:**
```bash
docker-compose -f docker-compose.prod.yml up --build
```

2. **Access the application:**
- Full Application: http://localhost
- The frontend is served by Nginx with API requests proxied to the backend

### Local Development

#### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

#### Backend Development
```bash
cd backend
pip install -r requirements.txt
python main.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/` | Root endpoint |
| GET    | `/health` | Backend health check |
| GET    | `/api/health` | API health check |
| GET    | `/api/info` | Application information |
| POST   | `/api/process` | Process message endpoint |
| GET    | `/docs` | Interactive API documentation |

## Docker Commands

### Development
```bash
# Start development environment
docker-compose --profile dev up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production
```bash
# Build and start production environment
docker-compose -f docker-compose.prod.yml up --build -d

# Scale backend service
docker-compose -f docker-compose.prod.yml up --scale backend=3 -d

# Update services
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d
```

## Configuration

### Environment Variables
- `ENVIRONMENT`: Set to `production` for production builds
- `PYTHONPATH`: Python module path (set automatically in containers)

### Nginx Configuration
The Nginx configuration (`nginx/nginx.conf`) includes:
- Static file serving with caching
- API request proxying
- CORS headers
- Gzip compression
- Error page handling

## Context7 Integration

This project is configured to work with Context7 for documentation purposes. The architecture and code examples can be easily referenced and used in development workflows.

## Health Checks

Both services include health check endpoints:
- Backend: `http://localhost:8000/health`
- Frontend: Served through Nginx proxy

## Contributing

1. Make changes to the appropriate service directory
2. Test locally using Docker Compose
3. Build and test production configuration
4. Update documentation as needed

## License

This project is for demonstration purposes.