# 🚀 GitHub Actions Setup Guide

## **Overview**

This repository includes comprehensive GitHub Actions workflows for:

- ✅ **Automated Testing** - Run tests on every push/PR
- ✅ **Security Scanning** - Vulnerability scanning with Trivy
- ✅ **Docker Build & Push** - Automatic Docker Hub updates
- ✅ **Dependency Review** - Security alerts for dependencies
- ✅ **Multi-platform Support** - AMD64 and ARM64 builds

## **📋 Prerequisites**

### **1. GitHub Repository**
- Create a GitHub repository
- Push your code to GitHub

### **2. Docker Hub Access Token**
1. Go to [Docker Hub](https://hub.docker.com/)
2. Sign in to your account (`helhamaky`)
3. Go to **Account Settings** → **Security**
4. Click **"New Access Token"**
5. **Name**: `GitHub Actions`
6. **Permissions**: Read & Write
7. **Copy the token** (you'll need it for GitHub secrets)

## **🔧 Setup Steps**

### **Step 1: Add GitHub Secrets**

1. Go to your GitHub repository
2. Click **"Settings"** tab
3. Click **"Secrets and variables"** → **"Actions"**
4. Click **"New repository secret"**

**Add these secrets:**

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `DOCKERHUB_USERNAME` | `helhamaky` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | `[Your Docker Hub token]` | Docker Hub access token |

### **Step 2: Push Your Code**

```bash
# Add the remote (replace with your GitHub repo URL)
git remote add origin https://github.com/helhamaky/twerlo-rag-system.git

# Push to GitHub
git push -u origin main
```

### **Step 3: Verify Workflows**

1. Go to your GitHub repository
2. Click **"Actions"** tab
3. You should see workflows running automatically

## **📊 Workflow Details**

### **Main Workflow: `docker-build.yml`**

**Triggers:**
- Push to `main` or `master` branch
- Pull requests to `main` or `master`
- Tags starting with `v*` (e.g., `v1.0.0`)
- Manual trigger via GitHub UI

**Jobs:**

1. **Test Job**
   - Runs Python tests
   - Lints code with flake8
   - Must pass before build

2. **Security Scan Job**
   - Scans Docker image with Trivy
   - Uploads results to GitHub Security tab
   - Runs after tests pass

3. **Build & Push Job**
   - Builds Docker image
   - Pushes to Docker Hub
   - Creates multiple tags
   - Only runs on push (not PR)

### **Test Workflow: `test-docker.yml`**

**Triggers:**
- After main workflow completes
- Manual trigger

**Features:**
- Tests Docker image functionality
- Tests API endpoints
- Tests docker-compose setup

### **Dependency Review: `dependency-review.yml`**

**Triggers:**
- Pull requests to main branch

**Features:**
- Reviews dependencies for security issues
- Fails on moderate+ severity issues
- Comments on PR with findings

## **🏷️ Docker Image Tags**

The workflow creates these tags automatically:

| Tag Pattern | Example | Description |
|-------------|---------|-------------|
| `latest` | `helhamaky/twerlo-app:latest` | Latest stable version |
| `main-[hash]` | `helhamaky/twerlo-app:main-abc123` | Branch-specific builds |
| `v1.0.0` | `helhamaky/twerlo-app:v1.0.0` | Semantic versioning |
| `1.0` | `helhamaky/twerlo-app:1.0` | Major.minor version |

## **🔍 Monitoring & Debugging**

### **View Workflow Logs**
1. Go to **Actions** tab
2. Click on workflow run
3. Click on job name
4. View step logs

### **Manual Trigger**
1. Go to **Actions** tab
2. Click **"Build and Push Docker Image"**
3. Click **"Run workflow"**
4. Select branch and click **"Run workflow"**

### **Check Docker Hub**
- Visit: https://hub.docker.com/r/helhamaky/twerlo-app
- See all tags and build history

## **🚨 Troubleshooting**

### **Common Issues**

**1. Docker Hub Authentication Failed**
- Check `DOCKERHUB_TOKEN` secret is correct
- Ensure token has Read & Write permissions

**2. Tests Failing**
- Check test logs in Actions tab
- Ensure all dependencies are in `requirements.txt`

**3. Build Failing**
- Check Dockerfile syntax
- Ensure all files are committed

**4. Security Scan Failing**
- Review Trivy scan results
- Update vulnerable dependencies

### **Debug Commands**

```bash
# Test locally before pushing
python -m pytest tests/ -v

# Build Docker image locally
docker build -t test-image .

# Test Docker image locally
docker run --rm test-image python -c "import app.main; print('OK')"
```

## **🔧 Customization**

### **Modify Docker Image Name**
Edit `.github/workflows/docker-build.yml`:
```yaml
env:
  DOCKER_IMAGE: your-username/your-app-name
```

### **Add More Tests**
Add to the test job:
```yaml
- name: Run additional tests
  run: |
    python -m pytest tests/ -v --cov=app
```

### **Add Notifications**
Add to workflow:
```yaml
- name: Notify on success
  uses: 8398a7/action-slack@v3
  with:
    status: success
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

## **📈 Best Practices**

1. **Always test locally** before pushing
2. **Use semantic versioning** for releases
3. **Review security scan results** regularly
4. **Monitor workflow performance** and optimize
5. **Keep dependencies updated** with Dependabot

## **🎯 Quick Start Checklist**

- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Docker Hub access token created
- [ ] GitHub secrets added
- [ ] First workflow run completed
- [ ] Docker image pushed to Docker Hub
- [ ] Tests passing
- [ ] Security scan completed

---

**✅ Your GitHub Actions are now set up for automatic Docker Hub updates!** 