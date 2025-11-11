#!/bin/bash

# AI智能简历优化器 - 一键启动脚本

set -e

echo "🚀 启动 AI 智能简历优化器..."

# 检查Python版本
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python 3，请先安装 Python 3.11+"
    exit 1
fi

# 检查Node.js版本
if ! command -v node &> /dev/null; then
    echo "❌ 错误: 未找到 Node.js，请先安装 Node.js 18+"
    exit 1
fi

# 检查Ollama是否运行
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "⚠️  警告: Ollama 服务未运行"
    echo "   请先启动 Ollama: ollama serve"
    echo "   然后拉取模型: ollama pull llama3.2"
    read -p "   是否继续? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# 启动后端
echo "📦 设置后端环境..."
cd backend
if [ ! -d "venv" ]; then
    echo "   创建虚拟环境..."
    python3 -m venv venv
fi

echo "   安装Python依赖..."
source venv/bin/activate || source venv/Scripts/activate
pip install -q -r requirements.txt

echo "   启动后端服务器 (http://localhost:8000)..."
python main.py &
BACKEND_PID=$!
cd ..

# 等待后端启动
sleep 3

# 启动前端
echo "📦 设置前端环境..."
cd frontend
if [ ! -d "node_modules" ]; then
    echo "   安装Node.js依赖..."
    npm install
fi

echo "   启动前端开发服务器 (http://localhost:5173)..."
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ 启动完成!"
echo ""
echo "📍 服务地址:"
echo "   前端: http://localhost:5173"
echo "   后端API: http://localhost:8000"
echo "   API文档: http://localhost:8000/docs"
echo ""
echo "按 Ctrl+C 停止所有服务"

# 等待用户中断
trap "echo ''; echo '🛑 正在停止服务...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT
wait

