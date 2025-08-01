# Twerlo RAG System

A modern Retrieval-Augmented Generation (RAG) system built with FastAPI and Next.js, featuring document processing, vector storage, and intelligent question answering capabilities with persistent user authentication.

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Storage       │
│   (Next.js)     │◄──►│   (FastAPI)     │◄──►│   (SQLite +     │
│   Port: 3000    │    │   Port: 8000    │    │   ChromaDB)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Auth     │    │   Document      │    │   Vector        │
│   (JWT)         │    │   Processing    │    │   Database      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   OpenAI API    │    │   PDF Parser    │    │   Embeddings    │
│   (GPT-4)       │    │   (PyPDF2)      │    │   (OpenAI)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Key Components:
- **Frontend**: Next.js web interface with modern UI
- **Backend**: FastAPI REST API with automatic documentation
- **Database**: SQLite for user data with persistent storage
- **Vector Store**: ChromaDB for document embeddings
- **AI**: OpenAI GPT-4 for question answering
- **Authentication**: JWT-based user authentication

## 🚀 Features

- **Document Processing**: Upload and process PDF documents with automatic chunking
- **Vector Storage**: ChromaDB-based vector database for semantic search
- **Question Answering**: AI-powered Q&A using OpenAI GPT-4 embeddings
- **User Authentication**: JWT-based authentication system with persistent data storage
- **Modern UI**: Responsive Next.js frontend with real-time chat interface
- **API Documentation**: Auto-generated Swagger/OpenAPI docs
- **Docker Ready**: Containerized for easy deployment with persistent database
- **Data Persistence**: User accounts and documents survive container restarts

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: Database ORM
- **SQLite**: Lightweight database for user data
- **ChromaDB**: Vector database for document embeddings
- **PyPDF2**: PDF document processing
- **OpenAI**: GPT-4 for question answering and embeddings
- **JWT**: User authentication
- **Uvicorn**: ASGI server

### Frontend
- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Utility-first CSS framework
- **React Hook Form**: Form handling
- **Axios**: HTTP client

### Infrastructure
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Volume Mounts**: Persistent data storage

## 📦 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- OpenAI API key
- At least 2GB RAM available

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd Twerlo

# Copy environment template
cp env.example .env
```

### 2. Configure Environment

Edit `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///./data/twerlo.db
CHROMA_DB_PATH=data/chroma_db
LLM_MODEL=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-large
```

### 3. Run with Docker Compose

```bash
# Build and start the application
docker-compose up --build -d

# View logs
docker-compose logs -f
```

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🔧 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `SECRET_KEY` | JWT secret key | `your-secret-key-change-this` |
| `DATABASE_URL` | Database connection string | `sqlite:///./data/twerlo.db` |
| `CHROMA_DB_PATH` | Vector database path | `data/chroma_db` |
| `LLM_MODEL` | OpenAI model for Q&A | `gpt-4o-mini` |
| `EMBEDDING_MODEL` | OpenAI embedding model | `text-embedding-3-large` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiry | `30` |

## 📚 API Endpoints

### Authentication
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

### Documents
```http
POST /documents/upload
Authorization: Bearer <token>
Content-Type: multipart/form-data

file: <pdf_file>
```

```http
GET /documents/
Authorization: Bearer <token>
```

### Question Answering
```http
POST /qa/ask
Authorization: Bearer <token>
Content-Type: application/json

{
  "question": "What is the main topic of the document?",
  "document_id": 1
}
```

## 🐛 Known Limitations

### Current Limitations
1. **File Size**: PDF files limited to 10MB per upload
2. **File Type**: Only PDF documents supported
3. **Language**: Optimized for English text
4. **Concurrent Users**: Limited by OpenAI API rate limits
5. **Memory Usage**: Large documents may require more RAM
6. **Vector Search**: Limited to 3 most relevant chunks per query

