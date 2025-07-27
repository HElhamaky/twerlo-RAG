# Twerlo RAG System

A FastAPI-based Retrieval-Augmented Generation (RAG) system with document processing, vector storage, and intelligent question answering capabilities.

## 🚀 Features

- **Document Processing**: Upload and process PDF documents
- **Vector Storage**: ChromaDB-based vector database for semantic search
- **Question Answering**: AI-powered Q&A using OpenAI embeddings
- **User Authentication**: JWT-based authentication system
- **API Documentation**: Auto-generated Swagger/OpenAPI docs
- **Docker Ready**: Containerized for easy deployment

## 📦 Quick Start

### Using Docker

```bash
# Pull the image
docker pull helhamaky/twerlo-app:latest

# Run with environment variables
docker run -p 8000:8000 \
  -v /path/to/data:/app/data \
  --env-file .env \
  helhamaky/twerlo-app:latest
```

### Using Docker Compose

```yaml
version: '3.8'
services:
  twerlo-app:
    image: helhamaky/twerlo-app:latest
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
    env_file:
      - .env
    environment:
      - OPENAI_API_KEY=your_openai_api_key
```

## 🔧 Environment Variables

Create a `.env` file with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///./rag_app.db
```

## 📚 API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - User login
- `POST /auth/refresh` - Refresh JWT token

### Documents
- `POST /documents/upload` - Upload PDF documents
- `GET /documents/list` - List uploaded documents
- `DELETE /documents/{doc_id}` - Delete document

### Question Answering
- `POST /qa/ask` - Ask questions about uploaded documents
- `GET /qa/history` - Get Q&A history

## 🛠️ Development

### Local Setup

```bash
# Clone the repository
git clone <repository-url>
cd Twerlo

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Build Docker Image

```bash
# Build the image
docker build -t twerlo-app .

# Run locally
docker run -p 8000:8000 twerlo-app
```

## 📊 System Requirements

- **Python**: 3.9+
- **Memory**: 2GB+ RAM recommended
- **Storage**: 1GB+ for vector database
- **Network**: Internet access for OpenAI API

## 🔍 API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🐛 Troubleshooting

### Common Issues

1. **NumPy Compatibility**: This image uses NumPy 1.24.3 for compatibility
2. **ChromaDB**: Vector database files are stored in `/app/data/chroma_db`
3. **API Keys**: Ensure OpenAI API key is valid and has sufficient credits

### Logs

```bash
# View container logs
docker logs <container_name>

# Check application logs
docker exec <container_name> python check_logs.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🔗 Links

- **Docker Hub**: https://hub.docker.com/r/helhamaky/twerlo-app
- **Documentation**: [Link to detailed docs]

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Contact: [your-email@example.com]

---

**Built with ❤️ using FastAPI, ChromaDB, and OpenAI** 