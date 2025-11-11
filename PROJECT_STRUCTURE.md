# 项目结构说明

## 📁 目录结构

```
Resume AI Optimizer/
├── .specify/
│   └── memory/
│       └── constitution.md          # 项目宪章
├── backend/                          # FastAPI 后端
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py                # 应用配置
│   │   ├── database.py              # 数据库模型和配置
│   │   ├── routers/                 # API 路由
│   │   │   ├── __init__.py
│   │   │   ├── health.py            # 健康检查路由
│   │   │   └── resume.py            # 简历优化路由
│   │   └── services/                # 业务逻辑服务
│   │       ├── __init__.py
│   │       └── ai_service.py        # AI 优化服务（Ollama/OpenAI）
│   ├── main.py                      # FastAPI 应用入口
│   ├── requirements.txt             # Python 依赖
│   ├── Dockerfile                   # 后端 Docker 镜像
│   └── env.example                  # 环境变量示例
├── frontend/                         # React 前端
│   ├── src/
│   │   ├── components/
│   │   │   ├── ResumeOptimizer.tsx  # 主优化组件
│   │   │   └── ResumeOptimizer.css  # 组件样式
│   │   ├── services/
│   │   │   └── api.ts               # API 客户端
│   │   ├── App.tsx                  # 主应用组件
│   │   ├── App.css                  # 应用样式
│   │   ├── main.tsx                 # React 入口
│   │   ├── index.css                # 全局样式
│   │   └── vite-env.d.ts            # Vite 类型定义
│   ├── index.html                   # HTML 模板
│   ├── package.json                 # Node.js 依赖
│   ├── tsconfig.json                # TypeScript 配置
│   ├── tsconfig.node.json           # Node TypeScript 配置
│   ├── vite.config.ts               # Vite 配置
│   ├── Dockerfile                   # 前端 Docker 镜像
│   ├── .eslintrc.cjs                # ESLint 配置
│   └── .gitignore                   # Git 忽略文件
├── docker-compose.yml               # Docker Compose 配置
├── start.sh                         # Linux/macOS 启动脚本
├── start.bat                        # Windows 启动脚本
├── README.md                        # 项目主文档
├── QUICKSTART.md                    # 快速启动指南
├── PROJECT_STRUCTURE.md             # 本文件
└── .gitignore                       # 项目级 Git 忽略文件
```

## 🔧 核心组件说明

### 后端 (Backend)

- **main.py**: FastAPI 应用主入口，配置 CORS 和路由
- **app/config.py**: 集中管理所有配置（数据库、Ollama、OpenAI等）
- **app/database.py**: SQLAlchemy 数据库模型和会话管理
- **app/routers/resume.py**: 简历优化的 RESTful API 端点
- **app/services/ai_service.py**: AI 优化核心逻辑，支持 Ollama 和 OpenAI

### 前端 (Frontend)

- **src/App.tsx**: 应用主组件
- **src/components/ResumeOptimizer.tsx**: 简历优化器主界面组件
- **src/services/api.ts**: 封装所有后端 API 调用

### 配置文件

- **docker-compose.yml**: 一键启动所有服务（后端、前端、Ollama）
- **start.sh / start.bat**: 本地开发环境一键启动脚本
- **requirements.txt**: Python 依赖列表
- **package.json**: Node.js 依赖和脚本

## 🚀 启动流程

1. **环境检查**: 验证 Python、Node.js、Ollama 是否安装
2. **后端启动**: 创建虚拟环境 → 安装依赖 → 启动 FastAPI 服务器
3. **前端启动**: 安装依赖 → 启动 Vite 开发服务器
4. **服务就绪**: 前端 (5173) 和后端 (8000) 端口监听

## 📊 数据流

```
用户输入简历
    ↓
React 前端 (ResumeOptimizer.tsx)
    ↓
API 调用 (api.ts)
    ↓
FastAPI 后端 (resume.py)
    ↓
AI 服务 (ai_service.py)
    ↓
Ollama/OpenAI
    ↓
返回优化结果
    ↓
显示在 UI
```

## 🔐 环境变量

### 后端 (.env)
- `OLLAMA_BASE_URL`: Ollama 服务地址
- `OLLAMA_MODEL`: 使用的模型名称
- `DATABASE_URL`: 数据库连接字符串
- `USE_OPENAI`: 是否使用 OpenAI（可选）
- `OPENAI_API_KEY`: OpenAI API 密钥（可选）

### 前端 (.env)
- `VITE_API_URL`: 后端 API 地址

## 🎯 扩展点

- **AI 服务**: 在 `ai_service.py` 中添加更多优化策略
- **数据库**: 在 `database.py` 中添加更多数据模型
- **API 端点**: 在 `routers/` 中添加新的路由模块
- **UI 组件**: 在 `components/` 中添加新的 React 组件