### Performance Considerations
- **Embedding Generation**: Large documents take time to process
- **API Costs**: OpenAI API usage incurs costs
- **Storage**: Vector database grows with document count
- **Response Time**: Complex questions may take 5-10 seconds

## 🔍 API Documentation

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Postman Collection
```json
{
  "info": {
    "name": "Twerlo API",
    "description": "RAG System API Collection"
  },
  "item": [
    {
      "name": "Authentication",
      "item": [
        {
          "name": "Register",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/auth/register",
            "body": {
              "mode": "raw",
              "raw": "{\n  \"email\": \"user@example.com\",\n  \"password\": \"password123\"\n}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            }
          }
        },
        {
          "name": "Login",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/auth/login",
            "body": {
              "mode": "raw",
              "raw": "{\n  \"email\": \"user@example.com\",\n  \"password\": \"password123\"\n}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            }
          }
        }
      ]
    },
    {
      "name": "Documents",
      "item": [
        {
          "name": "Upload Document",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/documents/upload",
            "header": [
              {
                "key": "Authorization",
                "value": "Bearer {{token}}"
              }
            ],
            "body": {
              "mode": "formdata",
              "formdata": [
                {
                  "key": "file",
                  "type": "file",
                  "src": []
                }
              ]
            }
          }
        },
        {
          "name": "List Documents",
          "request": {
            "method": "GET",
            "url": "{{base_url}}/documents/",
            "header": [
              {
                "key": "Authorization",
                "value": "Bearer {{token}}"
              }
            ]
          }
        }
      ]
    },
    {
      "name": "Question Answering",
      "item": [
        {
          "name": "Ask Question",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/qa/ask",
            "header": [
              {
                "key": "Authorization",
                "value": "Bearer {{token}}"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"question\": \"What is the main topic?\",\n  \"document_id\": 1\n}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            }
          }
        }
      ]
    }
  ],
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:8000"
    },
    {
      "key": "token",
      "value": "your_jwt_token_here"
    }
  ]
}
```

## 🛠️ Development

### Development History & Steps

This application was developed through several key phases:

#### Phase 1: Core Backend Development
1. **FastAPI Setup**: Created the main FastAPI application with CORS middleware
2. **Database Design**: Implemented SQLAlchemy models for User, Document, and QueryLog
3. **Authentication System**: Built JWT-based authentication with password hashing
4. **Document Processing**: Added PDF upload and processing with PyPDF2
5. **Vector Storage**: Integrated ChromaDB for document embeddings
6. **Question Answering**: Implemented OpenAI integration for RAG functionality

#### Phase 2: Frontend Development
1. **Next.js Setup**: Created modern React application with TypeScript
2. **UI Components**: Built reusable components with Tailwind CSS
3. **Authentication UI**: Implemented login/signup forms with validation
4. **Document Upload**: Created drag-and-drop file upload interface
5. **Chat Interface**: Built real-time chat UI for Q&A interactions
6. **Responsive Design**: Made the interface mobile-friendly

#### Phase 3: Infrastructure & Deployment
1. **Docker Containerization**: Created multi-stage Docker build
2. **Database Persistence**: Fixed container restart data loss issues
3. **Environment Configuration**: Set up proper environment variable management
4. **Production Optimization**: Optimized for production deployment
5. **Documentation**: Created comprehensive API documentation

#### Phase 4: Testing & Optimization
1. **API Testing**: Created test suite for backend endpoints
2. **Performance Optimization**: Optimized database queries and vector search
3. **Error Handling**: Implemented comprehensive error handling
4. **Security Hardening**: Added input validation and security measures
5. **Monitoring**: Added health checks and logging

### Local Development Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
cd frontend
npm install

# Start backend (in one terminal)
cd ..
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Start frontend (in another terminal)
cd frontend
npm run dev
```

### Database Management

```bash
# Initialize database
python -m app.db.init_db

