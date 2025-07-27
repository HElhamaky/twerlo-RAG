# 🧪 Test Running Guide

## **Quick Commands**

### **Local Testing**
```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run specific test file
python -m pytest tests/test_api.py

# Run specific test function
python -m pytest tests/test_api.py::test_register_user

# Run with print statements visible
python -m pytest -s

# Run and show coverage
python -m pytest --cov=app
```

### **Docker Testing**
```bash
# Run tests in Docker container
docker run --rm twerlo-app python -m pytest -v

# Run tests with coverage in Docker
docker run --rm twerlo-app python -m pytest --cov=app
```

### **Docker Compose Testing**
```bash
# Run tests using docker-compose
docker-compose run --rm app python -m pytest -v
```

## **Test Categories**

### **Current Tests**
- ✅ `test_root` - Tests the root endpoint
- ✅ `test_health` - Tests the health check endpoint  
- ✅ `test_register_user` - Tests user registration
- ✅ `test_login_user` - Tests user login

### **Test Results**
```
=========================================== test session starts ===========================================
platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
collected 4 items

tests\test_api.py ....                                                                               [100%] 
====================================== 4 passed, 4 warnings in 4.50s ======================================
```

## **Advanced Test Commands**

### **Debug Mode**
```bash
# Run with debug output
python -m pytest -v -s --tb=long

# Run single test with debug
python -m pytest tests/test_api.py::test_register_user -v -s
```

### **Coverage Testing**
```bash
# Install coverage (if not installed)
pip install pytest-cov

# Run with coverage
python -m pytest --cov=app --cov-report=html

# View coverage report
# Open htmlcov/index.html in browser
```

### **Performance Testing**
```bash
# Run with timing
python -m pytest --durations=10

# Run with performance profiling
python -m pytest --profile
```

## **Test Configuration**

### **pytest.ini (Optional)**
Create a `pytest.ini` file for custom configuration:
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

### **Environment Variables for Testing**
```bash
# Set test environment
export TESTING=true
export DATABASE_URL=sqlite:///./test.db

# Run tests with environment
TESTING=true python -m pytest
```

## **Writing New Tests**

### **Example Test Structure**
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_new_endpoint():
    """Test a new API endpoint."""
    response = client.get("/new-endpoint")
    assert response.status_code == 200
    assert "expected_data" in response.json()
```

### **Test Best Practices**
1. **Use unique data** - Avoid conflicts with existing data
2. **Clean up after tests** - Don't leave test data in database
3. **Test both success and failure cases**
4. **Use descriptive test names**
5. **Add docstrings to explain test purpose**

## **Troubleshooting**

### **Common Issues**
1. **Database conflicts** - Use unique test data
2. **Import errors** - Check Python path and dependencies
3. **Authentication issues** - Ensure test users are created properly

### **Debug Commands**
```bash
# Check what tests are collected
python -m pytest --collect-only

# Run with maximum verbosity
python -m pytest -vvv

# Run and stop on first failure
python -m pytest -x
```

## **Continuous Integration**

### **GitHub Actions Example**
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: python -m pytest -v
```

## **Test Reports**

### **Generate HTML Report**
```bash
python -m pytest --html=report.html --self-contained-html
```

### **Generate JUnit XML**
```bash
python -m pytest --junitxml=test-results.xml
```

---

**✅ All tests are currently passing!** 