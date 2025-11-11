# 快速启动指南

## 🚀 5分钟快速开始

### 步骤 1: 安装 Ollama

1. 访问 https://ollama.ai 下载并安装 Ollama
2. 启动 Ollama 服务（通常会自动启动）
3. 拉取模型:
   ```bash
   ollama pull llama3.2
   ```

### 步骤 2: 启动应用

**Windows 用户:**
```cmd
start.bat
```

**Linux/macOS 用户:**
```bash
chmod +x start.sh
./start.sh
```

### 步骤 3: 使用应用

1. 打开浏览器访问: http://localhost:5173
2. 在左侧输入您的简历内容
3. （可选）输入目标职位描述
4. 点击"开始优化"
5. 查看右侧的优化结果

## 📝 手动启动（如果脚本不工作）

### 后端启动

```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### 前端启动

```bash
cd frontend
npm install
npm run dev
```

## ✅ 验证安装

访问以下地址确认服务正常运行:

- ✅ 前端: http://localhost:5173
- ✅ 后端健康检查: http://localhost:8000/api/health
- ✅ API 文档: http://localhost:8000/docs

## 🐛 常见问题

**Q: Ollama 连接失败？**
A: 确保 Ollama 正在运行: `ollama serve`，并已下载模型: `ollama pull llama3.2`

**Q: 端口被占用？**
A: 修改 `backend/app/config.py` 中的端口号，或关闭占用端口的程序

**Q: 依赖安装失败？**
A: 确保使用 Python 3.11+ 和 Node.js 18+，尝试使用国内镜像源

## 🎉 开始使用

一切就绪后，开始优化您的简历吧！

