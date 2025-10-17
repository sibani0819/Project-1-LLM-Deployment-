# LLM Code Deployment API

A scalable FastAPI application that automatically generates, deploys, and updates web applications using LLM assistance. The system handles millions of records and is SEO-optimized for production use.

## 🚀 Features

- **Automatic Code Generation**: Uses OpenAI, Gemini, or AIPipe.org fallback
- **GitHub Integration**: Creates repositories with GitHub Pages
- **Round-based Updates**: Supports initial creation and subsequent modifications
- **Scalable Architecture**: Handles millions of records efficiently
- **SEO Optimized**: Production-ready applications
- **CSS & JavaScript Generation**: Properly separated and optimized files

## 📋 API Endpoints

### Health Checks
- `GET /ping` - Simple health check
- `GET /health` - Comprehensive system status

### Task Management
- `POST /task` - Create new application (Round 1)
- `POST /revise` - Modify existing application (Round 2+)

## 🔧 Setup

### Prerequisites
- Python 3.8+
- GitHub Personal Access Token
- OpenAI API Key (optional)
- Gemini API Key (optional)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd llm-code-deployment-project1

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Environment Variables
```env
GITHUB_PAT=your_github_token
VERIFICATION_SECRET=your_secret_key
LLM_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
```

### Running the Application
```bash
# Development
python main.py

# Production
python build_and_deploy.py
```

## 🧪 Testing

### Quick Test
```bash
# Test health
curl -X GET http://localhost:8000/ping

# Test task creation
curl -X POST http://localhost:8000/task \
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

### Postman Collection
Import `LLM_Code_Deployment_API.postman_collection.json` for comprehensive testing.

## 📊 Response Format

Both `/task` and `/revise` endpoints return:
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

## 🔄 Workflow

1. **Round 1**: Create initial application
2. **Round 2+**: Modify existing application with new features
3. **Automatic Deployment**: GitHub Pages updated automatically
4. **Code Generation**: CSS and JavaScript properly separated

## 🛠️ Architecture

- **FastAPI**: High-performance web framework
- **GitHub API**: Repository management
- **LLM Integration**: OpenAI, Gemini, AIPipe.org
- **Background Processing**: Asynchronous task handling
- **Error Handling**: Comprehensive retry mechanisms

## 📈 Performance

- **Scalable**: Handles millions of records
- **Fast**: 15-40 seconds processing time
- **Reliable**: Multiple LLM fallbacks
- **SEO Optimized**: Production-ready applications

## 🔒 Security

- **Secret Verification**: API authentication
- **Input Validation**: Comprehensive request validation
- **Error Handling**: Secure error responses
- **Rate Limiting**: Built-in protection

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues and questions, please check the logs and GitHub repository status.