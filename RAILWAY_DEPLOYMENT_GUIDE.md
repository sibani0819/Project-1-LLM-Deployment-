# 🚀 Railway Deployment Guide for LLM Code Deployment API

## ✅ **Fixed Issues**

I've cleaned up your `requirements.txt` file - it now has only the essential packages (36 instead of 300+):
- ✅ **FastAPI** and core dependencies
- ✅ **GitHub integration** (PyGithub)
- ✅ **LLM integration** (OpenAI, Gemini)
- ✅ **HTTP clients** (requests, httpx)
- ✅ **Environment management** (python-dotenv)

## 🔧 **Fixed Railway Port Issue**

I've also fixed the `$PORT` environment variable issue:
- ✅ **Created `start_railway.py`** - Handles port configuration properly
- ✅ **Updated `Procfile`** - Uses the new startup script
- ✅ **Updated `railway.json`** - Railway-specific configuration
- ✅ **Port handling** - Defaults to 8000 if PORT not set

## 🚀 **Railway Deployment Steps**

### **Step 1: Push to GitHub**
```bash
git add .
git commit -m "Fix requirements.txt for Railway deployment"
git push origin main
```

### **Step 2: Deploy to Railway**
1. **Go to**: [railway.app](https://railway.app)
2. **Sign up** with GitHub
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**
6. **Railway will auto-detect Python**

### **Step 3: Set Environment Variables**
In Railway dashboard → Project → Variables:
```
GITHUB_PAT=your_github_personal_access_token
VERIFICATION_SECRET=your_secret_key
LLM_API_KEY=your_openai_api_key (optional)
GEMINI_API_KEY=your_gemini_api_key (optional)
```

### **Step 4: Deploy**
- Railway will automatically build and deploy
- You'll get a URL like: `https://your-app.railway.app`

## 🧪 **Test Your Railway Deployment**

### **Health Check:**
```bash
curl https://your-app.railway.app/ping
```

### **Create Task:**
```bash
curl -X POST https://your-app.railway.app/task \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "secret": "your_secret",
    "task": "test-railway-123",
    "round": 1,
    "nonce": "test-456",
    "brief": "Create a simple calculator",
    "checks": ["Calculator works properly"],
    "evaluation_url": "https://httpbin.org/post",
    "attachments": []
  }'
```

### **Revise Task:**
```bash
curl -X POST https://your-app.railway.app/revise \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "secret": "your_secret",
    "task": "test-railway-123",
    "round": 2,
    "nonce": "test-456",
    "brief": "Add dark mode support",
    "checks": ["Dark mode works"],
    "evaluation_url": "https://httpbin.org/post",
    "attachments": []
  }'
```

## 📊 **Your API Endpoints**

After deployment, you'll have:
```
https://your-app.railway.app/ping          # Health check
https://your-app.railway.app/task          # Create task
https://your-app.railway.app/revise        # Revise task
https://your-app.railway.app/health        # System health
```

## 🎯 **Perfect for Assignment Submission**

### **Your API URL:**
```
https://your-app.railway.app
```

### **Response Format:**
```json
{
  "email": "user@example.com",
  "task": "app-name-123",
  "round": 1,
  "nonce": "unique-nonce",
  "repo_url": "https://github.com/username/repo",
  "commit_sha": "main",
  "pages_url": "https://username.github.io/repo"
}
```

## 🎉 **Railway Benefits**

- ✅ **Free**: $5 credit monthly (enough for small apps)
- ✅ **Fast**: Automatic deployments from GitHub
- ✅ **Reliable**: Enterprise-grade infrastructure
- ✅ **Easy**: GitHub integration
- ✅ **Professional**: Clean URLs
- ✅ **Monitoring**: Built-in analytics

## 🔧 **Railway Configuration**

Your project already has:
- ✅ `Procfile` - For Railway deployment
- ✅ `railway.json` - Configuration
- ✅ `requirements.txt` - Clean dependencies
- ✅ `main.py` - FastAPI application

## 🚨 **Important Notes**

### **Railway Free Tier:**
- **$5 credit monthly** (usually enough)
- **Automatic deployments** from GitHub
- **Custom domains** available
- **Environment variables** management

### **For Production:**
- **Pro Plan**: $5/month for more resources
- **Team Plan**: For collaboration
- **Enterprise**: For high-volume usage

## 🎯 **Assignment Submission Format**

```
API Base URL: https://your-app.railway.app

Endpoints:
- Health: https://your-app.railway.app/ping
- Create: https://your-app.railway.app/task
- Revise: https://your-app.railway.app/revise

Response Format:
{
  "email": "user@example.com",
  "task": "app-name-123",
  "round": 1,
  "nonce": "unique-nonce",
  "repo_url": "https://github.com/username/repo",
  "commit_sha": "main",
  "pages_url": "https://username.github.io/repo"
}
```

## 🚀 **Quick Start**

1. **Push to GitHub**: `git push origin main`
2. **Go to Railway**: [railway.app](https://railway.app)
3. **Deploy**: Connect your GitHub repo
4. **Set Variables**: Add your API keys
5. **Test**: Use the curl commands above

## 🎉 **Success!**

Your LLM Code Deployment API is now ready for Railway deployment! 

**Perfect for assignment submission** - professional, fast, and reliable! 🚀
