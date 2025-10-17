# 🚀 Vercel Deployment Guide for LLM Code Deployment API

## 🎯 Why Vercel?

- **Free Tier**: Generous free tier for students
- **Fast**: Global CDN, instant deployments
- **Easy**: GitHub integration, automatic deployments
- **Perfect for APIs**: Serverless functions
- **Custom Domains**: Free custom domains
- **SSL**: Automatic HTTPS

## 📋 Prerequisites

- GitHub account
- Vercel account (free)
- Your API keys (GitHub PAT, OpenAI, Gemini)

## 🚀 Step-by-Step Deployment

### Step 1: Prepare Your Repository

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Add Vercel deployment files"
   git push origin main
   ```

2. **Required Files** (already created):
   - ✅ `vercel.json` - Vercel configuration
   - ✅ `api/index.py` - Vercel API handler
   - ✅ `requirements.txt` - Dependencies

### Step 2: Deploy to Vercel

1. **Go to**: [vercel.com](https://vercel.com)
2. **Sign up** with GitHub
3. **Click "New Project"**
4. **Import your GitHub repository**
5. **Configure**:
   - Framework Preset: **Other**
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: Leave empty
6. **Set Environment Variables**:
   ```
   GITHUB_PAT=your_github_token
   VERIFICATION_SECRET=your_secret
   LLM_API_KEY=your_openai_key
   GEMINI_API_KEY=your_gemini_key
   ```
7. **Deploy!**

### Step 3: Get Your API URL

After deployment, you'll get a URL like:
```
https://your-project-name.vercel.app
```

## 🧪 Testing Your Vercel API

### Health Check:
```bash
curl https://your-project-name.vercel.app/ping
```

### Create Task:
```bash
curl -X POST https://your-project-name.vercel.app/task \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "secret": "your_secret",
    "task": "test-app-123",
    "round": 1,
    "nonce": "test-456",
    "brief": "Create a simple calculator",
    "checks": ["Calculator works properly"],
    "evaluation_url": "https://httpbin.org/post",
    "attachments": []
  }'
```

### Revise Task:
```bash
curl -X POST https://your-project-name.vercel.app/revise \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "secret": "your_secret",
    "task": "test-app-123",
    "round": 2,
    "nonce": "test-456",
    "brief": "Add dark mode support",
    "checks": ["Dark mode works"],
    "evaluation_url": "https://httpbin.org/post",
    "attachments": []
  }'
```

## 📊 API Endpoints

Your deployed API will have these endpoints:

- **Health Check**: `GET /ping`
- **System Health**: `GET /health`
- **Create Task**: `POST /task`
- **Revise Task**: `POST /revise`
- **List Tasks**: `GET /tasks`
- **Task Status**: `GET /tasks/{task_id}`

## 🎯 Submission Format

### For Your Assignment:
```
API Base URL: https://your-project-name.vercel.app

Endpoints:
- Health: https://your-project-name.vercel.app/ping
- Create: https://your-project-name.vercel.app/task
- Revise: https://your-project-name.vercel.app/revise

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

## 🔧 Vercel Configuration

### vercel.json:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ],
  "env": {
    "PYTHONPATH": "."
  }
}
```

### Environment Variables:
Set these in Vercel dashboard:
- `GITHUB_PAT` - Your GitHub Personal Access Token
- `VERIFICATION_SECRET` - Your secret key
- `LLM_API_KEY` - OpenAI API key (optional)
- `GEMINI_API_KEY` - Gemini API key (optional)

## 🚨 Important Notes

### Vercel Limitations:
- **Function Timeout**: 10 seconds (Hobby plan)
- **Memory**: 1024 MB
- **Request Size**: 4.5 MB
- **Cold Starts**: First request may be slower

### For Production:
- **Pro Plan**: $20/month for longer timeouts
- **Enterprise**: For high-volume usage
- **Monitoring**: Built-in analytics

## 🎉 Benefits of Vercel

### For Students:
- ✅ **Free**: Generous free tier
- ✅ **Fast**: Global CDN
- ✅ **Easy**: GitHub integration
- ✅ **Reliable**: 99.9% uptime
- ✅ **Secure**: Automatic HTTPS
- ✅ **Scalable**: Auto-scaling

### For API Submission:
- ✅ **Professional URL**: Clean, branded URLs
- ✅ **Fast Response**: Global edge network
- ✅ **Reliable**: Enterprise-grade infrastructure
- ✅ **Monitoring**: Built-in analytics
- ✅ **Custom Domain**: Free custom domains

## 📱 Custom Domain (Optional)

1. **Go to**: Vercel dashboard → Project → Settings → Domains
2. **Add Domain**: Enter your domain
3. **Configure DNS**: Point to Vercel
4. **SSL**: Automatic HTTPS

## 🎯 Final Submission

### Your API URL:
```
https://your-project-name.vercel.app
```

### Test Commands:
```bash
# Health check
curl https://your-project-name.vercel.app/ping

# Create task
curl -X POST https://your-project-name.vercel.app/task \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","secret":"your_secret","task":"test-123","round":1,"nonce":"test","brief":"Create a calculator","checks":["Works"],"evaluation_url":"https://httpbin.org/post","attachments":[]}'
```

## 🎉 Success!

Your LLM Code Deployment API is now live on Vercel! 

**Perfect for assignment submission** - professional, fast, and reliable! 🚀
