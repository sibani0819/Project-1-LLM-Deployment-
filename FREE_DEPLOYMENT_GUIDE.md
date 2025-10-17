# 🚀 Free Deployment Guide for Students

## 🎯 Best Free Hosting Options

### 1. **Railway** (Recommended) ⭐
- **Free Tier**: $5 credit monthly (enough for small apps)
- **Easy Setup**: GitHub integration
- **Features**: Automatic deployments, custom domains
- **Perfect for**: FastAPI applications

### 2. **Render** (Great for Students)
- **Free Tier**: 750 hours/month
- **Features**: Automatic deployments, SSL, custom domains
- **Limitations**: Sleeps after 15 minutes of inactivity
- **Perfect for**: Development and testing

### 3. **Heroku** (Classic Choice)
- **Free Tier**: Discontinued, but has low-cost options
- **Alternative**: Use Heroku's $5/month plan
- **Features**: Easy deployment, add-ons

### 4. **Fly.io** (Developer Friendly)
- **Free Tier**: 3 shared-cpu VMs
- **Features**: Global deployment, fast
- **Perfect for**: Production applications

### 5. **PythonAnywhere** (Python Focused)
- **Free Tier**: Limited but good for learning
- **Features**: Python-specific hosting
- **Perfect for**: Students learning Python

## 🚀 Quick Deployment with Railway (Recommended)

### Step 1: Prepare Your Project
```bash
# Create a Procfile for Railway
echo "web: uvicorn main:app --host 0.0.0.0 --port $PORT" > Procfile

# Create railway.json for configuration
echo '{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "uvicorn main:app --host 0.0.0.0 --port $PORT",
    "healthcheckPath": "/ping"
  }
}' > railway.json
```

### Step 2: Deploy to Railway
1. **Sign up**: Go to [railway.app](https://railway.app)
2. **Connect GitHub**: Link your GitHub account
3. **Deploy**: Select your repository
4. **Set Environment Variables**:
   ```
   GITHUB_PAT=your_github_token
   VERIFICATION_SECRET=your_secret
   LLM_API_KEY=your_openai_key
   GEMINI_API_KEY=your_gemini_key
   ```

### Step 3: Get Your URL
- Railway will give you a URL like: `https://your-app.railway.app`
- Test: `https://your-app.railway.app/ping`

## 🚀 Alternative: Render Deployment

### Step 1: Create render.yaml
```yaml
services:
  - type: web
    name: llm-code-deployment
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: GITHUB_PAT
        sync: false
      - key: VERIFICATION_SECRET
        sync: false
      - key: LLM_API_KEY
        sync: false
      - key: GEMINI_API_KEY
        sync: false
```

### Step 2: Deploy to Render
1. **Sign up**: Go to [render.com](https://render.com)
2. **Connect GitHub**: Link your repository
3. **Deploy**: Render will auto-detect Python
4. **Set Environment Variables**: Add your API keys

## 🚀 Alternative: Fly.io Deployment

### Step 1: Install Fly CLI
```bash
# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex

# Or download from: https://fly.io/docs/hands-on/install-flyctl/
```

### Step 2: Create fly.toml
```toml
app = "llm-code-deployment"
primary_region = "ord"

[build]

[env]
  PORT = "8080"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0
  processes = ["app"]

[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory_mb = 256
```

### Step 3: Deploy
```bash
# Login to Fly
fly auth login

# Deploy
fly launch
fly deploy
```

## 🔧 Environment Variables Setup

### For All Platforms:
```env
GITHUB_PAT=your_github_personal_access_token
VERIFICATION_SECRET=your_secret_key_here
LLM_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
PORT=8080
```

### GitHub Token Setup:
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with scopes:
   - `repo` (full control of private repositories)
   - `public_repo` (access public repositories)
   - `admin:repo_hook` (full control of repository hooks)
   - `workflow` (update GitHub Action workflows)

## 📱 Testing Your Deployment

### Health Check:
```bash
curl https://your-app.railway.app/ping
```

### Create Task:
```bash
curl -X POST https://your-app.railway.app/task \
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

## 🎯 Student-Specific Tips

### 1. **GitHub Student Pack**
- Sign up for [GitHub Student Pack](https://education.github.com/pack)
- Get free credits for various services
- Includes free domains and hosting

### 2. **Educational Discounts**
- **Railway**: Student discount available
- **Render**: Free tier is generous
- **Fly.io**: Free tier for small apps

### 3. **Cost Optimization**
- Use free tiers efficiently
- Monitor usage to avoid overages
- Use environment variables for secrets

## 🚨 Important Notes

### Free Tier Limitations:
- **Render**: Sleeps after 15 minutes of inactivity
- **Railway**: Limited to $5 credit monthly
- **Fly.io**: Limited to 3 VMs

### Production Considerations:
- **Monitoring**: Set up health checks
- **Logging**: Use platform logging features
- **Backup**: Keep your code in GitHub
- **Scaling**: Upgrade when needed

## 🎉 Success Checklist

- [ ] Choose hosting platform
- [ ] Set up environment variables
- [ ] Deploy application
- [ ] Test health endpoint
- [ ] Test task creation
- [ ] Monitor logs
- [ ] Set up custom domain (optional)

## 📞 Support

- **Railway**: [Discord Community](https://discord.gg/railway)
- **Render**: [Documentation](https://render.com/docs)
- **Fly.io**: [Community Forum](https://community.fly.io)

Your LLM Code Deployment API is now ready for free hosting! 🚀
