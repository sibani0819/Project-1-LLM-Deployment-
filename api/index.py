"""
Vercel API handler for LLM Code Deployment
This file makes the FastAPI app compatible with Vercel's serverless functions
"""

import sys
import os
from pathlib import Path

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

# Import the FastAPI app
from main import app

# Export the app for Vercel
handler = app
