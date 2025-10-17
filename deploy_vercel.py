#!/usr/bin/env python3
"""
Vercel Deployment Script for LLM Code Deployment API
"""

import os
import subprocess
import sys
from pathlib import Path

def check_vercel_cli():
    """Check if Vercel CLI is installed"""
    try:
        result = subprocess.run(['vercel', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Vercel CLI installed: {result.stdout.strip()}")
            return True
        else:
            print("❌ Vercel CLI not found")
            return False
    except FileNotFoundError:
        print("❌ Vercel CLI not found")
        return False

def install_vercel_cli():
    """Install Vercel CLI"""
    print("\n📦 Installing Vercel CLI...")
    print("Run this command in your terminal:")
    print("npm install -g vercel")
    print("\nOr visit: https://vercel.com/docs/cli")

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'main.py',
        'requirements.txt',
        'vercel.json',
        'api/index.py'
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
    
    print("Required environment variables for Vercel:")
    for key, description in env_vars.items():
        print(f"  {key}: {description}")
    
    print("\n📝 Set these in Vercel dashboard → Project → Settings → Environment Variables")

def deploy_vercel():
    """Deploy to Vercel"""
    print("\n🚀 Vercel Deployment")
    print("=" * 40)
    
    if not check_vercel_cli():
        install_vercel_cli()
        return
    
    print("1. Login to Vercel:")
    print("   vercel login")
    
    print("\n2. Deploy your project:")
    print("   vercel")
    
    print("\n3. Set environment variables in Vercel dashboard:")
    print("   - Go to your project → Settings → Environment Variables")
    print("   - Add: GITHUB_PAT, VERIFICATION_SECRET, LLM_API_KEY, GEMINI_API_KEY")
    
    print("\n4. Redeploy with environment variables:")
    print("   vercel --prod")
    
    print("\n✅ Your API will be available at: https://your-project.vercel.app")

def deploy_github():
    """Deploy via GitHub integration"""
    print("\n🚀 GitHub Integration Deployment")
    print("=" * 40)
    print("1. Push your code to GitHub:")
    print("   git add .")
    print("   git commit -m 'Add Vercel deployment'")
    print("   git push origin main")
    
    print("\n2. Go to https://vercel.com")
    print("3. Sign up with GitHub")
    print("4. Click 'New Project'")
    print("5. Import your GitHub repository")
    print("6. Configure:")
    print("   - Framework Preset: Other")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Output Directory: (leave empty)")
    print("7. Set environment variables")
    print("8. Deploy!")
    
    print("\n✅ Your API will be available at: https://your-project.vercel.app")

def test_deployment(url):
    """Test the deployed API"""
    print(f"\n🧪 Testing Deployment: {url}")
    print("=" * 40)
    
    try:
        import requests
        response = requests.get(f"{url}/ping", timeout=10)
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"Response: {response.json()}")
            
            # Test task creation
            print("\n🧪 Testing task creation...")
            task_data = {
                "email": "test@example.com",
                "secret": "test_secret",
                "task": "test-vercel-123",
                "round": 1,
                "nonce": "test-456",
                "brief": "Create a simple calculator",
                "checks": ["Calculator works"],
                "evaluation_url": "https://httpbin.org/post",
                "attachments": []
            }
            
            response = requests.post(f"{url}/task", json=task_data, timeout=30)
            if response.status_code == 200:
                print("✅ Task creation test passed!")
                print(f"Response: {response.json()}")
            else:
                print(f"❌ Task creation failed: {response.status_code}")
                print(f"Response: {response.text}")
                
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing deployment: {str(e)}")

def main():
    """Main deployment function"""
    print("🚀 LLM Code Deployment API - Vercel Deployment")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Please ensure all required files are present")
        return
    
    # Setup environment
    setup_environment()
    
    # Show deployment options
    print("\n🎯 Choose Your Deployment Method:")
    print("1. Vercel CLI (Recommended)")
    print("2. GitHub Integration (Easy)")
    print("3. Both methods")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1" or choice == "3":
        deploy_vercel()
    
    if choice == "2" or choice == "3":
        deploy_github()
    
    # Test deployment
    if choice in ["1", "2", "3"]:
        print("\n🧪 After deployment, test your API:")
        url = input("Enter your Vercel app URL (or press Enter to skip): ").strip()
        if url:
            test_deployment(url)
    
    print("\n🎉 Vercel deployment guide complete!")
    print("📚 For detailed instructions, see VERCEL_DEPLOYMENT_GUIDE.md")
    print("\n🎯 Your API URL will be perfect for assignment submission!")

if __name__ == "__main__":
    main()
