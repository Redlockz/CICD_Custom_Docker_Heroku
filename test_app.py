"""
Unit tests for Flask application
"""
import pytest
import json
from app import app


@pytest.fixture
def client():
    """Create a test client for the app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test the home endpoint returns correct response"""
    response = client.get('/')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'message' in data
    assert data['status'] == 'running'
    assert data['version'] == '1.0.0'


def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert data['service'] == 'flask-app'


def test_info_endpoint(client):
    """Test the info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'app' in data
    assert 'environment' in data
    assert 'port' in data


def test_404_endpoint(client):
    """Test that non-existent endpoints return 404"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
