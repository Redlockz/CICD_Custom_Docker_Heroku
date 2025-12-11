"""
Integration tests for Docker deployment
Tests that the containerized app is accessible
"""
import requests
import time
import sys
import os


def test_container_accessibility(base_url=None):
    """Test if the containerized app is accessible"""
    if base_url is None:
        base_url = os.getenv("APP_BASE_URL", "http://localhost:5000")
    
    max_retries = 30
    retry_delay = 2
    
    print(f"Testing accessibility at {base_url}")
    
    # Wait for container to be ready
    for attempt in range(max_retries):
        try:
            response = requests.get(f"{base_url}/health", timeout=5)
            if response.status_code == 200:
                print(f"✓ Container is accessible (attempt {attempt + 1})")
                break
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                print(f"Waiting for container... (attempt {attempt + 1}/{max_retries})")
                time.sleep(retry_delay)
            else:
                print(f"✗ Container failed to become accessible: {e}")
                return False
    
    # Test home endpoint
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        assert response.status_code == 200
        data = response.json()
        assert 'message' in data
        assert data['status'] == 'running'
        print("✓ Home endpoint test passed")
    except Exception as e:
        print(f"✗ Home endpoint test failed: {e}")
        return False
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        assert response.status_code == 200
        data = response.json()
        assert data['status'] == 'healthy'
        print("✓ Health endpoint test passed")
    except Exception as e:
        print(f"✗ Health endpoint test failed: {e}")
        return False
    
    # Test info endpoint
    try:
        response = requests.get(f"{base_url}/api/info", timeout=5)
        assert response.status_code == 200
        data = response.json()
        assert 'app' in data
        print("✓ Info endpoint test passed")
    except Exception as e:
        print(f"✗ Info endpoint test failed: {e}")
        return False
    
    print("\n✓ All container accessibility tests passed!")
    return True


if __name__ == "__main__":
    success = test_container_accessibility()
    sys.exit(0 if success else 1)
