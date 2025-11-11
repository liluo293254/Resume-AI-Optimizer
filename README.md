# AI 智能简历优化器 (Resume AI Optimizer)

一个基于 AI 技术的智能简历优化工具，使用 Python + FastAPI + React + SQLite + Ollama 构建，支持本地部署和实时优化。

## ✨ 特性

- 🤖 **AI 驱动优化**: 使用 Ollama 本地 LLM 或 OpenAI API 优化简历内容
- 🎯 **职位匹配**: 根据目标职位描述进行针对性优化
- 💾 **本地优先**: 所有数据存储在本地 SQLite 数据库，保护隐私
- 🚀 **一键启动**: 提供便捷的启动脚本，快速开始使用
- 📱 **现代化 UI**: 响应式设计，直观易用的用户界面
- 🔄 **实时预览**: 即时查看优化结果和建议

## 🛠️ 技术栈

- **后端**: Python 3.11+, FastAPI, SQLAlchemy, Pydantic
- **前端**: React 18+, TypeScript, Vite
- **数据库**: SQLite (开发) / PostgreSQL (生产可选)
- **AI 引擎**: Ollama (本地 LLM) / OpenAI API (可选)
- **部署**: Docker Compose, 支持本地开发和生产部署

## 📋 前置要求

- Python 3.11 或更高版本
- Node.js 18 或更高版本
- Ollama (用于本地 AI 模型)
  - 下载: https://ollama.ai
  - 安装后运行: `ollama serve`
  - 拉取模型: `ollama pull llama3.2`

## 🚀 快速开始

### 方法 1: 使用启动脚本 (推荐)

**Linux/macOS:**
```bash
chmod +x start.sh
./start.sh
```

**Windows:**
```cmd
start.bat
```

### 方法 2: 手动启动

#### 1. 启动后端

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

后端将在 http://localhost:8000 启动

#### 2. 启动前端

```bash
cd frontend
npm install
npm run dev
```

前端将在 http://localhost:5173 启动

### 方法 3: 使用 Docker Compose

```bash
docker-compose up -d
```

**注意**: 首次使用需要手动拉取 Ollama 模型:
```bash
docker exec -it resume-ai-optimizer-ollama-1 ollama pull llama3.2
```

## ⚙️ 配置

### 后端配置

复制 `backend/.env.example` 为 `backend/.env` 并修改配置:

```env
# Ollama配置
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# OpenAI配置（可选）
USE_OPENAI=False
OPENAI_API_KEY=your-api-key-here
```

### 前端配置

创建 `frontend/.env`:

```env
VITE_API_URL=http://localhost:8000/api
```

## 📖 API 文档

启动后端后，访问以下地址查看 API 文档:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 主要 API 端点

- `POST /api/resume/optimize` - 直接优化简历（不保存）
- `POST /api/resume/` - 创建简历记录
- `POST /api/resume/{id}/optimize` - 优化指定简历
- `GET /api/resume/{id}` - 获取简历详情
- `GET /api/resume/` - 获取简历列表
- `GET /api/health` - 健康检查

## 🎯 使用指南

1. **打开应用**: 访问 http://localhost:5173
2. **输入简历**: 在左侧文本框中粘贴您的原始简历内容
3. **添加职位描述** (可选): 输入目标职位描述，AI 将根据职位要求优化简历
4. **开始优化**: 点击"开始优化"按钮
5. **查看结果**: 优化后的简历将显示在右侧，您可以复制结果

## 📁 项目结构

```
.
├── backend/                 # FastAPI 后端
│   ├── app/
│   │   ├── config.py       # 配置管理
│   │   ├── database.py     # 数据库模型
│   │   ├── routers/        # API 路由
│   │   └── services/       # 业务逻辑服务
│   ├── main.py             # 应用入口
│   └── requirements.txt    # Python 依赖
├── frontend/               # React 前端
│   ├── src/
│   │   ├── components/     # React 组件
│   │   ├── services/       # API 服务
│   │   └── App.tsx         # 主应用组件
│   └── package.json        # Node.js 依赖
├── docker-compose.yml      # Docker 编排配置
├── start.sh                # Linux/macOS 启动脚本
├── start.bat               # Windows 启动脚本
└── README.md               # 项目文档
```

## 🧪 开发

### 运行测试

```bash
# 后端测试
cd backend
pytest

# 前端测试
cd frontend
npm test
```

### 代码规范

- Python: 遵循 PEP 8
- TypeScript/React: 使用 ESLint

## 🐛 故障排除

### Ollama 连接失败

1. 确保 Ollama 服务正在运行: `ollama serve`
2. 检查模型是否已下载: `ollama list`
3. 如果未下载，运行: `ollama pull llama3.2`

### 端口冲突

如果 8000 或 5173 端口被占用，可以修改:
- 后端: `backend/app/config.py` 中的 `PORT`
- 前端: `frontend/vite.config.ts` 中的 `server.port`

### 数据库错误

删除 `backend/resume_optimizer.db` 文件，应用将自动重新创建数据库。

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request!

## 📧 联系方式

如有问题或建议，请提交 Issue。

---

**享受使用 AI 智能简历优化器！** 🎉

