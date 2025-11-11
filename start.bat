@echo off
REM AI智能简历优化器 - Windows一键启动脚本

echo 🚀 启动 AI 智能简历优化器...

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到 Python，请先安装 Python 3.11+
    pause
    exit /b 1
)

REM 检查Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到 Node.js，请先安装 Node.js 18+
    pause
    exit /b 1
)

REM 检查Ollama
curl -s http://localhost:11434/api/tags >nul 2>&1
if errorlevel 1 (
    echo ⚠️  警告: Ollama 服务未运行
    echo    请先启动 Ollama: ollama serve
    echo    然后拉取模型: ollama pull llama3.2
    set /p continue="    是否继续? (y/n) "
    if /i not "%continue%"=="y" exit /b 1
)

REM 启动后端
echo 📦 设置后端环境...
cd backend
if not exist "venv" (
    echo    创建虚拟环境...
    python -m venv venv
)

echo    安装Python依赖...
call venv\Scripts\activate.bat
pip install -q -r requirements.txt

echo    启动后端服务器 (http://localhost:8000)...
start "Backend Server" cmd /k "venv\Scripts\activate.bat && python main.py"
cd ..

timeout /t 3 /nobreak >nul

REM 启动前端
echo 📦 设置前端环境...
cd frontend
if not exist "node_modules" (
    echo    安装Node.js依赖...
    call npm install
)

echo    启动前端开发服务器 (http://localhost:5173)...
start "Frontend Server" cmd /k "npm run dev"
cd ..

echo.
echo ✅ 启动完成!
echo.
echo 📍 服务地址:
echo    前端: http://localhost:5173
echo    后端API: http://localhost:8000
echo    API文档: http://localhost:8000/docs
echo.
echo 关闭此窗口将不会停止服务，请手动关闭后端和前端窗口
pause

