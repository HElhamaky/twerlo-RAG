# Docker Registry Configuration

## 🐳 **Docker Hub Registry**

### **Registry Information**
- **Repository**: `helhamaky/twerlo-app`
- **Latest Tag**: `helhamaky/twerlo-app:latest`
- **Versioned Tag**: `helhamaky/twerlo-app:20250728-1535`
- **Registry**: Docker Hub (docker.io)

### **Available Images**

| Tag | Description | Size | Created |
|-----|-------------|------|---------|
| `latest` | Latest production build | 2.69GB | 2025-07-28 |
| `20250728-1535` | Versioned build | 2.69GB | 2025-07-28 |
| `20250727-211759` | Previous version | 1.05GB | 2025-07-27 |

### **Pull Commands**

```bash
# Pull latest version
docker pull helhamaky/twerlo-app:latest

# Pull specific version
docker pull helhamaky/twerlo-app:20250728-1535

# Run with docker-compose
docker-compose up -d
```

### **Push Commands**

```bash
# Build and tag
docker build -t helhamaky/twerlo-app:latest .
docker tag twerlo-app:latest helhamaky/twerlo-app:$(date +%Y%m%d-%H%M%S)

# Push to registry
docker push helhamaky/twerlo-app:latest
docker push helhamaky/twerlo-app:20250728-1535
```

### **Deployment Options**

#### **1. Local Development**
```bash
# Uses local build
docker-compose up -d
```

#### **2. Production (Registry)**
```bash
# Uses registry image
docker-compose -f docker-compose.prod.yml up -d
```

#### **3. Direct Docker Run**
```bash
# Run from registry
docker run -p 3000:3000 -p 8000:8000 helhamaky/twerlo-app:latest
```

### **Environment Variables**

#### **Required for Production**
```bash
SECRET_KEY=your-secret-key-here
CORS_ORIGINS=https://your-domain.com
```

#### **Optional**
```bash
NODE_ENV=production
NEXT_TELEMETRY_DISABLED=1
DATABASE_URL=sqlite:///./data/twerlo.db
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### **Health Checks**

The production image includes health checks:
- **Endpoint**: `http://localhost:8000/health`
- **Interval**: 30 seconds
- **Timeout**: 10 seconds
- **Retries**: 3

### **Registry Access**

- **Public Repository**: Yes
- **Authentication**: Docker Hub login required for push
- **Pull**: No authentication required
- **Push**: Requires `helhamaky` Docker Hub account

### **Image Features**

✅ **Multi-stage build** for optimized size  
✅ **Production-ready** configuration  
✅ **Health checks** included  
✅ **Environment variables** support  
✅ **Volume mounting** for data persistence  
✅ **CORS configuration** for web access  
✅ **JWT authentication** ready  
✅ **Document processing** capabilities  

### **Usage Examples**

#### **Development**
```bash
# Build and run locally
docker-compose up -d
```

#### **Production**
```bash
# Use registry image
docker-compose -f docker-compose.prod.yml up -d
```

#### **Custom Environment**
```bash
# Run with custom environment
docker run -d \
  -p 3000:3000 \
  -p 8000:8000 \
  -e SECRET_KEY=your-secret \
  -e CORS_ORIGINS=https://your-domain.com \
  -v $(pwd)/data:/app/data \
  helhamaky/twerlo-app:latest
```

### **Registry URL**
- **Docker Hub**: https://hub.docker.com/r/helhamaky/twerlo-app
- **Pull URL**: `docker.io/helhamaky/twerlo-app:latest` 