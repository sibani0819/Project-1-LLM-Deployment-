#!/usr/bin/env python3
"""
Railway startup script for LLM Code Deployment API
Handles port configuration and environment setup
"""

import os
import sys
import uvicorn
from main import app

def main():
    """Start the FastAPI application with Railway configuration"""
    
    # Get port from environment variable, default to 8000
    port = int(os.environ.get("PORT", 8000))
    
    # Get host (Railway expects 0.0.0.0)
    host = os.environ.get("HOST", "0.0.0.0")
    
    # Get environment (production on Railway)
    environment = os.environ.get("ENVIRONMENT", "production")
    
    print(f"🚀 Starting LLM Code Deployment API on Railway")
    print(f"📍 Host: {host}")
    print(f"🔌 Port: {port}")
    print(f"🌍 Environment: {environment}")
    
    # Start the server
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info" if environment == "production" else "debug"
    )

if __name__ == "__main__":
    main()