# View database
sqlite3 data/twerlo.db
```

### Development Workflow

#### Backend Development
```bash
# Run backend with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run tests
python -m pytest tests/

# Check code formatting
black app/
isort app/

# Type checking
mypy app/
```

#### Frontend Development
```bash
# Start development server
cd frontend
npm run dev

# Run tests
npm test

# Build for production
npm run build

# Type checking
npm run type-check
```

#### Database Development
```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Reset database
rm data/twerlo.db
python -m app.db.init_db
```

### Key Development Decisions

#### Architecture Choices
- **FastAPI**: Chosen for its modern async support and automatic API documentation
- **SQLite**: Selected for simplicity and zero-configuration deployment
- **ChromaDB**: Picked for its Python-native vector database capabilities
- **Next.js**: Chosen for its React framework with built-in optimizations
- **Docker**: Used for consistent development and deployment environments

#### Database Persistence Solution
The application originally had a critical issue where user data was lost on container restarts. This was solved by:
1. Moving database from container filesystem to mounted volume
2. Adding proper database initialization on startup
3. Implementing environment variable configuration
4. Creating migration scripts for existing deployments

#### Security Implementation
- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: bcrypt for secure password storage
- **Input Validation**: Pydantic models for request validation
- **CORS Configuration**: Proper cross-origin resource sharing setup

#### Performance Optimizations
- **Vector Search**: Limited to 3 most relevant chunks for faster responses
- **Database Indexing**: Added indexes on frequently queried fields
- **Caching**: Implemented response caching for repeated queries
- **Chunking**: Optimal document chunking for better search results

## 📊 System Requirements

### Minimum Requirements
- **CPU**: 2 cores
- **RAM**: 2GB
- **Storage**: 1GB free space
- **Network**: Internet access for OpenAI API

### Recommended Requirements
- **CPU**: 4+ cores
- **RAM**: 4GB+
- **Storage**: 5GB+ for large document collections
- **Network**: Stable internet connection

## 🔧 Troubleshooting

### Common Issues

1. **Container Won't Start**
   ```bash
   # Check logs
   docker-compose logs
   
   # Rebuild container
   docker-compose down
   docker-compose up --build
   ```

2. **Database Issues**
   ```bash
   # Check database file
   ls -la data/twerlo.db
   
   # Reinitialize database
   docker-compose exec app python -m app.db.init_db
   ```

3. **OpenAI API Errors**
   - Verify API key is correct
   - Check API usage limits
   - Ensure sufficient credits

4. **Memory Issues**
   - Increase Docker memory limit
   - Reduce document chunk size in config

### Logs and Debugging

```bash
# View all logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f app

# Check container status
docker-compose ps

# Access container shell
docker-compose exec app bash
```

## 🔒 Security Considerations

- **JWT Tokens**: Set strong SECRET_KEY
- **API Keys**: Never commit .env files
- **File Uploads**: Validate file types and sizes
- **Rate Limiting**: Consider implementing API rate limits
- **HTTPS**: Use HTTPS in production

## 🚀 Deployment

### Production Deployment

1. **Environment Setup**
   ```bash
   # Set production environment variables
   export NODE_ENV=production
   export DATABASE_URL=sqlite:///./data/twerlo.db
   ```

2. **Docker Production**
   ```bash
   # Build production image
   docker build -t twerlo-app:latest .
   
   # Run with production config
   docker-compose -f docker-compose.prod.yml up -d
   ```

3. **Reverse Proxy** (Recommended)
   - Use Nginx or Traefik
   - Configure SSL certificates
   - Set up proper CORS headers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use TypeScript for frontend code
- Add tests for new features
- Update documentation for API changes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **GitHub Repository**: [Link to repo]
- **Docker Hub**: https://hub.docker.com/r/helhamaky/twerlo-app
- **API Documentation**: http://localhost:8000/docs

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review API documentation

---

**Built with ❤️ using FastAPI, Next.js, ChromaDB, and OpenAI**