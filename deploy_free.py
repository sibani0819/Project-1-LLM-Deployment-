#!/usr/bin/env python3
"""
Free Deployment Script for LLM Code Deployment API
Supports Railway, Render, and Fly.io
"""

import os
import subprocess
import sys
from pathlib import Path

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'main.py',
        'requirements.txt',
        'Procfile',
        'railway.json'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def setup_environment():
    """Setup environment variables"""
    print("\n🔧 Environment Variables Setup")
    print("=" * 40)
    
    env_vars = {
        'GITHUB_PAT': 'Your GitHub Personal Access Token',
        'VERIFICATION_SECRET': 'Your verification secret',
        'LLM_API_KEY': 'Your OpenAI API key (optional)',
        'GEMINI_API_KEY': 'Your Gemini API key (optional)'
    }
    
    print("Required environment variables:")
    for key, description in env_vars.items():
        print(f"  {key}: {description}")
    
    print("\n📝 Set these in your hosting platform's environment variables section")

def deploy_railway():
    """Deploy to Railway"""
    print("\n🚀 Railway Deployment")
    print("=" * 40)
    print("1. Go to https://railway.app")
    print("2. Sign up with GitHub")
    print("3. Click 'New Project'")
    print("4. Select 'Deploy from GitHub repo'")
    print("5. Choose your repository")
    print("6. Set environment variables:")
    print("   - GITHUB_PAT")
    print("   - VERIFICATION_SECRET")
    print("   - LLM_API_KEY (optional)")
    print("   - GEMINI_API_KEY (optional)")
    print("7. Deploy!")
    print("\n✅ Your app will be available at: https://your-app.railway.app")

def deploy_render():
    """Deploy to Render"""
    print("\n🚀 Render Deployment")
    print("=" * 40)
    print("1. Go to https://render.com")
    print("2. Sign up with GitHub")
    print("3. Click 'New +' → 'Web Service'")
    print("4. Connect your GitHub repository")
    print("5. Configure:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT")
    print("6. Set environment variables")
    print("7. Deploy!")
    print("\n✅ Your app will be available at: https://your-app.onrender.com")

def deploy_fly():
    """Deploy to Fly.io"""
    print("\n🚀 Fly.io Deployment")
    print("=" * 40)
    print("1. Install Fly CLI: https://fly.io/docs/hands-on/install-flyctl/")
    print("2. Run: fly auth login")
    print("3. Run: fly launch")
    print("4. Set secrets:")
    print("   - fly secrets set GITHUB_PAT=your_token")
    print("   - fly secrets set VERIFICATION_SECRET=your_secret")
    print("5. Run: fly deploy")
    print("\n✅ Your app will be available at: https://your-app.fly.dev")

def test_deployment(url):
    """Test the deployed application"""
    print(f"\n🧪 Testing Deployment: {url}")
    print("=" * 40)
    
    try:
        import requests
        response = requests.get(f"{url}/ping", timeout=10)
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing deployment: {str(e)}")

def main():
    """Main deployment function"""
    print("🚀 LLM Code Deployment API - Free Deployment Guide")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Please ensure all required files are present")
        return
    
    # Setup environment
    setup_environment()
    
    # Show deployment options
    print("\n🎯 Choose Your Deployment Platform:")
    print("1. Railway (Recommended) - $5 credit monthly")
    print("2. Render - 750 hours/month free")
    print("3. Fly.io - 3 shared-cpu VMs free")
    print("4. All options")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1" or choice == "4":
        deploy_railway()
    
    if choice == "2" or choice == "4":
        deploy_render()
    
    if choice == "3" or choice == "4":
        deploy_fly()
    
    # Test deployment
    if choice in ["1", "2", "3", "4"]:
        print("\n🧪 After deployment, test your app:")
        url = input("Enter your app URL (or press Enter to skip): ").strip()
        if url:
            test_deployment(url)
    
    print("\n🎉 Deployment guide complete!")
    print("📚 For detailed instructions, see FREE_DEPLOYMENT_GUIDE.md")

if __name__ == "__main__":
    main()
